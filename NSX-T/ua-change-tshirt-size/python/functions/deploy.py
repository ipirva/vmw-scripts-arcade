#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
'''

import subprocess, sys, os, shutil, sysconfig
from pprint import pprint
from python.functions.variables import f_check_env_variables

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

def f_terraform_destroy_vms() -> str:
    '''
        terraform destroy
        do not allow the destroy command to run if any of the NEW NSX Manager VMs is in the NSX Manager Cluster!
        the function stores the stdout and std error and returns it
    '''

    terraformDir = f_check_env_variables(var = ["terraformDir"])["terraformDir"]

    if not os.path.exists(terraformDir):
        print(f"ERROR Dir {terraformDir} does not exist.")
        return None

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