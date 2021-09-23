# JoinClusterParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username on the cluster node | [optional] 
**certficate_sha256_thumbprint** | **str** | SHA256 Thumbprint of the API certificate of the cluster node | 
**token** | **str** | Limited time OAuth token instead of the username/password | [optional] 
**cluster_id** | **str** | UUID of the cluster to join | 
**password** | **str** | Password of the user on the cluster node | [optional] 
**ip_address** | **str** | IP address of a node already part of the cluster to join | 
**port** | **int** | API port on the cluster node | [optional] [default to 443]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

