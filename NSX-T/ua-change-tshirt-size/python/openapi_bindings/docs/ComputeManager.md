# ComputeManager

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**LoginCredential**](LoginCredential.md) |  | [optional] 
**set_as_oidc_provider** | **bool** | If the compute manager is VC and need to set set as OIDC provider for NSX then this flag should be set as true. This is specific to wcp feature, should be enabled when this feature is being used.  | [optional] [default to False]
**access_level_for_oidc** | **str** | Specifies the maximum access level allowed for calls from compute manager to NSX using the OIDC provider.  | [optional] [default to 'FULL']
**reverse_proxy_https_port** | **int** | Specifies https port of the reverse proxy to connect to compute manager. For e.g. In case of VC, this port can be retrieved from this config file /etc/vmware-rhttpproxy/config.xml.  | [optional] [default to 443]
**create_service_account** | **bool** | Enable this flag to create service account user on compute manager. This is required by features such as vSphere Lifecycle Manager for authentication with vAPIs from nsx.  | [optional] [default to False]
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Key-Value map of additional specific properties of compute manager | [optional] 
**origin_type** | **str** | Compute manager type like vCenter | 
**server** | **str** | IP address or hostname of compute manager | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

