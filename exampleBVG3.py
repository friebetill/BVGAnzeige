from bvggrabber.api.actualdeparture import ActualDepartureQueryApi
import json

busKoeniginQuery = ActualDepartureQueryApi('Königin-Elisabeth-Str/Spandauer Damm (Berlin)')
busKoeniginResult = busKoeniginQuery.call()
busKoeniginParsed = json.loads(busKoeniginResult.to_json)

sWestendQuery = ActualDepartureQueryApi('S Westend (Berlin)')
sWestendResult = sWestendQuery.call()
sWestendParsed = json.loads(sWestendResult.to_json)

# print(sWestendParsed[0][0])
# print(sWestendParsed[0][1][0]['line'])
# print(sWestendParsed[0][1][0]['start'])
# print(sWestendParsed[0][1][0]['end'])
# print(sWestendParsed[0][1][0]['remaining'])

sWestendResult.merge(busKoeniginResult)
parsed = json.loads(sWestendResult.to_json)

counterWestend = 0
counterKoenigin = 0
listOfEntrys = []
while len(listOfEntrys) < 10:
    if parsed[0][1][counterWestend]['remaining'] < parsed[1][1][counterKoenigin]['remaining']:
        if parsed[0][1][counterWestend]['line']  != 'Bus  M45':
            listOfEntrys.append(parsed[0][1][counterWestend])
            counterWestend += 1
        else:
            counterWestend += 1

    else:
        listOfEntrys.append(parsed[1][1][counterKoenigin])
        counterKoenigin += 1

for i in range(len(listOfEntrys)):
    print(listOfEntrys[i])


# print(busKoeniginParsed)
