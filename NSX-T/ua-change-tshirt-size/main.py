#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
workflow manager in python
'''
import argparse, os, sys, subprocess
from pprint import pprint

from python.functions.nsx import f_check_nsx_cluster_status
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
            envFile.write(f"pythonDir={myDir}/python\n")
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
    parser.add_argument("--action", default=None, type=str, choices=["Python_INIT", "Terraform_INIT", "CHECK", "PLAN_NEW_NSX_VM", "DEPLOY_NEW_NSX_VM", "DESTROY_NEW_NSX_VM", "REPLACE_NSX_CLUSTER"], help='''\
        Python_INIT: Downloads the NSX OpenAPI schema from the existing NSX cluster; Generates NSX API Python bindings. No changes are made on the infrastructure!
        Terraform_INIT: "terraform init". No changes are made on the infrastructure!
        CHECK: Checks VC connectivity and authentication; Checks the NSX Manager cluster status. No changes are made on the infrastructure!
        PLAN_NEW_NSX_VM: Plans the new NSX Manager VM(s) deployment. The planning is done using Terraform (plan), run Terraform_INIT before. No changes are made on the infrastructure!
        DEPLOY_NEW_NSX_VM: Deploys the new NSX Manager VM(s). The deployment is done using Terraform (apply), run Terraform_INIT before. Changes are made on the infrastructure!
        DESTROY_NEW_NSX_VM: Destroys the newly created NSX Manager VM(s). The action is done using Terraform (destroy), run Terraform_INIT before. The action is not available after a successful REPLACE_NSX_CLUSTER action. Changes are made on the infrastructure!
        REPLACE_NSX_CLUSTER: Replaces the VMs of the current NSX Manager cluster with the newly deployed NSX Manager VM(s). The old NSX Manager VMs are taken out of the NSX Manager cluster and shut down. Changes are made on the infrastructure!
    ''')
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    nsxClusterIP = f_check_env_variables(var = ["TF_VAR_nsxt_manager"])["TF_VAR_nsxt_manager"]
    nsxClusterUser = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_admin_username"])["TF_VAR_nsxt_manager_vm_admin_username"]
    nsxClusterPass = f_check_env_variables(var = ["TF_VAR_nsxt_manager_vm_admin_password"])["TF_VAR_nsxt_manager_vm_admin_password"]
    vcIP = f_check_env_variables(var = ["TF_VAR_vsphere_server"])["TF_VAR_vsphere_server"]
    vcUser = f_check_env_variables(var = ["TF_VAR_vsphere_server_username"])["TF_VAR_vsphere_server_username"]
    vcPass = f_check_env_variables(var = ["TF_VAR_vsphere_server_password"])["TF_VAR_vsphere_server_password"]
    vcCluster = f_check_env_variables(var = ["TF_VAR_vsphere_compute_cluster"])["TF_VAR_vsphere_compute_cluster"]
    
    # functions/init.py
    if args.action == "Python_INIT":
        print(f_python_init(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
    if args.action == "Terraform_INIT":
        print(f_terraform_init())

    # requires Python_INIT
    if args.action == "CHECK":
        print("Check NSX\n")
        # functions/nsx.py
        print(f_check_nsx_cluster_status(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass))
        print("Check vCenter\n")
        # functions/vc.py
        print(f_check_vc_reachability(vcIP = vcIP, vcUser = vcUser, vcPass = vcPass))

    # functions/deploy.py
    # requires Terraform_INIT
    if args.action == "PLAN_NEW_NSX_VM":
        print(f_terraform_plan_vms())

    # functions/deploy.py
    # requires Terraform_INIT
    if args.action == "DEPLOY_NEW_NSX_VM":
        print(f_terraform_apply_vms())
    
    # functions/deploy.py
    # requires Terraform_INIT
    if args.action == "DESTROY_NEW_NSX_VM":
        print(f_terraform_destroy_vms())

    # functions/replace.py
    # requires Python_INIT
    if args.action == "REPLACE_NSX_CLUSTER":
        print(args.action)