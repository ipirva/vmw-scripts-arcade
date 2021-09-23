# ServicePathHop

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active_from_dp** | **bool** | Indicating whether the corresponding service VM is active or not per DP. | [optional] 
**is_active_from_mp** | **bool** | Indicating whether the corresponding service VM is active or not per MP. | [optional] 
**vif** | **str** | ID of the virtual network interface. | [optional] 
**mac_address** | **str** | MAC address of the virtual network interface. | [optional] 
**action** | **str** | Action that will be taken by the corresponding service VM of the hop. | [optional] 
**is_active_from_ccp** | **bool** | Indicating whether the corresponding service VM is active or not per CCP. | [optional] 
**in_maintenance_mode** | **bool** | Indicating the maintenance mode of the corresponding service VM. | [optional] 
**nsh_liveness_support** | **bool** | Indicating whether NSH liveness is supported or not by the corresponding service VM. | [optional] 
**can_decrement_si** | **bool** | Indicating whether service is configured to decrement SI field in NSH metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

