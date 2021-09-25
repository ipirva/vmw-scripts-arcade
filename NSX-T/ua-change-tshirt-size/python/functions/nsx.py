#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
'''

import sys, subprocess
from pprint import pprint

from python.functions.variables import f_check_env_variables

# add nsxOpenAPIBinding to the path where python will look for modules
nsxOpenAPIBindingDir = f_check_env_variables(var = ["nsxOpenAPIBindingDir"])["nsxOpenAPIBindingDir"]
sys.path.insert(0, nsxOpenAPIBindingDir)

def f_check_nsx_cluster_status(nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> dict:
    '''
        Return NSX Manager cluster status
    '''

    import swagger_client.configuration
    import swagger_client.rest
    import swagger_client.api_client
    from swagger_client.api.system_administration_configuration_nsx_managers_clusters_cluster_status_api import SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi

    # Configure HTTP basic authorization: BasicAuth
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{nsxClusterIP}/api/v1"
    configuration.username = nsxClusterUser
    configuration.password = nsxClusterPass
    configuration.verify_ssl = False

    print("Check NSX Manager cluster status: GET '/cluster/status'\n")
    # create an instance of the API class
    APIInstance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi(swagger_client.ApiClient(configuration))

    try:
        # GET '/cluster/status'
        nsxClusterStatus = APIInstance.read_cluster_status_with_http_info()
        nsxClusterStatusHTTPCode = nsxClusterStatus[1]
        nsxClusterStatusOutput = nsxClusterStatus[0]
    except Exception as e:
        print(f"ERROR while trying to GET NSX cluster status: {str(e)}")
        return None
    if nsxClusterStatusHTTPCode == 200:
        print(f"SUCCESS NSX API GET cluster status returned HTTP code: {str(nsxClusterStatusHTTPCode)}")
    else:
        print(f"ERROR NSX API GET cluster status returned HTTP code: {str(nsxClusterStatusHTTPCode)}")
        return None

    output = {}

    try:
        # nsx cluster id
        nsxClusterID = nsxClusterStatusOutput.cluster_id
        # nsx cluster control plane status
        nsxClusterControlStatus = nsxClusterStatusOutput.control_cluster_status.status
        # nsx cluster overall status
        nsxClusterOverallStatus = nsxClusterStatusOutput.detailed_cluster_status.overall_status
        # nsx cluster management status: offline and online nodes
        nsxClusterMgmtStatus = nsxClusterStatusOutput.mgmt_cluster_status.status
        if nsxClusterStatusOutput.mgmt_cluster_status.offline_nodes is None:
            # no mgmt plane offline for any nodes
            nsxClusterMgmtOfflineNodes = None
        else:
            nsxClusterMgmtOfflineNodes = list()
            for node in nsxClusterStatusOutput.mgmt_cluster_status.offline_nodes:
                nsxClusterMgmtOfflineNodes.append(node)
        if nsxClusterStatusOutput.mgmt_cluster_status.online_nodes is None:
            # no mgmt plane offline for any nodes
            nsxClusterMgmtOnlineNodes = None
        else:
            nsxClusterMgmtOnlineNodes = list()
            for node in nsxClusterStatusOutput.mgmt_cluster_status.online_nodes:
                nsxClusterMgmtOnlineNodes.append(node)
        # nsxClusterControlGroups is a list with all the control plane services, its memebers and status per member
        nsxClusterControlGroups = nsxClusterStatusOutput.detailed_cluster_status.groups
        if type(nsxClusterControlGroups) == list:
            if len(nsxClusterControlGroups) > 0:
                nsxClusterControlNodes = {}
                # which node uuid handles the cluster vip
                nsxClusterControlNodes["vip_node_uuid"] = None
                nsxClusterControlNodes["groups"] = {}
                nsxClusterControlNodes["members"] = set()
                # nsxClusterControlNodes["members"] = {}
                for el in nsxClusterControlGroups:
                    nsxClusterControlNodesMembers = el.members
                    # el.group_status
                    # el.group_type
                    # el.group_id
                    if el.group_type == "HTTPS" or el.group_type == "HTTP":
                        nsxClusterControlNodes["vip_node_uuid"] = el.leaders[0].leader_uuid
                    if el.group_id not in nsxClusterControlNodes["groups"].keys():
                        nsxClusterControlNodes["groups"][el.group_id] = {}
                        nsxClusterControlNodes["groups"][el.group_id]["group_status"] = el.group_status
                        nsxClusterControlNodes["groups"][el.group_id]["group_type"] = el.group_type
                        nsxClusterControlNodes["groups"][el.group_id]["members"] = list()
                    for m in nsxClusterControlNodesMembers:
                        nsxClusterControlNodes["groups"][el.group_id]["members"].append({
                            "member_fqdn": m.member_fqdn,
                            "member_ip": m.member_ip,
                            "member_status": m.member_status,
                            "member_uuid": m.member_uuid
                        })
                        if el.group_type != "CONTROLLER":
                            nsxClusterControlNodes["members"].add(
                                (m.member_ip, m.member_fqdn, m.member_uuid)
                            )
            else: 
                nsxClusterControlNodes = None
        else:
            nsxClusterControlNodes = None
    except  Exception as e:
        print(f"ERROR NSX API GET cluster status processing failed: {str(e)}")
        return None
    else:
        output["cluster_id"] = nsxClusterID
        output["overall_status"] = nsxClusterOverallStatus
        output["control_plane_status"] = nsxClusterControlStatus
        output["management_plane_status"] = nsxClusterMgmtStatus
        output["management_offline"] = nsxClusterMgmtOfflineNodes
        output["management_online"] = nsxClusterMgmtOnlineNodes
        output["control_plane_nodes"] = nsxClusterControlNodes

    return output

def f_check_nsx_backup_status(nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> dict:
    '''
        Return NSX backup status
    '''

    import swagger_client.configuration
    import swagger_client.rest
    import swagger_client.api_client
    from swagger_client.api.system_administration_lifecycle_management_backup_restore_management_backup_api import SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi

    # Configure HTTP basic authorization: BasicAuth
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{nsxClusterIP}/api/v1"
    configuration.username = nsxClusterUser
    configuration.password = nsxClusterPass
    configuration.verify_ssl = False

    print("Check NSX Backup status: GET '/backups/config'\n")
    # create an instance of the API class
    APIInstance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
    try:
        # GET '/backups/config'
        nsxBackupStatus = APIInstance.get_backup_config_with_http_info()
        nsxBackupStatusHTTPCode = nsxBackupStatus[1]
        nsxBackupStatusOutput = nsxBackupStatus[0]
    except Exception as e:
        print(f"ERROR while trying to GET NSX backup status: {str(e)}")
        return None
    else:
        print(nsxBackupStatusOutput)
    
    if nsxBackupStatusHTTPCode == 200:
        print(f"SUCCESS NSX API GET backup status returned HTTP code: {str(nsxBackupStatusHTTPCode)}")
    else:
        print(f"ERROR NSX API GET backup status returned HTTP code: {str(nsxBackupStatusHTTPCode)}")
        return None

    nsxBackupEnabled = None

    try:
        # nsx backup enabled True or False
        nsxBackupEnabled = nsxBackupStatusOutput.backup_enabled
    except  Exception as e:
        print(f"ERROR NSX API GET backup status processing failed: {str(e)}")
        return None
    else:
        print(f"SUCCESS NSX API GET backup status returned: {str(nsxBackupEnabled)}")
        if nsxBackupEnabled is True:
            print(f"SUCCESS NSX Cluster backup is enabled")
        if nsxBackupStatus is False:
            print(f"SUCCESS NSX Cluster backup is NOT enabled")

    return nsxBackupEnabled

def f_do_nsx_backup(nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> dict:
    '''
        Perform NSX backup
        cluster-node-backups
        inventory-summary
    '''

    import swagger_client.configuration
    import swagger_client.rest
    import swagger_client.api_client
    from swagger_client.api.system_administration_lifecycle_management_backup_restore_management_backup_api import SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi


    print(f"Checking NSX Cluster backup status ...")
    nsxBackupStatus = f_check_nsx_backup_status(nsxClusterIP = nsxClusterIP, nsxClusterUser = nsxClusterUser, nsxClusterPass = nsxClusterPass)
    if nsxBackupStatus is not True:
        print(f"ERROR to perform NSX backup: NSX Backup must be enabled.")
        return None
    
    # Configure HTTP basic authorization: BasicAuth
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{nsxClusterIP}/api/v1"
    configuration.username = nsxClusterUser
    configuration.password = nsxClusterPass
    configuration.verify_ssl = False
    
    # async_req=False
    print(f"Synchronous NSX backup ongoing ...\n")

    # create an instance of the API class
    APIInstance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
    try:
        # POST '/cluster?action=backup_to_remote'
        # do sync backup
        nsxDoBackup = APIInstance.request_onetime_backup_backup_to_remote_with_http_info(async_req=False)
    except Exception as e:
        print(f"ERROR while trying to GET NSX backup status: {str(e)}")
        return None

    return True


def f_add_vm_nsx_cluster(nsxNewVMIP: str = None, nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> dict:
    '''
        ADD NSX Manager VM to cluster
    '''

    import swagger_client.configuration
    import swagger_client.rest
    import swagger_client.api_client
    from swagger_client.api.system_administration_configuration_nsx_managers_clusters_cluster_configuration_api import SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi


    print(f"Checking NSX Cluster status ...")
    try:
        nsxClusterStatus = f_check_nsx_cluster_status(nsxClusterIP=nsxClusterIP, nsxClusterUser=nsxClusterUser, nsxClusterPass=nsxClusterPass)
        nsxClusterID = nsxClusterStatus["cluster_id"]
        nsxClusterStatusOverall = nsxClusterStatus["overall_status"]
        nsxClusterStatusCtrlGlobal = nsxClusterStatus["control_plane_status"]
        nsxClusterStatusMgmtGlobal = nsxClusterStatus["management_plane_status"]
        nsxClusterMembers = nsxClusterStatus["control_plane_nodes"]["members"]
    except Exception as e:
        print(f"ERROR while trying to GET NSX Cluster ID: {str(e)}")
        return None
    for item in nsxClusterMembers:
        if nsxNewVMIP in item:
            print(f"ERROR NSX Manager VM is already part of the NSX cluster ID {nsxClusterID}")
            pprint(nsxClusterStatus)
            return None

    # move forward only if the cluster status is STABLE
    if nsxClusterStatusOverall != "STABLE":
        print(f"ERROR NSX Manager cluster ID {nsxClusterID} overall status must be STABLE, and not {nsxClusterStatusOverall}")
        return None
    else:
        print(f"SUCCESS NSX Manager cluster ID {nsxClusterID} overall status is {nsxClusterStatusOverall}")

    # get certficate_sha256_thumbprint
    print(f"Get NSX Cluster {nsxClusterIP}:443 SSL SHA256 thumbprint ...")
    nsxClusterIPSHA256Thumbprint = None
    try:
        cmdGetSHA256Thumbprint = (
            f"openssl s_client -connect {nsxClusterIP}:443 < /dev/null 2>/dev/null | openssl x509 -fingerprint -sha256 -noout -in /dev/stdin "
            " | awk -F= '{gsub (\"[:]\",\"\"); printf $2}'"
        )
        cmdRunGetSHA256Thumbprint = subprocess.Popen(cmdGetSHA256Thumbprint, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmdRunGetSHA256ThumbprintStdOut, cmdRunGetSHA256ThumbprintStdErr = cmdRunGetSHA256Thumbprint.communicate()
    except Exception as e:
        print(f"ERROR cannot get SSL SHA256 thumbprint for {nsxClusterIP}:443: {str(e)}")
        return None
    else:
        if len(cmdRunGetSHA256ThumbprintStdErr.decode()) != 0:
            print(f"ERROR while reading the SSL SHA256 thumbprint for {nsxClusterIP}:443: {str(cmdRunGetSHA256ThumbprintStdErr.decode())}")
            return None
        else:
            print(f"SUCCESS the SSL SHA256 thumbprint for {nsxClusterIP}:443 is: {str(cmdRunGetSHA256ThumbprintStdOut.decode())}")
            nsxClusterIPSHA256Thumbprint =  cmdRunGetSHA256ThumbprintStdOut.decode()

    # Configure HTTP basic authorization: BasicAuth
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{nsxNewVMIP}/api/v1"
    configuration.username = nsxClusterUser
    configuration.password = nsxClusterPass
    configuration.verify_ssl = False

    # create an instance of the API class
    APIInstance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))

    reqBody = {
        "cluster_id": nsxClusterID, 
        "ip_address": nsxClusterIP, 
        "username": nsxClusterUser, 
        "password": nsxClusterPass, 
        "certficate_sha256_thumbprint": nsxClusterIPSHA256Thumbprint
        }
    
    # add new NSX Manager VM to cluster
    # synchronous action
    print(f"Adding NSX Manager VM {nsxNewVMIP} to NSX Manager {nsxClusterIP} cluster ID {nsxClusterID} ...")
    print(f"POST '/cluster?action=join_cluster'")
    print(f"{str(reqBody)}")
    try:
        # POST '/cluster?action=join_cluster'
        nsxVMJoinCluster = APIInstance.join_cluster_join_cluster_with_http_info(reqBody, async_req=False)
        nsxVMJoinClusterHTTPCode = nsxVMJoinCluster[1]
        nsxVMJoinClusterOutput = nsxVMJoinCluster[0]
    except Exception as e:
        print(f"ERROR while trying to add NSX Manager VM {nsxNewVMIP} to NSX Manager {nsxClusterIP} cluster ID {nsxClusterID}: {str(e)}")
        return None
    else:
        print(nsxVMJoinClusterOutput)
    
    if nsxVMJoinClusterHTTPCode == 200:
        print(f"SUCCESS NSX API POST add NSX Manager VM {nsxNewVMIP} to NSX Manager {nsxClusterIP} cluster ID {nsxClusterID} returned HTTP code: {str(nsxVMJoinClusterHTTPCode)}")
        newVMJoined = False
        for i in nsxVMJoinClusterOutput.nodes:
            if nsxNewVM in (i.entities[0].fqdn, i.entities[0].ip_address):
                if i.status == "JOINED":
                    print(f"SUCCESS NSX Manager VM {nsxNewVMIP} joined NSX Manager {nsxClusterIP} cluster ID {nsxClusterID}")
                    newVMJoined = True
        if newVMJoined is False:
            print(f"ERROR NSX Manager VM {nsxNewVMIP} did NOT join NSX Manager {nsxClusterIP} cluster ID {nsxClusterID}")
    else:
        print(f"ERROR NSX API POST add NSX Manager VM {nsxNewVMIP} to NSX Manager {nsxClusterIP} cluster ID {nsxClusterID} returned HTTP code: {str(nsxVMJoinClusterHTTPCode)}")
        return None
    
    # terminate loop after 5 minutes
    whileLoopTerminate = 5*60 # seconds
    whileLoopSleep = 10 # seconds
    whileLoopCounter = 0
    while True:
        print(f"INFO Waiting for the NSX cluster overall status to transition to STABLE ...")
        print(f"{str(whileLoopCounter)} seconds passed ...")

        try:
            nsxClusterStatus = f_check_nsx_cluster_status(nsxClusterIP=nsxClusterIP, nsxClusterUser=nsxClusterUser, nsxClusterPass=nsxClusterPass)
            nsxClusterID = nsxClusterStatus["cluster_id"]
            nsxClusterStatusCtrlGlobal = nsxClusterStatus["control_plane_status"]
            nsxClusterStatusMgmtGlobal = nsxClusterStatus["management_plane_status"]
        except Exception as e:
            print(f"ERROR while trying to GET NSX Cluster ID: {str(e)}")
            break

        # move forward only if the cluster status is STABLE
        if nsxClusterStatusOverall == "STABLE":
            print(f"SUCCESS NSX Manager cluster ID {nsxClusterID} overall status is {nsxClusterStatusOverall}")
            break
        else:
            print(f"INFO NSX Manager cluster ID {nsxClusterID} overall status is {nsxClusterStatusOverall}")
            # sleep
            time.sleep(whileLoopSleep)
        
        if whileLoopCounter >= whileLoopTerminate:
            print(f"ERROR Wait time of {str(whileLoopTerminate)} seconds expired.")
            break
        whileLoopCounter +=  whileLoopSleep

    return f_check_nsx_cluster_status(nsxClusterIP=nsxClusterIP, nsxClusterUser=nsxClusterUser, nsxClusterPass=nsxClusterPass)

def f_remove_vm_nsx_cluster(nsxVMIP: list = None, nsxNewVM: list = None, nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> dict:
    '''
        Remove NSX Manager VM from cluster
        nsxVMIP = [(IP, HOSTNAME), ]
        nsxVMIP = specific IP -> remove that specific NSX VM
            - this is done without checking that NSX Cluster overall status be STABLE
        nsxVMIP = None -> remove the old NSX Manager VMs and keep the newly deployed ones
            - this is done only if the NSX Cluster overall status is STABLE
    '''

    import swagger_client.configuration
    import swagger_client.rest
    import swagger_client.api_client
    from swagger_client.api.system_administration_configuration_nsx_managers_clusters_cluster_configuration_api import SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi

    print(f"Checking NSX Cluster status ...")
    try:
        nsxClusterStatus = f_check_nsx_cluster_status(nsxClusterIP=nsxClusterIP, nsxClusterUser=nsxClusterUser, nsxClusterPass=nsxClusterPass)
        nsxClusterID = nsxClusterStatus["cluster_id"]
        nsxClusterStatusOverall = nsxClusterStatus["overall_status"]
        nsxClusterStatusCtrlGlobal = nsxClusterStatus["control_plane_status"]
        nsxClusterStatusMgmtGlobal = nsxClusterStatus["management_plane_status"]
        nsxClusterMembers = nsxClusterStatus["control_plane_nodes"]["members"]
        nsxClusterMembersMgmtOnline = nsxClusterStatus["management_online"]
    except Exception as e:
        print(f"ERROR while trying to GET NSX Cluster ID: {str(e)}")
        return None

    nsxVMUUID2IP = dict()

    # remove the new NSX VMs
    if nsxVMIP is not None:
        nsxVMUUID2Remove = list()
        nsxNewVMIPList = set()
        try:
            for item in nsxVMIP:
                a, b = item
                nsxNewVMIPList.add(a)

            for item in nsxClusterMembers:
                nsxVMIPv4Val, nsxVMHostnameVal, nsxVMUUIDVal = item
                if nsxVMIPv4Val in nsxNewVMIPList:
                    nsxVMUUID2Remove.append(nsxVMUUIDVal)
                    nsxVMUUID2IP[nsxVMUUIDVal] = nsxVMIPv4Val

        except Exception as e:
            pprint(f"ERROR cannot determine node UUID for VM IP {str(nsxVMIP)} reading {nsxClusterMembers}: {str(e)}")
            return None
    
    # remove the old NSX VMs
    if nsxVMIP is None:
        nsxVMUUID2Remove = list()
        nsxNewVMIPList = set()
        # move forward only if the cluster status is STABLE
        if nsxClusterStatusOverall != "STABLE":
            print(f"ERROR NSX Manager cluster ID {nsxClusterID} overall status must be STABLE, and not {nsxClusterStatusOverall}")
            return None
        else:
            print(f"SUCCESS NSX Manager cluster ID {nsxClusterID} overall status is {nsxClusterStatusOverall}")

        try:
            for item in nsxNewVM:
                a, b = item
                nsxNewVMIPList.add(a)

            for item in nsxClusterMembers:
                nsxVMIPv4Val, nsxVMHostnameVal, nsxVMUUIDVal = item
                if nsxVMIPv4Val not in nsxNewVMIPList:
                    nsxVMUUID2Remove.append(nsxVMUUIDVal)
                    nsxVMUUID2IP[nsxVMUUIDVal] = nsxVMIPv4Val
        except Exception as e:
            pprint(f"ERROR cannot determine node UUID for the old NSX Manager VMs while reading {nsxClusterMembers}: {str(e)}")
            return None

    # Configure HTTP basic authorization: BasicAuth
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{nsxClusterIP}/api/v1"
    configuration.username = nsxClusterUser
    configuration.password = nsxClusterPass
    configuration.verify_ssl = False
    
    # create an instance of the API class
    APIInstance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
    
    # remove NSX Manager VM from cluster
    # synchronous action !!!
    for nsxVMUUID in nsxVMUUID2Remove:
        print(f"Removing synchronously (!) NSX Manager VM {nsxVMUUID2IP[nsxVMUUID]}, node uuid {nsxVMUUID} from NSX Manager {nsxClusterIP} cluster ID {nsxClusterID} ...")
        print(f"POST '/cluster/{nsxVMUUID}?action=remove_node'")
        try:
            # POST '/cluster/{node-id}?action=remove_node'
            nsxVMRemoveCluster = APIInstance.detach_cluster_node_remove_node_with_http_info(node_id=nsxVMUUID, async_req=False)
        except Exception as e:
            print(f"ERROR while trying to remove NSX Manager VM {nsxVMUUID2IP[nsxVMUUID]}, node uuid {nsxVMUUID} from NSX Manager {nsxClusterIP} cluster ID {nsxClusterID}: {str(e)}")
            return None
        else:
            print(nsxVMRemoveCluster)
            print(f"SUCCESS NSX API POST remove NSX Manager VM {nsxVMUUID2IP[nsxVMUUID]}, node uuid {nsxVMUUID} from NSX Manager {nsxClusterIP} cluster ID {nsxClusterID}")

    return True


