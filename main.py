import json
import os
import subprocess
import sys

import time

import webview # Package to make webviews for python ( pip install pywebview )

from subprocess import Popen

port=3000 ## Default port if it was not able to read it from manifest.js.
nodeFile="index.js" ## Default JS name to get executed by node.
local=False

def getJSON():
    f = open('manifest.json')
    data=json.load(f)
    f.close()
    return data
def getUrl(): ## Gets the port in the Manifest.json and add it to "localhost:"
    data=getJSON()
    port=data['port']
    nodeFile=data['nodeFile']
    local=data['isLocal']
    url=data['url']
    print(data['windowTitle'])
    if not local:
        return url
    else:
        if port:
            return f"http://localhost:{port}/"
    return f"http://localhost:3000/"
    
def _exit():## Makes sure that it kills the node process when closes.
    if local:
    	killProcess(process)
    print("Exiting.")
def initNode(): ## Initiates the node process
    return subprocess.Popen([f"node {nodeFile}"], shell=True) ## Returns the process initated by the node file

def killProcess(p): ## Kills the node process
    subprocess.call(["kill", "-9", "%d" % int(p.pid+1)]) ## Node process
    subprocess.call(["kill", "-9", "%d" % int(p.pid)]) ## Bash process.

_url = getUrl()
window=webview.create_window(getJSON()['windowTitle'], _url) ## Creates a window navigating through the node website

if local: ## Check if it's a local node project or one in the web
    process=initNode() ## Stores the node process

try:
    webview.start() ## Starts the WebView
except ex:
    print(ex)

sys.exit(_exit())

