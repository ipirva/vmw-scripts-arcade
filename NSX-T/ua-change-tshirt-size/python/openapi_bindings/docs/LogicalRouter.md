# LogicalRouter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_cluster_member_indices** | **list[int]** | For stateful services, the logical router should be associated with edge cluster. For TIER 1 logical router, for manual placement of service router within the cluster, edge cluster member indices needs to be provided else same will be auto-allocated. You can provide maximum two indices for HA ACTIVE_STANDBY. For TIER0 logical router this property is no use and placement is derived from logical router uplink or loopback port.  | [optional] 
**ipv6_profiles** | [**IPv6Profiles**](IPv6Profiles.md) |  | [optional] 
**allocation_profile** | [**EdgeClusterMemberAllocationProfile**](EdgeClusterMemberAllocationProfile.md) |  | [optional] 
**firewall_sections** | [**list[ResourceReference]**](ResourceReference.md) | List of Firewall sections related to Logical Router. | [optional] 
**failover_mode** | **str** | Determines the behavior when a logical router instance restarts after a failure. If set to PREEMPTIVE, the preferred node will take over, even if it causes another failure. If set to NON_PREEMPTIVE, then the instance that restarted will remain secondary. This property must not be populated unless the high_availability_mode property is set to ACTIVE_STANDBY. If high_availability_mode property is set to ACTIVE_STANDBY and this property is not specified then default will be NON_PREEMPTIVE.  | [optional] 
**advanced_config** | [**LogicalRouterConfig**](LogicalRouterConfig.md) |  | [optional] 
**router_type** | **str** | TIER0 for external connectivity. TIER1 for two tier topology with TIER0 on top. VRF for isolation of routing table on TIER0.  | 
**preferred_edge_cluster_member_index** | **int** | Preferred edge cluster member index which is required for PREEMPTIVE failover mode. Used for Tier0 routers only.  | [optional] 
**high_availability_mode** | **str** | High availability mode | [optional] 
**edge_cluster_id** | **str** | Used for tier0 routers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

