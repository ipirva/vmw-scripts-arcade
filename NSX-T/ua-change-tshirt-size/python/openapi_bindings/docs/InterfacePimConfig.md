# InterfacePimConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hold_interval** | **int** | PIM hold interval. Ranges from 1 to 630 seconds. hold_interval should be greater than hello_interval. If hold interval is not provided then it will be considered as 3.5 times of hello_interval.  | [optional] 
**enabled** | **bool** | If the flag is set to true - it will enable PIM on the uplink interface. If the flag is set to false - it will disable PIM on the uplink interface.  | [optional] [default to False]
**hello_interval** | **int** | PIM hello interval. Ranges from 1 to 180 seconds.  | [optional] [default to 30]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

