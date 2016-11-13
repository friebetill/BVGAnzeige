import kivy
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import StringProperty, ListProperty
from datetime import datetime
from kivy.core.window import Window

from bvggrabber.api.actualdeparture import ActualDepartureQueryApi
import json

import re

kivy.require('1.0.5')

def updateList(listLine, listDestination, listRemaining):
    busKoeniginResult = ActualDepartureQueryApi('S Westend (Berlin)').call()
    sWestendResult = ActualDepartureQueryApi('Königin-Elisabeth-Str/Spandauer Damm (Berlin)').call()
    sWestendResult.merge(busKoeniginResult)
    parsed = json.loads(sWestendResult.to_json)

    shortestTenEntries = getShortestTenEntries(parsed)
    for i in range(len(listLine)):
        linie = shortestTenEntries[i]['line']
        linie = re.sub(r'Bus  ', r'', linie)
        linie = re.sub(r'\n[\s\S]*', r'', linie)
        listLine[i] = linie
        listDestination[i] = shortestTenEntries[i]['end']
        time = int(shortestTenEntries[i]['remaining']/60)
        if time <= 0:
            listRemaining[i] = 'Jetzt'
        else:
            listRemaining[i] = str(time) + 'm'

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
                counterWestend += 1
        else:
            listOfEntrys.append(parsed[1][1][counterKoenigin])
            counterKoenigin += 1
    return listOfEntrys

class BVG(FloatLayout):
    def update(self, dt):
        self.time = str(datetime.now().strftime('%H:%M:%S'))
        self.counter += 1
        if(self.counter >= 10):
            self.counter = 0
            updateList(self.listLine, self.listDestination, self.listRemaining)

    time = StringProperty()
    counter = 0

    listLine = ['0'] * 10
    listDestination = ['0'] * 10
    listRemaining = ['0'] * 10
    line = ListProperty(listLine)
    destination = ListProperty(listDestination)
    remaining = ListProperty(listRemaining)

    updateList(listLine, listDestination, listRemaining)


class BVGApp(App):

    def build(self):
        bvg = BVG()
        Clock.schedule_interval(bvg.update, 1.0)
        return bvg

if __name__ == '__main__':
    # Window.size = (1280, 1024)
    Window.size = (1920, 1080)
    Window.fullscreen = True
    BVGApp().run()
