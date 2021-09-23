# MigrationFeedbackRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolved** | **bool** | Indicates if a valid response already exist for this feedback request. | [optional] 
**accepted_actions** | **list[str]** | List of acceptable actions for this feedback request. | [optional] 
**hash** | **str** | Identify a feedback request type across objects. This can be used to group together objects with similar feedback request and resolve them in one go. | [optional] 
**vertical** | **str** | Functional area that this query falls into. | [optional] 
**v_object_id** | **str** | Identifier for this object in the source NSX endpoint. | [optional] 
**suggested_value** | **str** | The suggested value to resolve this feedback request. | [optional] 
**message** | **str** | Detailed feedback request with options. | [optional] 
**object_id** | **str** | Identifier of the object for which feedback is requested. | [optional] 
**accepted_value_type** | **str** | Data type of the items listed in acceptable values list. | [optional] 
**v_object_name** | **str** | Name of this object in the source NSX endpoint. | [optional] 
**multi_value** | **bool** | Indicates if multiple values can be selected as response from the list of acceptable value. | [optional] 
**accepted_values** | **list[str]** | List of acceptable values for this feedback request. | [optional] 
**id** | **str** | Identifier of the feedback request. | [optional] 
**suggested_action** | **str** | The suggested action to resolve this feedback request. | [optional] 
**sub_vertical** | **str** | Functional sub-area that this query falls into. | [optional] 
**resolution** | **str** | If the feedback request was resolved earlier, provides details about the previous resolution. | [optional] 
**rejected** | **bool** | Indicates if previous response was invalid. Please provide a valid response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

