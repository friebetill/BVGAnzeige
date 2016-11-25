from bvggrabber.api.scheduleddeparture import ScheduledDepartureQueryApi
from bvggrabber.api.actualdeparture import ActualDepartureQueryApi
import json


# query = ScheduledDepartureQueryApi('Königin-Elisabeth-Str/Spandauer Damm (Berlin)', 1, limit=2)
# res = query.call()
# print(json.dump(res.to_json, indent=4, sort_keys=True))
aquery = ActualDepartureQueryApi('Königin-Elisabeth-Str/Spandauer Damm (Berlin)')
res2 = aquery.call()
# res.merge(res2)
# parsed = json.loads(res.to_json)
# print(json.dumps(parsed, indent=4, sort_keys=True))
# print(parsed[0])
parsed = json.loads(res2.to_json)
print(parsed[0][1][0])


