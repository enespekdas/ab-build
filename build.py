
import sys
# sys.path is a list of absolute path strings
sys.path.append('./classes')

import json
import os
import platform
from parseBuildData import ParseBuildData


with open('devops-settings-example.json') as json_file:
    data = dict(json.load(json_file))

parseJson=ParseBuildData()
parseJson.parseDevops(data['devops'])
#Enhancement The parameters will be list that sent to ContainerBuild ex: CDWithHelm
#Load Environment
osSystem = platform.system()
# for item in parseJson.build[0]:
#     if item['builder'] == "docker":
#         osSystem = platform.system()
#         cloudNative.dockerBuildandPush(osSystem)
parseJson.test()

print( parseJson.build)
