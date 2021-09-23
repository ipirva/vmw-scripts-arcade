# HaVipConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha_vip_subnets** | [**list[VIPSubnet]**](VIPSubnet.md) | Array of IP address subnets which will be used as floating IP addresses. | Note - this configuration is applicable only for Active-Standby LogicalRouter. | For Active-Active LogicalRouter this configuration will be rejected. | 
**redundant_uplink_port_ids** | **list[str]** | Identifiers of logical router uplink ports which are to be paired to provide | redundancy. Floating IP will be owned by one of these uplink ports (depending upon | which node is Active). | 
**enabled** | **bool** | Flag to enable this ha vip config. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

