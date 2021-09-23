# IntelligenceVsphereClusterNodeVMDeploymentConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_url** | **str** | The NSX-Intelligence cluster node VM OVF URL to download and install the OVF file. This field is deprecated now. Please upload OVA file using \&quot;/repository/bundles\&quot; API and then try deployment without providing this field.  | [optional] 
**dns_servers** | **list[str]** | List of DNS servers. If DHCP is used, the default DNS servers associated with the DHCP server will be used instead. Required if using static IP.  | [optional] 
**display_name** | **str** | Desired display name for NSX-Intelligence VM to be deployed  | [optional] 
**ntp_servers** | **list[str]** | List of NTP servers. To use hostnames, a DNS server must be defined. If not using DHCP, a DNS server should be specified under dns_servers.  | [optional] 
**management_network_id** | **str** | Distributed portgroup identifier to which the management vnic of NSX-Intelligence cluster node VM will be connected.  | 
**enable_ssh** | **bool** | If true, the SSH service will automatically be started on the VM. Enabling SSH service is not recommended for security reasons.  | [optional] [default to False]
**allow_ssh_root_login** | **bool** | If true, the root user will be allowed to log into the VM. Allowing root SSH logins is not recommended for security reasons.  | [optional] [default to False]
**compute_id** | **str** | The NSX-Intelligence cluster node VM will be deployed on the specified cluster or resourcepool for specified VC server.  | 
**disk_provisioning** | **str** | Specifies the disk provisioning type of the VM.  | [optional] [default to 'THIN']
**vc_id** | **str** | The VC-specific identifiers will be resolved on this VC, so all other identifiers specified in the config must belong to this vCenter server.  | 
**storage_id** | **str** | The NSX-Intelligence cluster node VM will be deployed on the specified datastore in the specified VC server. User must ensure that storage is accessible by the specified cluster/host.  | 
**default_gateway_addresses** | **list[str]** | The default gateway for the VM to be deployed must be specified if all the other VMs it communicates with are not in the same subnet. Do not specify this field and management_port_subnets to use DHCP. Note: only single IPv4 default gateway address is supported and it must belong to management network. IMPORTANT: VMs deployed using DHCP are currently not supported, so this parameter should be specified.  | [optional] 
**management_port_subnets** | [**list[IPSubnet]**](IPSubnet.md) | IP Address and subnet configuration for the management port. Do not specify this field and default_gateway_addresses to use DHCP. Note: only one IPv4 address is supported for the management port. IMPORTANT: VMs deployed using DHCP are currently not supported, so this parameter should be specified.  | [optional] 
**host_id** | **str** | The NSX-Intelligence cluster node VM will be deployed on the specified host in the specified VC server within the cluster if host_id is specified. Note: User must ensure that storage and specified networks are accessible by this host.  | [optional] 
**hostname** | **str** | Desired host name/FQDN for the VM to be deployed  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

