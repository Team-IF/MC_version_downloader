import wget
import json
import os

def move(MC_version):
    os.mkdir(MC_version)
    os.chdir(MC_version)

def L_Json_download(MC_version):
    url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    wget.download(url)
    with open ("version_manifest.json") as version_manifest:
        version_manifest = version_manifest.read()
    os.remove("version_manifest.json")
    jsons = json.loads(version_manifest).get('versions')
    for dic in jsons:
        for value in dic.values():
            if MC_version == value:
                url = dic.get('url')
                wget.download(url)

def L_Jar_download(MC_version):
    with open (MC_version+".json") as mcjson:
        mcjsons = mcjson.read()
    url = json.loads(mcjsons).get('downloads').get("client").get("url")
    wget.download(url)
    os.rename("client.jar", MC_version+".jar")
    
def L_download(MC_version):
    move(MC_version)
    L_Json_download(MC_version)
    L_Jar_download(MC_version)
