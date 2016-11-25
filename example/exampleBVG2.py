import subprocess
import json

output = subprocess.check_output("/usr/local/bin/bvg-grabber.py 'Königin-Elisabeth-Str/Spandauer Damm (Berlin)' - --vehicle BUS --limit 2", shell=True)
print(type(output))
# outputJson = json.loads(output)
# print(outputJson[0])
