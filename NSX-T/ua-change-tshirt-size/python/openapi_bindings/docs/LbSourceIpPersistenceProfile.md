# LbSourceIpPersistenceProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purge** | **str** | persistence purge setting | [optional] [default to 'FULL']
**ha_persistence_mirroring_enabled** | **bool** | Persistence entries are not synchronized to the HA peer by default.  | [optional] [default to False]
**timeout** | **int** | When all connections complete (reference count reaches 0), persistence entry timer is started with the expiration time.  | [optional] [default to 300]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

