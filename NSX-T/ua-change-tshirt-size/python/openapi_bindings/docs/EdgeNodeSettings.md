# EdgeNodeSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_domains** | **list[str]** | List of domain names that are used to complete unqualified host names.  | [optional] 
**dns_servers** | **list[str]** | List of DNS servers.  | [optional] 
**syslog_servers** | [**list[SyslogConfiguration]**](SyslogConfiguration.md) | List of Syslog server configuration.  | [optional] 
**ntp_servers** | **list[str]** | List of NTP servers.  | [optional] 
**hostname** | **str** | Host name or FQDN for edge node. | [optional] 
**enable_ssh** | **bool** | Enabling SSH service is not recommended for security reasons.  | [optional] [default to False]
**allow_ssh_root_login** | **bool** | Allowing root SSH logins is not recommended for security reasons. Edit of this property is not supported when updating transport node. Use the CLI to change this property.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

