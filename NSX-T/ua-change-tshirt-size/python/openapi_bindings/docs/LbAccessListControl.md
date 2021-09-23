# LbAccessListControl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | ALLOW means connections matching grouping object IP list are allowed and requests not matching grouping object IP list are dropped. DROP means connections matching grouping object IP list are dropped and requests not matching grouping object IP list are allowed.  | 
**group_id** | **str** | The identifier of grouping object which defines the IP addresses or ranges to match the client IP.  | 
**enabled** | **bool** | The enabled flag indicates whether to enable access list control option. It is false by default.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

