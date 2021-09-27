#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
workflow manager in python
'''
import argparse, os, sys, subprocess
from pprint import pprint

from python.functions.nsx import f_check_nsx_cluster_status, f_check_nsx_backup_status, f_do_nsx_backup, f_add_vm_nsx_cluster, f_remove_vm_nsx_cluster
from python.functions.vc import f_check_vc_reachability
from python.functions.variables import f_check_env_variables
from python.functions.init import f_terraform_init, f_python_init
from python.functions.deploy import f_terraform_plan_vms, f_terraform_apply_vms, f_terraform_destroy_vms

def f_create_env_file():
    '''
        Store extra env file
    '''
    # myDir may be /workspace
    myDir = os.path.dirname(os.path.realpath(__file__))
    pythonDir = f"{myDir}/python"

    try:
        # set extra env variables
        with open(f"{pythonDir}/.env", "w") as envFile:
            envFile.write(f"pythonDir={pythonDir}\n")
            envFile.write(f"terraformDir={myDir}/terraform\n")
            envFile.write(f"nsxOpenAPIBindingDir={pythonDir}/openapi_bindings\n")
    except Exception as e:
        return False
    
    return True

if __name__ == "__main__":
    
    # set extra env variables
    f_create_env_file()
    
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="""
    This script guides you through the available options of the NSX ua-change-tshirt-size recipe.
    """, usage='Use "%(prog)s --help" for more information', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--action", default=None, type=str, choices=["Python_INIT", "Terraform_INIT", "CHECK", "NSX_CLUSTER_STATUS", "PLAN_NEW_NSX_VM", "DEPLOY_NEW_NSX_VM", "DESTROY_NEW_NSX_VM", "ADD_NEW_NSX_VM_TO_CLUSTER", "REMOVE_NEW_NSX_VM_FROM_CLUSTER", "REMOVE_OLD_NSX_VM_FROM_CLUSTER"], help='''\
        Python_INIT: Downloads the NSX OpenAPI schema from the existing NSX cluster; Generates NSX API Python bindings. No changes are made on the infrastructure!
        Terraform_INIT: "terraform init". No changes are made on the infrastructure!
        CHECK: Checks VC connectivity and authentication; Checks the NSX Manager cluster status; Checks if NSX Backup is configured and healthy. No changes are made on the infrastructure!
        NSX_CLUSTER_STATUS: Shows NSX Manager Cluster status. No changes are made on the infrastructure!
        PLAN_NEW_NSX_VM: Plans the new NSX Manager VM(s) deployment. The planning is done using Terraform (plan), run Terraform_INIT before. No changes are made on the infrastructure!
        DEPLOY_NEW_NSX_VM: Deploys the new NSX Manager VM(s). The deployment is done using Terraform (apply), run Terraform_INIT before. Changes are made on the infrastructure!
        DESTROY_NEW_NSX_VM: Destroys the newly created NSX Manager VM(s). The action is done using Terraform (destroy), run Terraform_INIT before. The action is not available after a successful REPLACE_NSX_CLUSTER action. Changes are made on the infrastructure!
        ADD_NEW_NSX_VM_TO_CLUSTER: Backups the existing NSX Cluster. Adds the new NSX Manager VMs to cluster. Changes are made on the infrastructure!
        REMOVE_NEW_NSX_VM_FROM_CLUSTER: Removes the new NSX Manager VMs from cluster. Changes are made on the infrastructure!
        REMOVE_OLD_NSX_VM_FROM_CLUSTER: Removes the old NSX Manager VMs from cluster. Changes are made on the infrastructure!
    ''')
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    nsxClusterIP = f_check_env_variables(var = ["TF_VAR_nsxt_manager"])["TF_VAR_nsxt_manager"]
    nsxClusterUser = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_admin_username"])["TF_VAR_nsxt_manager_vm_admin_username"]
    nsxClusterPass = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_admin_password"])["TF_VAR_nsxt_manager_vm_admin_password"]
    vcIP = f_check_env_variables(var = ["TF_VAR_vsphere_server"])["TF_VAR_vsphere_server"]
    vcUser = f_check_env_variables(var = ["TF_VAR_vsphere_server_username"])["TF_VAR_vsphere_server_username"]
    vcPass = f_check_env_variables(var = ["TF_VAR_vsphere_server_password"])["TF_VAR_vsphere_server_password"]
    vcCluster = f_check_env_variables(var = ["TF_VAR_vsphere_compute_cluster"])["TF_VAR_vsphere_compute_cluster"]

    # [(nsxNewVMIPv4, nswNewVMHostname)]
    nsxNewManagerVMs = list()

    try:        
        nsxManagerVMIPv4Raw = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_ipv4_prefix"])["TF_VAR_nsxt_manager_vm_ipv4_prefix"]
        nsxManagerVMHostnameRaw = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_hostname"])["TF_VAR_nsxt_manager_vm_hostname"]
        nsxManagerVMIPv4Raw = nsxManagerVMIPv4Raw.split(",")
        nsxManagerVMHostnameRaw = nsxManagerVMHostnameRaw.split(",")
        
        if len(nsxManagerVMIPv4Raw) == len(nsxManagerVMHostnameRaw):
            for i in nsxManagerVMIPv4Raw:
                nsxNewManagerVMs.append((i.split("/")[0].strip(), nsxManagerVMHostnameRaw[nsxManagerVMIPv4Raw.index(i)].strip()))
    except Exception as e:
        print(f"ERROR cannot obtain the IPv4 of the new NSX Manager VMs. Make sure you have specify their IPv4 addresses and hostnames: {str(e)}")
    else:
        print(f"New NSX Manager VMs are: {str(nsxNewManagerVMs)}")

    # [(nsxKeepVMIPv4, nswKeepVMHostname)]
    nsxKeepManagerVMs = list()

    try:
        nsxClusterVMIPv4KeepRaw = f_check_env_variables(var = ["TF_VAR_nsxt_manager_keep_vm_ipv4"])["TF_VAR_nsxt_manager_keep_vm_ipv4"]
        nsxClusterVMIPv4KeepRaw = nsxClusterVMIPv4KeepRaw.split(",")
        for i in nsxClusterVMIPv4KeepRaw:
            nsxKeepManagerVMs.append((i.split("/")[0].strip(), ""))
    except Exception as e:
        print(f"ERROR cannot obtain the IPv4 of the NSX Manager VMs to keep. Make sure you have specify their IPv4 addresses or leave it empty if none mus be kept: {str(e)}")
    else:
        print(f"The NSX Manager VMs to keep in the cluster are: {str(nsxKeepManagerVMs)}")

    # functions/init.py
    if args.action == "Python_INIT":
        print("Working ...\n")
        print(f_python_init(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
    if args.action == "Terraform_INIT":
        print("Working ...\n")
        print(f_terraform_init())

    # requires Python_INIT
    if args.action == "CHECK":
        print("Working ...\n")
        # functions/nsx.py
        pprint(f_check_nsx_cluster_status(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
        # functions/nsx.py
        pprint(f_check_nsx_backup_status(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
        # functions/vc.py
        print(f_check_vc_reachability(vcIP = vcIP, vcUser = vcUser, vcPass = vcPass))

    # requires Python_INIT
    if args.action == "NSX_CLUSTER_STATUS":
        print("Working ...\n")
        # functions/nsx.py
        pprint(f_check_nsx_cluster_status(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))

    # functions/deploy.py
    # requires Terraform_INIT
    if args.action == "PLAN_NEW_NSX_VM":
        print("Working ...\n")
        print("Terraform plan\n")
        print(f_terraform_plan_vms())

    # functions/deploy.py
    # requires Terraform_INIT
    if args.action == "DEPLOY_NEW_NSX_VM":
        print("Working ...\n")
        print("Terraform apply\n")
        print(f_terraform_apply_vms())
    
    # functions/deploy.py
    # requires Terraform_INIT
    if args.action == "DESTROY_NEW_NSX_VM":
        print("Working ...\n")
        # check if the new NSX Manager VMs are in the cluster; they must not be
        # destroy the new NSX Manager VMs
        print("Terraform destroy\n")
        print(f_terraform_destroy_vms(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))

    # functions/nsx.py
    # requires Python_INIT
    if args.action == "ADD_NEW_NSX_VM_TO_CLUSTER":
        print("Working ...\n")
        # do a complete NSX backup
        # add the new NSX Manager VMs to the cluster and wait for the cluster global status to become STABLE
        print(f_do_nsx_backup(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
        
        if len(nsxNewManagerVMs) > 0:
            print(f"Add the following VMs to NSX Manager Cluster: {str(nsxNewManagerVMs)}")
            for i in nsxNewManagerVMs:
                nsxVMIPv4Val, nsxVMHostnameVal = i
                print(f"Add VM {str(i)} to NSX Manager Cluster ...")
                pprint(f_add_vm_nsx_cluster(nsxNewVMIP = nsxVMIPv4Val, nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
        else:
            print(f"ERROR cannot obtain the IPv4 of the new NSX Manager VMs. Make sure you have specify their IPv4 addresses and hostnames.")

    # functions/nsx.py
    # requires Python_INIT
    if args.action == "REMOVE_NEW_NSX_VM_FROM_CLUSTER":
        print("Working ...\n")
        # nsxNewManagerVMs = [("172.17.23.123", "nsx-t-a.test.io"), ]
        if len(nsxNewManagerVMs) > 0:
            print(f"Remove the following VMs from NSX Manager Cluster: {str(nsxNewManagerVMs)}")
            pprint(f_remove_vm_nsx_cluster(nsxVMIP = nsxNewManagerVMs, nsxNewVM = None, nsxKeepVM = None, nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
        else:
            print(f"ERROR cannot obtain the IPv4 of the NSX Manager VMs. Make sure you have specify their IPv4 addresses and hostnames.")

    # functions/nsx.py
    # requires Python_INIT
    if args.action == "REMOVE_OLD_NSX_VM_FROM_CLUSTER":
        print("Working ...\n")
        print(f_remove_vm_nsx_cluster(nsxVMIP = None, nsxNewVM = nsxNewManagerVMs, nsxKeepVM = nsxKeepManagerVMs, nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
