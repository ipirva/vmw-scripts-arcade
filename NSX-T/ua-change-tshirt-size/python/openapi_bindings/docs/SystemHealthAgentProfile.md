# SystemHealthAgentProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The on-off switch of System Health Agent | [optional] 
**plugin_id** | **str** | The id of System Health Agent plugin | 
**config** | **str** | The config content of System Health Agent | 
**type** | **str** | The type of System Health Agent. The System Health Agent plugin associated with given plugin id has already defined the profile type. So the backend can obtain the type by the plugin definition directly. Mark this field as optional. If need to check the type value by given plugin id, please call /systemhealth/plugins/&lt;plugin-id&gt;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

