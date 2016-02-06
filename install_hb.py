import subprocess

def installNode(path):
	subprocess.call(["cd " + path], shell=True)
	subprocess.call(["sudo npm install -g homebridge"], shell=True)
	
homebridgeInstallPath = "/home/flintory/"

print("***** Installing Homebridge ******")
installNode(homebridgeInstallPath)

print "All Done!!"