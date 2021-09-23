# DhcpV6InfoBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease_time** | **int** | Lease time, in seconds. | [optional] [default to 86400]
**sntp_servers** | **list[str]** | SNTP server ips. | [optional] 
**preferred_time** | **int** | Preferred time, in seconds. If this value is not provided, the value of lease_time*0.8 will be used.  | [optional] 
**dns_nameservers** | **list[str]** | Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.  | [optional] 
**domain_names** | **list[str]** | Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

