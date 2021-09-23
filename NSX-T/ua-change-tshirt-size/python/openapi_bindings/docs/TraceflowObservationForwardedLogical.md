# TraceflowObservationForwardedLogical

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_path_index** | **int** | The path index of the service insertion component | [optional] 
**component_id** | **str** | The id of the component that forwarded the traceflow packet. | [optional] 
**spoofguard_vlan_id** | **int** | This field specified the VLAN id a traceflow packet matched in the whitelist in spoofguard. | [optional] 
**resend_type** | **str** | ARP_UNKNOWN_FROM_CP - Unknown ARP query result emitted by control plane ND_NS_UNKNOWN_FROM_CP - Unknown neighbor solicitation query result emitted by control plane UNKNOWN - Unknown resend type | [optional] 
**lport_name** | **str** | The name of the logical port through which the traceflow packet was forwarded. | [optional] 
**acl_rule_id** | **int** | The id of the acl rule that was applied to forward the traceflow packet | [optional] 
**service_index** | **int** | The index of the service insertion component | [optional] 
**vni** | **int** | VNI for the logical network on which the traceflow packet was forwarded. | [optional] 
**dst_component_name** | **str** | The name of the destination component to which the traceflow packet was forwarded. | [optional] 
**nat_rule_id** | **int** | The ID of the NAT rule that was applied to forward the traceflow packet | [optional] 
**translated_src_ip** | **str** | The translated source IP address of VPN/NAT | [optional] 
**translated_dst_ip** | **str** | The translated destination IP address of VNP/NAT | [optional] 
**spoofguard_mac** | **str** | The source MAC address of form: \&quot;^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\&quot;. For example: 00:00:00:00:00:00.  | [optional] 
**dst_component_type** | **str** | The type of the destination component to which the traceflow packet was forwarded. | [optional] 
**lport_id** | **str** | The id of the logical port through which the traceflow packet was forwarded. | [optional] 
**dst_component_id** | **str** | The id of the destination component to which the traceflow packet was forwarded. | [optional] 
**spoofguard_ip** | **str** | This field specified the prefix IP address a traceflow packet matched in the whitelist in spoofguard. | [optional] 
**service_ttl** | **int** | The ttl of the service insertion component | [optional] 
**svc_nh_mac** | **str** | MAC address of nexthop for service insertion(SI) in service VM(SVM) where the traceflow packet was received.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

