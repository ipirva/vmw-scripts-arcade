# IPv6DhcpServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_server_ip** | **str** | DHCP server ip in CIDR format. | [optional] 
**server_id** | **str** | DHCP server id. | [optional] 
**dns_nameservers** | **list[str]** | Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.  | [optional] 
**sntp_servers** | **list[str]** | SNTP server ips. | [optional] 
**domain_names** | **list[str]** | Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

