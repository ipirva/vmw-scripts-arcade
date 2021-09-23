# NatStatisticsPerLogicalRouter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_update_timestamp** | **int** | Timestamp when the data was last updated; unset if data source has never updated the data. | [optional] 
**per_transport_node_statistics** | [**list[NatStatisticsPerTransportNode]**](NatStatisticsPerTransportNode.md) | Detailed per node statistics | [optional] 
**statistics_across_all_nodes** | [**NatCounters**](NatCounters.md) |  | [optional] 
**logical_router_id** | **str** | Id for the logical router | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

