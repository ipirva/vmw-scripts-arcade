# IPMirrorDestination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ips** | **list[str]** | The destination IPs of the mirror packet will be sent to. | 
**encapsulation_type** | **str** | You can choose GRE, ERSPAN II or ERSPAN III. | [default to 'GRE']
**erspan_id** | **int** | Used by physical switch for the mirror traffic forwarding. Must be provided and only effective when encapsulation type is ERSPAN type II or type III.  | [optional] 
**gre_key** | **int** | User-configurable 32-bit key only for GRE | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

