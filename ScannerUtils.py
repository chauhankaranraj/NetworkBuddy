import os
import re


def getMacAddresses():
	"""
	Runs the script that scans the local network and gets the mac addresses of connected devices

	:return: macAddresses: list of mac addresses of all devices currently connected to network
	"""

	os.system('chmod +x scan_script.sh')  # give required permissions
	os.system('sudo ./scan_script.sh')  # run the script which scans the network and saves results in scan_results.txt

	macAddresses = []

	# open the results file and see if we have any mac addresses; if we do then add them to the list
	with open('scan_results.txt', 'r') as outputFile:
		for line in outputFile:
			if (line[0:3] == "MAC"):
				# re to strip off irrelevant stuff and get the actual mac address
				macAddresses.append(line.split()[2] + " " + re.search(r'\((.*?)\)', line).group(1))

	return macAddresses