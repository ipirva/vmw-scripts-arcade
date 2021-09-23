# PortMirroringSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Port mirroring session direction | 
**mirror_sources** | [**list[MirrorSource]**](MirrorSource.md) | Mirror sources | 
**encapsulation_vlan_id** | **int** | Only for Remote SPAN Port Mirror. | [optional] 
**session_type** | **str** | If this property is unset, this session will be treated as LocalPortMirrorSession.  | [optional] [default to 'LocalPortMirrorSession']
**snap_length** | **int** | If this property is set, the packet will be truncated to the provided length. If this property is unset, entire packet will be mirrored.  | [optional] 
**port_mirroring_filters** | [**list[PortMirroringFilter]**](PortMirroringFilter.md) | An array of 5-tuples used to filter packets for the mirror session, if not provided, all the packets will be mirrored. | [optional] 
**tcp_ip_stack** | **str** | If set to mirror, mirror packet will be sent via dedicated mirror stack to destination; If set to default, mirror packet will be sent via default stack; So far, the value mirror can only be chosen in L3PortMirrorSession.  | [optional] 
**preserve_original_vlan** | **bool** | Only for Remote SPAN Port Mirror. Whether to preserve original VLAN. | [optional] [default to False]
**mirror_destination** | [**MirrorDestination**](MirrorDestination.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

