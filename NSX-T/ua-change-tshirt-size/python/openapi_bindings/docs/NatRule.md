# NatRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_destination_network** | **str** | IP Address | CIDR | (null implies Any)  | [optional] 
**translated_network** | **str** | The translated address for the matched IP packet. For a SNAT, it can be a single ip address, an ip range, or a CIDR block. For a DNAT and a REFLEXIVE, it can be a single ip address or a CIDR block. Translated network is not supported for NO_SNAT or NO_DNAT.  | [optional] 
**rule_priority** | **int** | Ascending, valid range [0-2147483647]. If multiple rules have the same priority, evaluation sequence is undefined.  | [optional] [default to 1024]
**match_service** | [**NSServiceElement**](NSServiceElement.md) |  | [optional] 
**applied_tos** | [**list[ResourceReference]**](ResourceReference.md) | Holds the list of LogicalRouterPort Ids that a NAT rule can be applied to. The LogicalRouterPort used must belong to the same LogicalRouter for which the NAT Rule is created. As of now a NAT rule can only have a single LogicalRouterPort as applied_tos. When applied_tos is not set, the NAT rule is applied to all LogicalRouterPorts beloging to the LogicalRouter. | [optional] 
**enabled** | **bool** | Indicator to enable/disable the rule.  | [optional] [default to True]
**internal_rule_id** | **str** | Internal NAT rule uuid for debug used in Controller and backend. | [optional] 
**logging** | **bool** | Enable/disable the logging of rule.  | [optional] [default to False]
**translated_ports** | **str** | The translated port(s) for the mtached IP packet. It can be a single port or a port range. Please note, port translating is supported only for DNAT.  | [optional] 
**action** | **str** | Valid actions: SNAT, DNAT, NO_SNAT, NO_DNAT, REFLEXIVE, NAT64. All rules in a logical router are either stateless or stateful. Mix is not supported. SNAT and DNAT are stateful, can NOT be supported when the logical router is running at active-active HA mode; REFLEXIVE is stateless. NO_SNAT and NO_DNAT have no translated_fields, only match fields are supported.  | 
**firewall_match** | **str** | Indicate how firewall is applied to a traffic packet. Firewall can be bypassed, or be applied to external/internal address of NAT rule.  The firewall_match will take priority over nat_pass. If the firewall_match is not provided, the nat_pass will be picked up.  | [optional] 
**nat_pass** | **bool** | Default is true. If the nat_pass is set to true, the following firewall stage will be skipped. Please note, if action is NO_SNAT or NO_DNAT, then nat_pass must be set to true or omitted.  Nat_pass was deprecated with an alternative firewall_match. Please stop using nat_pass to specify whether firewall stage is skipped. if you want to skip, please set firewall_match to BYPASS. If you do not want to skip, please set the firewall_match to MATCH_EXTERNAL_ADDRESS or MATCH_INTERNAL_ADDRESS.  Please note, the firewall_match will take priority over the nat_pass. If both are provided, the nat_pass is ignored. If firewall_match is not provided while the nat_pass is specified, the nat_pass will still be picked up. In this case, if nat_pass is set to false, firewall rule will be applied on internall address of a packet, i.e. MATCH_INTERNAL_ADDRESS.  | [optional] [default to True]
**logical_router_id** | **str** | The logical router id which the nat rule runs on. | [optional] 
**match_source_network** | **str** | IP Address | CIDR | (null implies Any)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

