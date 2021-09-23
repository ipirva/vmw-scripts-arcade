# IpfixDfwTemplateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_icmp_type** | **bool** | Type of the IPv4 ICMP message.  | [optional] [default to True]
**icmp_code** | **bool** | Code of the IPv4 ICMP message.  | [optional] [default to True]
**destination_transport_port** | **bool** | The destination transport port of a monitored network flow.  | [optional] [default to True]
**octet_delta_count** | **bool** | The number of octets since the previous report (if any) in incoming packets for this flow at the observation point. The number of octets include IP header(s) and payload.  | [optional] [default to True]
**vif_uuid** | **bool** | VIF UUID - enterprise specific Information Element that uniquely identifies VIF.  | [optional] [default to True]
**protocol_identifier** | **bool** | The value of the protocol number in the IP packet header.  | [optional] [default to True]
**firewall_event** | **bool** | Five valid values are allowed: 1. Flow Created. 2. Flow Deleted. 3. Flow Denied. 4. Flow Alert (not used in DropKick implementation). 5. Flow Update.  | [optional] [default to True]
**flow_direction** | **bool** | Two valid values are allowed: 1. 0x00: igress flow to VM. 2. 0x01: egress flow from VM.  | [optional] [default to True]
**flow_end** | **bool** | The absolute timestamp (seconds) of the last packet of this flow.  | [optional] [default to True]
**source_transport_port** | **bool** | The source transport port of a monitored network flow.  | [optional] [default to True]
**packet_delta_count** | **bool** | The number of incoming packets since the previous report (if any) for this flow at the observation point.  | [optional] [default to True]
**destination_address** | **bool** | The destination IP address of a monitored network flow.  | [optional] [default to True]
**source_address** | **bool** | The source IP address of a monitored network flow.  | [optional] [default to True]
**rule_id** | **bool** | Firewall rule Id - enterprise specific Information Element that uniquely identifies firewall rule.  | [optional] [default to True]
**flow_start** | **bool** | The absolute timestamp (seconds) of the first packet of this flow.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

