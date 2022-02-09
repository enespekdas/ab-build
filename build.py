
import json
import os
import platform
from classes.parseBuildData import ParseBuildData
import subprocess

with open('${{ github.action_path }}/devops-settings-example.json') as json_file:
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
if parseJson.details[0]["dockerFilePath"] == "":
    parseJson.details[0]["dockerFilePath"] = "./Dockerfile"
buildYap=subprocess.check_output("podman build --tag "+parseJson.details[0]["imageName"]+":"+parseJson.details[0]["tag"]+" -f "+parseJson.details[0]["dockerFilePath"], shell=True)
print(buildYap)
echoYap=subprocess.check_output("echo ls yapiyorum", shell=True)
print(echoYap)
lsYap=subprocess.check_output("ls", shell=True)
print(lsYap)
