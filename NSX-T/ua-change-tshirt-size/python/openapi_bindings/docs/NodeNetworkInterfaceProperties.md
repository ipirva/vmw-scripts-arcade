# NodeNetworkInterfaceProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_address** | **str** | Interface MAC address | [optional] 
**broadcast_address** | **str** | Interface broadcast address | [optional] 
**link_status** | **str** | Interface administration status | [optional] 
**default_gateway** | **str** | Interface&#x27;s default gateway | [optional] 
**bond_primary** | **str** | Bond&#x27;s primary device name in active-backup bond mode | [optional] 
**bond_slaves** | **list[str]** | Bond&#x27;s slave devices | [optional] 
**ip_addresses** | [**list[IPv4AddressProperties]**](IPv4AddressProperties.md) | Interface IP addresses | [optional] 
**vlan** | **int** | VLAN Id | [optional] 
**bond_mode** | **str** | Bond mode | [optional] 
**interface_id** | **str** | Interface ID | [optional] 
**admin_status** | **str** | Interface administration status | [optional] 
**plane** | **str** | Interface plane | [optional] 
**is_kni** | **bool** | Interface is a KNI | [optional] 
**ip_configuration** | **str** | Interface configuration | 
**mtu** | **int** | Interface MTU | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

