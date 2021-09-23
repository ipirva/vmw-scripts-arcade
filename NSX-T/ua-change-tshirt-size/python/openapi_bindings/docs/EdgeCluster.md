# EdgeCluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_node_type** | **str** | Edge cluster is homogenous collection of transport nodes. Hence all transport nodes of the cluster must be of same type. This readonly field shows the type of transport nodes.  | [optional] 
**members** | [**list[EdgeClusterMember]**](EdgeClusterMember.md) | EdgeCluster only supports homogeneous members. These member should be backed by either EdgeNode or PublicCloudGatewayNode. TransportNode type of these nodes should be the same. DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to be the same. EdgeCluster supports members of different deployment types.  | [optional] 
**node_rtep_ips** | [**list[NodeRtepIpsConfig]**](NodeRtepIpsConfig.md) | List of remote tunnel endpoint ipaddress configured on edge cluster for each transport node. | [optional] 
**cluster_profile_bindings** | [**list[ClusterProfileTypeIdEntry]**](ClusterProfileTypeIdEntry.md) | Edge cluster profile bindings | [optional] 
**enable_inter_site_forwarding** | **bool** | Flag should be only use in federation for inter site l2 and l3 forwarding. Before enabling this flag, all the edge cluster members must have remote tunnel endpoint configured. TIER0/TIER1 logical routers managed by GM must be associated with edge cluster which has inter-site forwarding enabled.  | [optional] 
**allocation_rules** | [**list[AllocationRule]**](AllocationRule.md) | Set of allocation rules and respected action for auto placement of logical router, DHCP and MDProxy on edge cluster members.  | [optional] 
**deployment_type** | **str** | This field is a readonly field which shows the deployment_type of members. It returns UNKNOWN if there are no members, and returns VIRTUAL_MACHINE| PHYSICAL_MACHINE if all edge members are VIRTUAL_MACHINE|PHYSICAL_MACHINE. It returns HYBRID if the cluster contains edge members of both types VIRTUAL_MACHINE and PHYSICAL_MACHINE.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

