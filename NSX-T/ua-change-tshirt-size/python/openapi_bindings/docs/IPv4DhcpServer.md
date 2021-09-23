# IPv4DhcpServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**DhcpOptions**](DhcpOptions.md) |  | [optional] 
**monitor_ippool_usage** | **bool** | Enable or disable monitoring of DHCP ip-pools usage. When enabled, system events are generated when pool usage exceeds the configured thresholds. System events can be viewed in REST API /api/v2/hpm/alarms  | [optional] [default to False]
**dhcp_server_ip** | **str** | DHCP server ip in CIDR format. | 
**dns_nameservers** | **list[str]** | Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.  | [optional] 
**domain_name** | **str** | Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.  | [optional] 
**gateway_ip** | **str** | Gateway ip to be assigned to host. It can be overridden by ip-pool or static-binding level property.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

