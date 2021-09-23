# LbEdgeNodeUsage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_credit_number** | **int** | The current credit number reflects the current usage on the node. For example, configuring a medium load balancer on a node consumes 10 credits. If there are 2 medium instances configured on a node, the current credit number is 2 * 10 &#x3D; 20.  | [optional] 
**form_factor** | **str** | The form factor of the given edge node.  | [optional] 
**current_virtual_servers** | **int** | The number of virtual servers configured on the node.  | [optional] 
**current_small_load_balancer_services** | **int** | The number of small load balancer services configured on the node.  | [optional] 
**current_pool_members** | **int** | The number of pool members configured on the node.  | [optional] 
**severity** | **str** | The severity calculation is based on current credit usage percentage of load balancer for one node.  | [optional] 
**current_pools** | **int** | The number of pools configured on the node.  | [optional] 
**remaining_pool_members** | **int** | The remaining number of pool members which could be configured on the given edge node.  | [optional] 
**edge_cluster_id** | **str** | The ID of edge cluster which contains the edge node.  | [optional] 
**remaining_xlarge_load_balancer_services** | **int** | The remaining number of xlarge load balancer services which could be configured on the given edge node.  | [optional] 
**remaining_small_load_balancer_services** | **int** | The remaining number of small load balancer services which could be configured on the given edge node.  | [optional] 
**current_xlarge_load_balancer_services** | **int** | The number of xlarge load balancer services configured on the node.  | [optional] 
**usage_percentage** | **float** | The usage percentage of the edge node for load balancer. The value is the larger value between load balancer credit usage percentage and pool member usage percentage for the edge node.  | [optional] 
**current_large_load_balancer_services** | **int** | The number of large load balancer services configured on the node.  | [optional] 
**remaining_credit_number** | **int** | The remaining credit number is the remaining credits that can be used for load balancer service configuration. For example, an edge node with form factor LARGE_VIRTUAL_MACHINE has 40 credits, and a medium load balancer instance costs 10 credits. If there are currently 3 medium instances configured, the remaining credit number is 40 - (3 * 10) &#x3D; 10.  | [optional] 
**remaining_large_load_balancer_services** | **int** | The remaining number of large load balancer services which could be configured on the given edge node.  | [optional] 
**remaining_medium_load_balancer_services** | **int** | The remaining number of medium load balancer services which could be configured on the given edge node.  | [optional] 
**current_medium_load_balancer_services** | **int** | The number of medium load balancer services configured on the node.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

