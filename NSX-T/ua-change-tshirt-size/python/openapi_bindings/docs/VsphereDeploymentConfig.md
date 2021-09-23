# VsphereDeploymentConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_network_ids** | **list[str]** | List of distributed portgroup or VLAN logical identifiers to which the datapath serving vnics of edge node vm will be connected.  | 
**resource_allocation** | [**ResourceAssignment**](ResourceAssignment.md) |  | [optional] 
**dns_servers** | **list[str]** | List of DNS servers. This field is deprecated. Use dns_servers property in EdgeNodeSettings section when creating or updating transport nodes.  | [optional] 
**compute_folder_id** | **str** | The edge node vm will be deployed on the specified compute folder created in a datacenter, if compute folder is specified. Note - User must ensure that compute folder is accessible by specified cluster/host.  | [optional] 
**search_domains** | **list[str]** | List of domain names that are used to complete unqualified host names. This field is deprecated. Use search_domains property in EdgeNodeSettings section when creating or updating transport nodes.  | [optional] 
**hostname** | **str** | Host name or FQDN for edge node. | [optional] 
**enable_ssh** | **bool** | Enabling SSH service is not recommended for security reasons. This field is deprecated. Use enable_ssh property in EdgeNodeSettings section when creating or updating transport nodes.  | [optional] [default to False]
**allow_ssh_root_login** | **bool** | Allowing root SSH logins is not recommended for security reasons. This field is deprecated. Use allow_ssh_root_login property in EdgeNodeSettings section when creating transport nodes.  | [optional] [default to False]
**compute_id** | **str** | The edge node vm will be deployed on the specified cluster or resourcepool. Note - all the hosts must have nsx fabric prepared in the specified cluster.  | 
**ntp_servers** | **list[str]** | List of NTP servers. This field is deprecated. Use ntp_servers property in EdgeNodeSettings section when creating or updating transport nodes.  | [optional] 
**reservation_info** | [**ReservationInfo**](ReservationInfo.md) |  | [optional] 
**vc_id** | **str** | The vc specific identifiers will be resolved on this VC. So all other identifiers specified here must belong to this vcenter server.  | 
**storage_id** | **str** | The edge node vm will be deployed on the specified datastore. User must ensure that storage is accessible by the specified cluster/host.  | 
**default_gateway_addresses** | **list[str]** | The default gateway for edge node must be specified if all the nodes it communicates with are not in the same subnet. Note: Only single IPv4 default gateway address is supported and it must belong to management network.  | [optional] 
**management_port_subnets** | [**list[IPSubnet]**](IPSubnet.md) | IP Address and subnet configuration for the management port. Note: only one IPv4 address is supported for the management port.  | [optional] 
**host_id** | **str** | The edge node vm will be deployed on the specified Host within the cluster if host_id is specified. Note - User must ensure that storage and specified networks are accessible by this host.  | [optional] 
**advanced_configuration** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties for advanced or cloud- specific deployments in key-value format.  | [optional] 
**management_network_id** | **str** | Distributed portgroup identifier to which the management vnic of edge node vm will be connected. This portgroup must have connectivity with MP and CCP. A VLAN logical switch identifier may also be specified.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

