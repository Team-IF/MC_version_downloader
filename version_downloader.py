import wget
import json
import os
import requests

def L_Json_download(MC_version):
    url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    jsons = requests.get(url).json()['versions']
    for dic in jsons:
        for value in dic.values():
            if MC_version == value:
                url = dic['url']
                L_Jar_download(MC_version,requests.get(url).json())

def L_Jar_download(MC_version,mcjsons):
    url = mcjsons['downloads']['client']['url']
    wget.download(url)
    os.rename("client.jar", MC_version+".jar")

def L_download(MC_version):
    os.mkdir(MC_version)
    os.chdir(MC_version)
    L_Json_download(MC_version)

if __name__=="__main__":
    L_download("1.12.2")
