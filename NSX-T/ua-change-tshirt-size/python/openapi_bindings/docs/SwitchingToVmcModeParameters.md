# SwitchingToVmcModeParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sre_org** | [**OrgInfo**](OrgInfo.md) |  | [optional] 
**default_org_id** | **str** | Org ID of a Client - commonly UUID. | [optional] 
**ea_org** | [**OrgInfo**](OrgInfo.md) |  | [optional] 
**gss_org** | [**OrgInfo**](OrgInfo.md) |  | [optional] 
**proxy_host** | **str** | IP/host of PoP (Point-of-Presence) HTTP proxy server | [optional] 
**csp_time_drift** | **int** | CSP time drift in milliseconds | [optional] 
**sddc_id** | **str** | SDDC id | [optional] 
**basic_auth_whitelist_ips** | **list[str]** | List of whitelist IPs for basic auth | [optional] 
**base_url** | **str** | Protocol and domain name (or IP address) of a CSP server, like \&quot;https://console-stg.cloud.vmware.com\&quot;. | [optional] 
**proxy_port** | **int** | Port of PoP (Point-of-Presence) Http proxy server | [optional] 
**csp_org_uri** | **str** | Relative path on CSP server to the Org location. Can be \&quot;/csp/gateway/am/api/orgs/\&quot;. | [optional] 
**csp_client_credential** | [**Oauth2Credentials**](Oauth2Credentials.md) |  | [optional] 
**auth_code** | [**Oauth2Credentials**](Oauth2Credentials.md) |  | [optional] 
**mode_change_only** | **bool** | When this parameter is set to true, only a change of the node mode happens without any update to the auth properties. When this param is not set to true i.e. set to false or not provided, mode change and update to the auth properties will both happen. | [optional] 
**csp_client_incoming_credentials** | **list[str]** | List of incoming client IDs | [optional] 
**service_definition_id** | **str** | Service definition id | [optional] 
**resource_type** | **str** | Node Mode type | [optional] [default to 'SwitchingToVmcModeParameters']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

