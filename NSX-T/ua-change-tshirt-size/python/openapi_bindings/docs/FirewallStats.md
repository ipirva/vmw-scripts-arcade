# FirewallStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_session_count** | **int** | Aggregated number of sessions processed by the all firewall rules. This is aggregated statistic which are computed with lower frequency compared to individual generic rule statistics. It may have a computation delay up to 15 minutes in response to this API. | [optional] 
**packet_count** | **int** | Aggregated number of packets processed by the rule. | [optional] 
**popularity_index** | **int** | This is calculated by sessions count divided by age of the rule. | [optional] 
**max_session_count** | **int** | Maximum value of sessions count of all firewall rules of the type. This is aggregated statistic which are computed with lower frequency compared to generic rule statistics. It may have a computation delay up to 15 minutes in response to this API. | [optional] 
**byte_count** | **int** | Aggregated number of bytes processed by the rule. | [optional] 
**max_popularity_index** | **int** | Maximum value of popularity index of all firewall rules of the type. This is aggregated statistic which are computed with lower frequency compared to individual generic rule statistics. It may have a computation delay up to 15 minutes in response to this API. | [optional] 
**hit_count** | **int** | Aggregated number of hits received by the rule. | [optional] 
**session_count** | **int** | Aggregated number of sessions processed by the rule. | [optional] 
**rule_id** | **str** | Rule Identifier of the Firewall rule. This is a globally unique number. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

