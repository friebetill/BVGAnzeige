import kivy
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import StringProperty, ListProperty
from datetime import datetime
from kivy.core.window import Window

from bvggrabber.api.actualdeparture import ActualDepartureQueryApi
import json

import re

from executor import execute

# import threading

kivy.require('1.0.5')

Builder.load_file('bvg1280.kv')

def getShortestTenEntries(parsed):
    counterWestend = 0
    counterKoenigin = 0
    listOfEntrys = []
    while len(listOfEntrys) < 10:
        if parsed[0][1][counterWestend]['remaining'] < parsed[1][1][counterKoenigin]['remaining']:
            if parsed[0][1][counterWestend]['line'] != 'Bus  M45':
                listOfEntrys.append(parsed[0][1][counterWestend])
            counterWestend += 1
        else:
            listOfEntrys.append(parsed[1][1][counterKoenigin])
            counterKoenigin += 1
    return listOfEntrys


class BVG(FloatLayout):
    def updateList(self):
        busKoeniginResult = ActualDepartureQueryApi('S Westend (Berlin)').call()
        sWestendResult = ActualDepartureQueryApi('Königin-Elisabeth-Str/Spandauer Damm (Berlin)').call()
        sWestendResult.merge(busKoeniginResult)
        parsed = json.loads(sWestendResult.to_json)

        shortestTenEntries = getShortestTenEntries(parsed)
        for i in range(len(self.destination)):
            linie = shortestTenEntries[i]['line']
            linie = re.sub(r'Bus  ', r'', linie)
            linie = re.sub(r'\n[\s\S]*', r'', linie)
            self.line[i] = linie
            self.destination[i] = shortestTenEntries[i]['end']
            time = int(shortestTenEntries[i]['remaining']/60)
            if time <= 0:
                self.remaining[i] = 'Jetzt'
            else:
                self.remaining[i] = str(time) + 'm'

    def update(self, dt):
        if(self.sleepmode == 1):
            if(not(datetime.now().hour <= 6 or datetime.now().hour >= 21)):
                self.sleepmode = 0
            return
        if(datetime.now().hour <= 6 or datetime.now().hour >= 21):
            self.sleepmode = 1
            execute('xset', 'dpms', 'force', 'off')
            return

        self.time = str(datetime.now().strftime('%H:%M:%S'))
        self.counter += 1
        if(self.counter >= 10):
            self.counter = 0
            self.updateList()
            # t = threading.Thread(target=self.updateList())
            # t.daemon = True
            # t.start()

    sleepmode = 0
    time = StringProperty()
    counter = 10
    listLine = ['0'] * 8
    listDestination = ['0'] * 8
    listRemaining = ['0'] * 8
    line = ListProperty(listLine)
    destination = ListProperty(listDestination)
    remaining = ListProperty(listRemaining)


class BVGApp(App):

    def build(self):
        bvg = BVG()
        Clock.schedule_interval(bvg.update, 1)
        return bvg

if __name__ == '__main__':
    Window.size = (1280, 1024)
    # Window.size = (1920, 1080)
    # Window.fullscreen = True
    BVGApp().run()
