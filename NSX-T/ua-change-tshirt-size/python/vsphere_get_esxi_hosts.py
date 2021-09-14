#!/usr/bin/env python3

'''
Ionut Pirva september 2021
The script connects to a vCenter server and gets all the esxi hosts and their respective hosts ids.
The script selects the CONNECTED and POWERED_ON esxi hosts for a specific vsphere DC and Cluster.

The output is a Terraform map variable type in an .auto.tfvars file.
The variable will be saved to file terraform/vsphere_esxi_hosts.auto.tfvars
'''

import sys, os
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

terraform_auto_var_file = "terraform/vsphere_esxi_hosts.auto.tfvars"
terraform_auto_var_file_folder = os.path.dirname(terraform_auto_var_file)
if os.path.exists(terraform_auto_var_file_folder) == False:
    raise SystemExit("The folder: "+terraform_auto_var_file_folder+" does not exist.")

s=requests.Session()
s.verify=False

# load vsphere login
try:
    vsphere_server_username=os.environ['TF_VAR_vsphere_server_username']
    vsphere_server_pawwsord=os.environ['TF_VAR_vsphere_server_password']
    vsphere_server=os.environ['TF_VAR_vsphere_server']
except Exception as e:
    sys.exit("Needed ENV variables not defined: "+str(e))

vsphere_auth_url="https://"+vsphere_server+"/rest/com/vmware/cis/session"
vsphere_api_get_host="https://"+vsphere_server+"/rest/vcenter/host"

def get_vcenter_session(vsphere_server: str, vsphere_server_username: str, vsphere_server_pawwsord: str) -> None:
    '''
    Create REST session auth
    '''
    s.post(vsphere_auth_url,auth=(vsphere_server_username,vsphere_server_pawwsord))
    return s

def get_vcenter_hosts(vsphere_server: str) -> None:
    '''
    Returns vcenter hosts CONNECTED and POWERED_ON 
    Terraform map format 
    vsphere_esxi_hosts={
        "esx01.cpod-go.az-fkd.cloud-garage.net": "host-16",
        "esx02.cpod-go.az-fkd.cloud-garage.net": "host-20"
    }
    '''
    try:
        vcenter_hosts=s.get(vsphere_api_get_host)
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e)
    # [{'host': 'host-16', 'name': 'esx01.cpod-go.az-fkd.cloud-garage.net', 'connection_state': 'CONNECTED', 'power_state': 'POWERED_ON'}, ]
    vcenter_hosts_list=json.loads(vcenter_hosts.text)["value"]

    vcenter_hosts=dict()

    for item in vcenter_hosts_list:
        if item["connection_state"] != "CONNECTED" or item["power_state"] != "POWERED_ON":
            vcenter_hosts_list.remove(item)
        else:
            vcenter_hosts[item["name"]]=item["host"]
    
    if len(vcenter_hosts) == 0:
        vcenter_hosts={}
    return "vsphere_esxi_hosts="+json.dumps(vcenter_hosts, indent=2).replace(', ','\n')


get_vcenter_session(vsphere_server, vsphere_server_username, vsphere_server_pawwsord)
vcenter_hosts=get_vcenter_hosts(vsphere_server)

# writes the Terraform vsphere_esxi_hosts map to Terraform .auto.tfvars file which is read automatically by Terraform
with open(terraform_auto_var_file, "w") as terraformvarfile:
    terraformvarfile.write(vcenter_hosts)
