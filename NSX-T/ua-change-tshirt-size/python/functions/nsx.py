#!/usr/bin/env python3
'''
Ionut Pirva  
September 2021
'''

import sys
from pprint import pprint

from python.functions.variables import f_check_env_variables

# add nsxOpenAPIBinding to the path where python will look for modules
nsxOpenAPIBindingDir = f_check_env_variables(var = ["nsxOpenAPIBindingDir"])["nsxOpenAPIBindingDir"]
sys.path.insert(0, nsxOpenAPIBindingDir)

import swagger_client.configuration
import swagger_client.rest
import swagger_client.api_client
from swagger_client.api.system_administration_configuration_nsx_managers_clusters_cluster_status_api import SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi

def f_check_nsx_cluster_status(nsxClusterIP: str = None, nsxClusterUser: str = None, nsxClusterPass: str = None) -> dict:
    '''
        Return NSX Manager cluster status
    '''

    # Configure HTTP basic authorization: BasicAuth
    configuration = swagger_client.Configuration()
    configuration.host = f"https://{nsxClusterIP}/api/v1"
    configuration.username = nsxClusterUser
    configuration.password = nsxClusterPass
    configuration.verify_ssl = False

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
        # nsx cluster control plane overall status
        nsxClusterControlStatus = nsxClusterStatusOutput.detailed_cluster_status.overall_status
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
                nsxClusterControlNodes["members"] = {}
                for el in nsxClusterControlGroups:
                    nsxClusterControlNodesMembers = el.members
                    for m in nsxClusterControlNodesMembers:
                        if m.member_uuid not in nsxClusterControlNodes["members"].keys():
                            nsxClusterControlNodes["members"][m.member_uuid] = {}
                            nsxClusterControlNodes["members"][m.member_uuid]["groups"] = list()
                            nsxClusterControlNodes["members"][m.member_uuid]["member_fqdn"] = m.member_fqdn
                            nsxClusterControlNodes["members"][m.member_uuid]["member_ip"] = m.member_ip
                        if el.group_type == "HTTPS" or el.group_type == "HTTP":
                            nsxClusterControlNodes["vip_node_uuid"] = el.leaders[0].leader_uuid
                        # if global status nsxClusterControlStatus is STABLE and any control node has services which are not STABLE
                        if el.group_status != nsxClusterControlStatus:
                            nsxClusterControlNodes["members"][m.member_uuid]["groups"].append({
                                "group_type": el.group_type,
                                "group_status": el.group_status
                                })
                        
            else: 
                nsxClusterControlNodes = None
        else:
            nsxClusterControlNodes = None
    
    except  Exception as e:
        print(f"ERROR NSX API GET cluster status processing failed: {str(e)}")
        return None
    else:
        output["cluster_id"] = nsxClusterID
        output["control_plane_status"] = nsxClusterControlStatus
        output["management_plane_status"] = nsxClusterMgmtStatus
        output["management_offline"] = nsxClusterMgmtOfflineNodes
        output["management_online"] = nsxClusterMgmtOnlineNodes
        output["control_plane_nodes"] = nsxClusterControlNodes
    
    return output









