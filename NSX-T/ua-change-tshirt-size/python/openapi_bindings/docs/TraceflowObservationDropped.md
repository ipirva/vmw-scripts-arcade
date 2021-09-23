# TraceflowObservationDropped

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nat_rule_id** | **int** | The ID of the NAT rule that was applied to forward the traceflow packet | [optional] 
**reason** | **str** | The reason traceflow packet was dropped | [optional] 
**lport_id** | **str** | The id of the logical port at which the traceflow packet was dropped | [optional] 
**lport_name** | **str** | The name of the logical port at which the traceflow packet was dropped | [optional] 
**acl_rule_id** | **int** | The id of the acl rule that was applied to drop the traceflow packet | [optional] 
**arp_fail_reason** | **str** | This field specifies the ARP fails reason ARP_TIMEOUT - ARP failure due to query control plane timeout ARP_CPFAIL - ARP failure due post ARP query message to control plane failure ARP_FROMCP - ARP failure due to deleting ARP entry from control plane ARP_PORTDESTROY - ARP failure due to port destruction ARP_TABLEDESTROY - ARP failure due to ARP table destruction ARP_NETDESTROY - ARP failure due to overlay network destruction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

