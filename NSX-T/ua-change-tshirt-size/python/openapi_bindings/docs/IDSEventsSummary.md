# IDSEventsSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_occurence** | **int** | First occurence of the intrusion, in epoch milliseconds. | [optional] 
**latest_occurence** | **int** | Latest occurence of the intrusion, in epoch milliseconds. | [optional] 
**total_count** | **int** | Number of times this particular signature was detected. | [optional] 
**user_details** | **object** | List of users logged into VMs on which a particular signature was detected. | [optional] 
**vm_details** | **object** | List of VMs on which a particular signature was detected with the count. | [optional] 
**is_rule_valid** | **bool** | Indicates if the rule id is valid or not. | [optional] 
**signature_metadata** | **object** | Metadata about the detected signature including name, id, severity, product affected, protocol etc. | [optional] 
**idsflow_details** | **object** | IDS event flow data specific to each IDS event. The data includes source ip, source port, destination ip, destination port, and protocol. | [optional] 
**signature_id** | **int** | Signature ID pertaining to the detected intrusion. | [optional] 
**rule_id** | **int** | The IDS Rule id that detected this particular intrusion. | [optional] 
**is_ongoing** | **bool** | Flag indicating an ongoing intrusion. | [optional] 
**affected_vm_count** | **int** | Count of VMs on which a particular signature was detected. | [optional] 
**resource_type** | **str** | IDSEvent resource type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

