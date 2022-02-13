
import json
import os
import platform
from classes.parseBuildData import ParseBuildData
import subprocess
import sys

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

print( sys.argv[0])
print( sys.argv[1])
print( sys.argv[2])
if parseJson.details[0]["dockerFilePath"] == "":
    parseJson.details[0]["dockerFilePath"] = "./Dockerfile"
buildYap=subprocess.check_output("podman build --tag "+parseJson.details[0]["imageName"]+":"+parseJson.details[0]["tag"]+" -f "+parseJson.details[0]["dockerFilePath"], shell=True)

print(parseJson.details)
lsYap=subprocess.check_output("echo podman imajlari listeleniyor", shell=True)
print(lsYap)
podmanImages=subprocess.check_output("podman images", shell=True)
print(podmanImages)

