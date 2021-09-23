# IpBlockSubnet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_ip** | **str** | For internal system use Only. Represents start ip address of the subnet from IP block. Subnet ip adddress will start from this ip address. | [optional] 
**cidr** | **str** | Represents network address and the prefix length which will be associated with a layer-2 broadcast domain | [optional] 
**allocation_ranges** | [**list[IpPoolRange]**](IpPoolRange.md) | A collection of IPv4/IPv6 IP ranges used for IP allocation. | [optional] 
**block_id** | **str** | Block id for which the subnet is created. | 
**size** | **int** | Represents the size or number of ip addresses in the subnet | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

