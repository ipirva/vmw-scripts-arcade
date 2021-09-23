# SupportBundleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_file_server** | [**SupportBundleRemoteFileServer**](SupportBundleRemoteFileServer.md) |  | [optional] 
**nodes** | **list[str]** | List of cluster/fabric node UUIDs processed in specified order | 
**content_filters** | **list[str]** | Bundle should include content of specified type | [optional] 
**log_age_limit** | **int** | Include log files with modified times not past the age limit in days | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

