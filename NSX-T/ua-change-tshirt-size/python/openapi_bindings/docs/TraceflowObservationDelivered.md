# TraceflowObservationDelivered

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_type** | **str** | This field specifies the resolution type of ARP ARP_SUPPRESSION_PORT_CACHE - ARP request is suppressed by port DB ARP_SUPPRESSION_TABLE - ARP request is suppressed by ARP table ARP_SUPPRESSION_CP_QUERY - ARP request is suppressed by info derived from CP ARP_VM - No suppression and the ARP request is resolved. | [optional] 
**lport_name** | **str** | The name of the logical port into which the traceflow packet was delivered | [optional] 
**target_mac** | **str** | The source MAC address of form: \&quot;^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\&quot;. For example: 00:00:00:00:00:00.  | [optional] 
**vlan_id** | **int** | VLAN on bridged network | [optional] 
**lport_id** | **str** | The id of the logical port into which the traceflow packet was delivered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

