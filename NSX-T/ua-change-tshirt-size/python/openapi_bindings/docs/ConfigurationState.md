# ConfigurationState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Gives details of state of desired configuration. Additional enums with more details on progress/success/error states are sent for edge node. The success states are NODE_READY and TRANSPORT_NODE_READY, pending states are {VM_DEPLOYMENT_QUEUED, VM_DEPLOYMENT_IN_PROGRESS, REGISTRATION_PENDING} and other values indicate failures. \&quot;in_sync\&quot; state indicates that the desired configuration has been received by the host to which it applies, but is not yet in effect. When the configuration is actually in effect, the state will change to \&quot;success\&quot;. Please note, failed state is deprecated.  | [optional] 
**details** | [**list[ConfigurationStateElement]**](ConfigurationStateElement.md) | Array of configuration state of various sub systems | [optional] 
**failure_code** | **int** | Error code | [optional] 
**failure_message** | **str** | Error message in case of failure | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

