# IDSSignatureDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_product** | **str** | Product affected by the signature. | [optional] 
**direction** | **str** | Source-destination direction. | [optional] 
**protocol** | **str** | Protocol used in the packet analysis. | [optional] 
**class_type** | **str** | Class type of the signature. | [optional] 
**enabled** | **bool** | Signature enabled. | [optional] 
**action** | **str** | Packet analysis action | [optional] 
**tag** | **list[str]** | Vendor assigned classification tag. | [optional] 
**malware_family** | **str** | Family of the malware tracked in the signature. | [optional] 
**name** | **str** | Name of the signature. | [optional] 
**category** | **list[str]** | VMware defined signature category. | [optional] 
**cvssv3** | **str** | Signature CVSSV3 score. | [optional] 
**cvssv2** | **str** | Signature CVSSV2 score. | [optional] 
**severity** | **str** | VMware defined signature severity. | [optional] 
**signature_revision** | **int** | The revision of the signature | [optional] 
**performance_impact** | **str** | Performance impact of the signature. | [optional] 
**flow** | **str** | Flow established from server, from client etc. | [optional] 
**signature_severity** | **str** | Signature vendor set severity of the signature rule. | [optional] 
**urls** | **list[str]** | List of mitre attack URLs pertaining to signature. | [optional] 
**policy** | **list[str]** | Signature policy. | [optional] 
**attack_target** | **str** | Target of the attack tracked in the signature. | [optional] 
**signature_id** | **int** | Unique ID of the signature rule. | [optional] 
**cves** | **list[str]** | CVE of the signature. | [optional] 
**type** | **list[str]** | Signature type. | [optional] 
**resource_type** | **str** | IDSSignatureDetail resource type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

