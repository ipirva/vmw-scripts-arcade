# ControlClusteringConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**join_to_existing_cluster** | **bool** | Specifies whether or not the cluster node VM should try to join to the existing control cluster or initialize a new one. Only required in uncertainty case, i.e. when there are manually- deployed controllers that are registered but not connected to the cluster and no auto-deployed controllers are part of the cluster.  | [optional] 
**shared_secret** | **str** | Shared secret to be used when joining the cluster node VM to a control cluster or for initializing a new cluster with the VM. Must contain at least 4 unique characters and be at least 6 characters long.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

