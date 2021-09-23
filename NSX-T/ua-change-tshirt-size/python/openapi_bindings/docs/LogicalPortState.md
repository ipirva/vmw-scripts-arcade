# LogicalPortState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_node_ids** | **list[str]** | Identifiers of the transport node where the port is located | [optional] 
**attachment** | [**LogicalPortAttachmentState**](LogicalPortAttachmentState.md) |  | [optional] 
**duplicate_bindings** | [**list[DuplicateAddressBindingEntry]**](DuplicateAddressBindingEntry.md) | If any address binding discovered on the port is also found on other port on the same logical switch, then it is included in the duplicate bindings list along with the ID of the port with which it conflicts.  | [optional] 
**discovered_bindings** | [**list[AddressBindingEntry]**](AddressBindingEntry.md) | Contains the list of address bindings for a logical port that were automatically dicovered using various snooping methods like ARP, DHCP etc.  | [optional] 
**id** | **str** | Id of the logical port | 
**realized_bindings** | [**list[AddressBindingEntry]**](AddressBindingEntry.md) | List of logical port bindings that are realized. This list may be populated from the discovered bindings or manual user specified bindings. This binding configuration can be used by features such as firewall, spoof-guard, traceflow etc.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

