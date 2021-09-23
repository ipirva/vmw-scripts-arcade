# ResourceAllocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation** | **float** | Minimum guaranteed bandwidth percentage | 
**traffic_type** | [**HostInfraTrafficType**](HostInfraTrafficType.md) |  | 
**limit** | **float** | The limit property specifies the maximum bandwidth allocation for a given traffic type and is expressed in percentage. The default value for this field is set to -1 which means the traffic is unbounded for the traffic type. All other negative values for this property is not supported and will be rejected by the API.  | 
**shares** | **int** | Shares | [default to 50]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

