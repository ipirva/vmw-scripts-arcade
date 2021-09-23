# BridgeEndpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ha_enable** | **bool** | This field will not be used if an edge cluster is being used for the bridge endpoint  | [optional] [default to True]
**bridge_cluster_id** | **str** | This field will not be used if an edge cluster is being used for the bridge endpoint  | [optional] 
**vlan_transport_zone_id** | **str** | This field will not be used if a bridge cluster is being used for the bridge endpoint  | [optional] 
**bridge_endpoint_profile_id** | **str** | This field will not be used if a bridge cluster is being used for the bridge endpoint  | [optional] 
**uplink_teaming_policy_name** | **str** | This name has to be one of the switching uplink teaming policy names listed inside the TransportZone. If this field is not specified, bridge will use the first pnic in host-switch config. This field will not be used if a bridge cluster is being used for the bridge endpoint | [optional] 
**vlan_trunk_spec** | [**VlanTrunkSpec**](VlanTrunkSpec.md) |  | [optional] 
**vlan** | **int** | This property is used for VLAN specification of bridge endpoint. It&#x27;s mutually exclusive with &#x27;vlan_trunk_spec&#x27;, either &#x27;vlan&#x27; or &#x27;vlan_trunk_spec&#x27; should be specified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

