# DhcpProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_cluster_member_indexes** | **list[int]** | The Edge nodes on which the DHCP servers run. If none is provided, the NSX will auto-select two edge-nodes from the given edge cluster. If only one edge node is provided, the DHCP servers will run without HA support.  | [optional] 
**enable_standby_relocation** | **bool** | Flag to enable the auto-relocation of standby DHCP Service in case of edge node failure. Only tier 1 and auto placed DHCP servers are considered for the relocation.  | [optional] [default to False]
**edge_cluster_id** | **str** | Edge cluster uuid on which the referencing logical DHCP server runs.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

