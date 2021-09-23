# NicMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_label** | **str** | Network Interface label. | 
**interface_type** | **str** | Interface that needs to be configured on the partner appliance. Ex. MANAGEMENT, DATA1, DATA2, HA1, HA2, CONTROL. | 
**transports** | **list[str]** | Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP. Here, the transports array specifies the kinds of transport where this particular NIC is user configurable. If nothing is specified, and the \&quot;user_configurable\&quot; flag is true, then user configuration will be allowed for all transports. If any transport is/are specified, then it will be considered as user configurable for the specified transports only.\&quot; | [optional] 
**user_configurable** | **bool** | Used to specify if the given interface needs configuration. Management nics will always need the configuration, for others it will be use case specific. For example, a DATA NIC may be user configurable if the appliance is deployed in certain mode, such as L3_ROUTED. | [optional] 
**interface_index** | **int** | Network Interface index. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

