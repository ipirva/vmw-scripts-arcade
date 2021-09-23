# SystemHealthPluginProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_types** | **list[str]** | Display the running node types of pre-defined plugin. The config can be changed by API /systemhealth/profiles. To see the effective status on given node, use the status API per node /systemhealth/plugins/status/&lt;node-id&gt;.  | [optional] 
**publisher** | **str** | The publisher of System Health Agent plugin | [optional] 
**config** | [**SHAPredefinedPluginProfileData**](SHAPredefinedPluginProfileData.md) |  | [optional] 
**enabled** | **bool** | Display the default on-off switch of pre defined plugin. The config can be changed by API /systemhealth/profiles. To see the effective status on given node, use the status API per node /systemhealth/plugins/status/&lt;node-id&gt;.  | [optional] 
**type** | **str** | The type of System Health Agent plugin | [optional] [default to 'NETWORK']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

