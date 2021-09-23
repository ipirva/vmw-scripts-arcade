# LogicalPort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logical_switch_id** | **str** | Id of the Logical switch that this port belongs to. | 
**init_state** | **str** | Set initial state when a new logical port is created. &#x27;UNBLOCKED_VLAN&#x27; means new port will be unblocked on traffic in creation, also VLAN will be set with corresponding logical switch setting. This port setting can only be configured at port creation (POST), and cannot be modified. &#x27;RESTORE_VIF&#x27; fetches and restores VIF attachment from ESX host.  | [optional] 
**switching_profile_ids** | [**list[SwitchingProfileTypeIdEntry]**](SwitchingProfileTypeIdEntry.md) |  | [optional] 
**attachment** | [**LogicalPortAttachment**](LogicalPortAttachment.md) |  | [optional] 
**internal_id** | **str** | The internal_id of the logical port may or may not be identical to it&#x27;s managed resource ID. If a VirtualMachine connected to logical port migrates from one site to another, then on the destination site, it will be connected to different logical port managed resource. However, the internal_id field will be persisted across vmotion.  | [optional] 
**extra_configs** | [**list[ExtraConfig]**](ExtraConfig.md) | This property could be used for vendor specific configuration in key value string pairs. Logical port setting will override logical switch setting if the same key was set on both logical switch and logical port.  | [optional] 
**address_bindings** | [**list[PacketAddressClassifier]**](PacketAddressClassifier.md) | Each address binding must contain both an IPElement and MAC address. VLAN ID is optional. This binding configuration can be used by features such as spoof-guard and overrides any discovered bindings. Any non unique entries are deduplicated to generate a unique set of address bindings and then stored. For IP addresses, a subnet address cannot have host bits set. A maximum of 128 unique address bindings is allowed per port.  | [optional] 
**ignore_address_bindings** | [**list[PacketAddressClassifier]**](PacketAddressClassifier.md) | IP Discovery module uses various mechanisms to discover address bindings being used on each port. If a user would like to ignore any specific discovered address bindings or prevent the discovery of a particular set of discovered bindings, then those address bindings can be provided here. Currently IP range in CIDR format is not supported.  | [optional] 
**admin_state** | **str** | Represents Desired state of the logical port | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

