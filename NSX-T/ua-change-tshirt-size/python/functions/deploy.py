#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
'''

import subprocess, sys, os, shutil, sysconfig
from pprint import pprint
from python.functions.variables import f_check_env_variables
from python.functions.nsx import f_check_nsx_cluster_status


def f_terraform_plan_vms() -> str:
    '''
        terraform plan
        the function stores the stdout and std error and returns it
    '''

    terraformDir = f_check_env_variables(var = ["terraformDir"])["terraformDir"]

    if not os.path.exists(terraformDir):
        print(f"ERROR Dir {terraformDir} does not exist.")
        return None

    cmdTerraformPLAN = "terraform plan -detailed-exitcode -no-color"
    command = f"echo chdir to {terraformDir} && cd {terraformDir} && echo Running the command: {cmdTerraformPLAN} && {cmdTerraformPLAN}"

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
        print(f"ERROR while running plan command: {command}")
    else:
        print(f"SUCCESS while running plan command: {command}")
    
    return output

def f_terraform_apply_vms() -> str:
    '''
        terraform apply
        the function stores the stdout and std error and returns it
    '''

    terraformDir = f_check_env_variables(var = ["terraformDir"])["terraformDir"]

    if not os.path.exists(terraformDir):
        print(f"ERROR Dir {terraformDir} does not exist.")
        return None

    cmdTerraformAPPLY = "terraform apply -no-color -auto-approve"
    command = f"echo chdir to {terraformDir} && cd {terraformDir} && echo Running the command: {cmdTerraformAPPLY} && {cmdTerraformAPPLY}"

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
        print(f"ERROR while running apply command: {command}")
    else:
        print(f"SUCCESS while running apply command: {command}")
    
    return output

def f_terraform_destroy_vms(nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> str:
    '''
        terraform destroy
        do not allow the destroy command to run if any of the NEW NSX Manager VMs is in the NSX Manager Cluster!
        the function stores the stdout and std error and returns it
    '''

    terraformDir = f_check_env_variables(var = ["terraformDir"])["terraformDir"]

    if not os.path.exists(terraformDir):
        print(f"ERROR Dir {terraformDir} does not exist.")
        return None

    # check if any of the new NSX Manager VM is in the NSX Manager cluster; must not be
    # NEW NSX Manager VM IPs and hostnames must be in the env vars
    # TF_VAR_nsxt_manager_vm_ipv4_prefix=172.17.23.123/24, 172.17.23.124/24, 172.17.23.125/24
    # TF_VAR_nsxt_manager_vm_hostname=nsx-t-a.cpod-go.az-fkd.cloud-garage.net,nsx-t-b.cpod-go.az-fkd.cloud-garage.net, nsx-t-c.cpod-go.az-fkd.cloud-garage.net
    nsxManagerVMIPv4Raw = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_ipv4_prefix"])["TF_VAR_nsxt_manager_vm_ipv4_prefix"]
    nsxManagerVMHostnameRaw = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_hostname"])["TF_VAR_nsxt_manager_vm_hostname"]
    
    # [("172.17.123", "nsx-t-a.cpod-go.az-fkd.cloud-garage.net")]
    nsxManagerVMs = list()
    try:
        nsxManagerVMIPv4Raw = nsxManagerVMIPv4Raw.split(",")
        nsxManagerVMHostnameRaw = nsxManagerVMHostnameRaw.split(",")

        if len(nsxManagerVMIPv4Raw) == len(nsxManagerVMHostnameRaw):
            for i in nsxManagerVMIPv4Raw:
                nsxManagerVMs.append((i.split("/")[0].strip(), nsxManagerVMHostnameRaw[nsxManagerVMIPv4Raw.index(i)].strip()))
        else:
            print(f"ERROR while reading new NSX Manager VM IPv4 and hostnames: there is no 1:1 mapping between {nsxManagerVMIPv4Raw} and {nsxManagerVMHostnameRaw}")
            return None
    except Exception as e:
        print(f"ERROR while handling new NSX Manager VM IPv4 and hostnames values: {str(e)}")
        return None

    nsxClusterStatus = f_check_nsx_cluster_status(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass)
    
    try:
        nsxClusterStatusControlMembers = nsxClusterStatus["control_plane_nodes"]["members"]
        nsxClusterStatusClusterID = nsxClusterStatus["cluster_id"]
    except Exception as e:
        print(f"ERROR while trying to get NSX Cluster members and Cluster ID: {str(e)}")
        return None
    else:
        for k, v in nsxClusterStatusControlMembers.items():
            memberHostname = v["member_fqdn"]
            memberIPv4 = v["member_ip"]
            lookForMember = (memberIPv4, memberHostname)
            if lookForMember in nsxManagerVMs:
                print(f"ERROR cannot destroy the newly created NSX Manager VMs. The NSX Manager VM {str(lookForMember)} is part of the NSX Manager Cluster ID {str(nsxClusterStatusClusterID)}")
                print(f"INFO NSX Manager Cluster {str(nsxClusterStatus)}")
                return None

    # at this point there is no new NSX Manager VM in the NSX Manager Cluster
    # it is safe to delete the VMs

    cmdTerraformDESTROY = "terraform destroy -no-color -auto-approve"
    command = f"echo chdir to {terraformDir} && cd {terraformDir} && echo Running the command: {cmdTerraformDESTROY} && {cmdTerraformDESTROY}"

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
        print(f"ERROR while running destroy command: {command}")
    else:
        print(f"SUCCESS while running destroy command: {command}")
    
    return output