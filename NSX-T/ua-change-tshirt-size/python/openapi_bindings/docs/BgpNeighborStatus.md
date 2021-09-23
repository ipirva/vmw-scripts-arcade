# BgpNeighborStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_state** | **str** | Current state of the BGP session. | [optional] 
**messages_received** | **int** | Count of messages received from the neighbor | [optional] 
**keep_alive_interval** | **int** | Time in ms to wait for HELLO packet from BGP peer | [optional] 
**neighbor_router_id** | **str** | Router ID of the BGP neighbor. | [optional] 
**total_out_prefix_count** | **int** | Sum of out prefixes counts across all address families. | [optional] 
**lr_component_id** | **str** | Logical router component(Service Router/Distributed Router) id | [optional] 
**established_connection_count** | **int** | Count of connections established | [optional] 
**messages_sent** | **int** | Count of messages sent to the neighbor | [optional] 
**time_since_established** | **int** | Time(in seconds) since connection was established. | [optional] 
**hold_time** | **int** | Time in ms to wait for HELLO from BGP peer. If a HELLO packet is not seen from BGP Peer withing hold_time then BGP neighbor will be marked as down. | [optional] 
**graceful_restart** | **bool** | Current state of graceful restart where graceful_restart &#x3D; true indicates graceful restart is enabled and graceful_restart &#x3D; false indicates graceful restart is disabled. This is deprecated field, use graceful_restart_mode instead.  | [optional] 
**graceful_restart_mode** | **str** | Current state of graceful restart of BGP neighbor. Possible values are - 1. GR_AND_HELPER - Graceful restart with Helper 2. HELPER_ONLY - Helper only 3. DISABLE - Disabled  | [optional] 
**connection_drop_count** | **int** | Count of connection drop | [optional] 
**remote_port** | **int** | TCP port number of remote BGP Connection | [optional] 
**total_in_prefix_count** | **int** | Sum of in prefixes counts across all address families. | [optional] 
**remote_site** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**transport_node** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**local_port** | **int** | TCP port number of Local BGP connection | [optional] 
**remote_as_number** | **str** | AS number of the BGP neighbor | [optional] 
**announced_capabilities** | **list[str]** | BGP capabilities sent to BGP neighbor. | [optional] 
**negotiated_capability** | **list[str]** | BGP capabilities negotiated with BGP neighbor. | [optional] 
**address_families** | [**list[BgpAddressFamily]**](BgpAddressFamily.md) | Address families of BGP neighbor | [optional] 
**source_address** | **str** | The Ip address of logical port | [optional] 
**neighbor_address** | **str** | The IP of the BGP neighbor | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

