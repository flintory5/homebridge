import subprocess

def installNode(path):
	subprocess.call(["cd " + path], shell=True)
	subprocess.call(["sudo npm install -g homebridge"], shell=True)
	
def installPlugin(pluginName):
	subprocess.call(["sudo npm install -g " + pluginName], shell=True)
	
def installConfigFile(configFilePath):
	subprocess.call(["sudo cp -X " + configFilePath + " ~/.homebridge"], shell=True)
	
def installISYDeviceTypes(isyDeviceTypesFilePath):
	subprocess.call(["sudo cp -X " + isyDeviceTypesFilePath + " /usr/local/lib/node_modules/homebridge-isy-js/node_modules/isy-js"], shell=True)

homebridgeInstallPath = "/Users/flintory"

installNode(homebridgeInstallPath)
installConfigFile(homebridgeInstallPath + "/homebridge/config.json")
installPlugin("homebridge-http")
installPlugin("homebridge-isy-js")
installPlugin("homebridge-nest")
installPlugin("homebridge-legacy-plugins")
installISYDeviceTypes(homebridgeInstallPath + "/homebridge/isydevicetypes.json")