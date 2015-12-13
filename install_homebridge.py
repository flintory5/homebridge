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

homebridgeInstallPath = raw_input("What's the path where you want to install homebridge?")
homebridgeHomePath = homebridgeInstallPath + "/homebridge"
print(homebridgeInstallPath)
print(homebridgeHomePath)


installNode(homebridgeInstallPath)
installConfigFile(homebridgeHomePath + "/config.json")
installPlugin("homebridge-http")
installPlugin("homebridge-isy-js")
installPlugin("homebridge-nest")
installPlugin("homebridge-legacy-plugins")
installISYDeviceTypes(homebridgeHomePath + "/isydevicetypes.json")

print "All Done!!"