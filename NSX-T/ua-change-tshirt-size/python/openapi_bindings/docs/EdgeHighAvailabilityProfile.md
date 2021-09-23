# EdgeHighAvailabilityProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standby_relocation_config** | [**StandbyRelocationConfig**](StandbyRelocationConfig.md) |  | [optional] 
**bfd_declare_dead_multiple** | **int** | Number of times a packet is missed before BFD declares the neighbor down. | [optional] [default to 3]
**bfd_probe_interval** | **int** | the time interval (in millisec) between probe packets for heartbeat purpose | [optional] [default to 500]
**bfd_allowed_hops** | **int** | BFD allowed hops | [optional] [default to 255]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

