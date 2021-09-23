# IpfixSwitchConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_timeout** | **int** | The time in seconds after a Flow is expired even if more packets matching this Flow are received by the cache.  | [optional] [default to 300]
**idle_timeout** | **int** | The time in seconds after a Flow is expired if no more packets matching this Flow are received by the cache.  | [optional] [default to 300]
**packet_sample_probability** | **float** | The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.  | [optional] 
**max_flows** | **int** | The maximum number of flow entries in each exporter flow cache.  | [optional] [default to 16384]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

