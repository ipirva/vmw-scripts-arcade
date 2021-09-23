# IDSEventsBySignature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of times this particular signature was detected. | [optional] 
**first_occurence** | **int** | First occurence of the intrusion, in epoch milliseconds. | [optional] 
**severity** | **str** | Severity of the threat covered by the signature, can be Critical, High, Medium, or Low. | [optional] 
**signature_name** | **str** | Name of the signature pertaining to the detected intrusion. | [optional] 
**is_ongoing** | **bool** | Flag indicating an ongoing intrusion. | [optional] 
**signature_id** | **int** | Signature ID pertaining to the detected intrusion. | [optional] 
**resource_type** | **str** | IDSEvent resource type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

