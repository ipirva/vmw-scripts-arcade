# HostNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovered_node_id** | **str** | Id of discovered node which was converted to create this node | [optional] 
**managed_by_server** | **str** | The id of the vCenter server managing the ESXi type HostNode | [optional] 
**host_credential** | [**HostNodeLoginCredential**](HostNodeLoginCredential.md) |  | [optional] 
**os_version** | **str** | Version of the hypervisor operating system | [optional] 
**os_type** | **str** | Hypervisor type, for example ESXi or RHEL KVM | 
**windows_install_location** | **str** | Specify an installation folder to install the NSX kernel modules for Windows Server. By default, it is C:\\Program Files\\VMware\\NSX\\. | [optional] 
**maintenance_mode_state** | **str** | Indicates host node&#x27;s maintenance mode state. The state is ENTERING when a task to put the host in maintenance-mode is in progress.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

