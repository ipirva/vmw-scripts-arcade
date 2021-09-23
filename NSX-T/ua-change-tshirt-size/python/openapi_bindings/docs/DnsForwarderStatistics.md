# DnsForwarderStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries_forwarded** | **int** | The total number of forwarded dns queries | [optional] 
**conditional_forwarder_statistics** | [**list[PerForwarderStatistics]**](PerForwarderStatistics.md) | The statistics of conditional forwarders | [optional] 
**default_forwarder_statistics** | [**PerForwarderStatistics**](PerForwarderStatistics.md) |  | [optional] 
**queries_answered_locally** | **int** | The totocal number of queries answered from local cache | [optional] 
**used_cache_statistics** | [**list[PerNodeUsedCacheStatistics]**](PerNodeUsedCacheStatistics.md) | The statistics of used cache | [optional] 
**configured_cache_size** | **int** | The configured cache size, in kb | [optional] 
**timestamp** | **int** | Time stamp of the current statistics, in ms | [optional] 
**error_message** | **str** | Error message, if available | [optional] 
**total_queries** | **int** | The total number of received dns queries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

