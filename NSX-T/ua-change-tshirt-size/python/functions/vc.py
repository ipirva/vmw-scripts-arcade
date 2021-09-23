#!/usr/bin/env python3
'''
Ionut Pirva
September 2021
'''

import os, subprocess
from pprint import pprint

def f_check_vc_reachability(vcIP: str = None, vcUser: str = None, vcPass: str = None):
	'''
		Check if we can connect to vCenter
		API  https://{api_host}/api/vcenter/cluster/{cluster}
	'''

	cmdVCAuthSessionID = (
		f"curl -w '\n' --connect-timeout 5 --retry 3 --retry-delay 1 --silent -k -o /dev/null -u \"{vcUser}:{vcPass}\" -X POST "
		f"-c /tmp/vc-auth-cookie.txt https://{vcIP}/rest/com/vmware/cis/session"
		)
	cmdGetVCCluster = (
		f"curl -w '\n' -X GET --connect-timeout 5 --retry 3 --retry-delay 1 -s -i -k -b /tmp/vc-auth-cookie.txt "
		f"https://{vcIP}/rest/vcenter/cluster 2>&1"
	)

	command = (
		f"echo Obtain VC API Auth session ID. && "
		f"{cmdVCAuthSessionID} && "
		f"echo Get VC Clusters && "
		f"{cmdGetVCCluster}"
		)

	try:
		cmdRun = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	except Exception as e:
		print(f"ERROR {str(e)} while running {command}")
		return None
	while True:
		cmdStdOutErr = cmdRun.stdout.readline()
		if cmdRun.poll() is not None:
			break
		if cmdStdOutErr:
			print(cmdStdOutErr.strip().decode())

	output = cmdRun.poll()
	outputReturnCode = cmdRun.returncode
	if outputReturnCode != 0:
		print(f"ERROR while running init command: {command}")
	else:
		print(f"SUCCESS while running init command: {command}")

	return output
