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

print("***** Installing Homebridge ******")
installNode(homebridgeInstallPath)
print("***** Installing Homebridge Config File ******")
installConfigFile(homebridgeHomePath + "/config.json")
print("***** Installing Homebridge HTTP Plugin ******")
installPlugin("homebridge-http")
print("***** Installing Homebridge ISY Plugin ******")
installPlugin("homebridge-isy-js")
print("***** Installing Homebridge Nest Plugin ******")
installPlugin("homebridge-nest")
print("***** Installing Homebridge Legacy Plugins ******")
installPlugin("homebridge-legacy-plugins")
print("***** Installing ISY Device Types file ******")
installISYDeviceTypes(homebridgeHomePath + "/isydevicetypes.json")

#Add git upstream original master
print("***** Setting up git upstream master nfarina/homebridge ******")
subprocess.call(["git remote add upstream https://github.com/nfarina/homebridge"], shell=True)

print "All Done!!"