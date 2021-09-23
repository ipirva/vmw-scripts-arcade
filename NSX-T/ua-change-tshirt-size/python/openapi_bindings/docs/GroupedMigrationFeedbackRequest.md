# GroupedMigrationFeedbackRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolved** | **bool** | Indicates if a valid response already exist for all feedback requests in this group. | [optional] 
**accepted_actions** | **list[str]** | List of acceptable actions for this feedback request. | [optional] 
**hash** | **str** | Identify a feedback request type across objects. This can be used to group together objects with similar feedback request and resolve them in one go. | [optional] 
**vertical** | **str** | Functional area that this query falls into. | [optional] 
**suggested_value** | **str** | The suggested value to resolve this feedback request. | [optional] 
**multi_value** | **bool** | Indicates if multiple values can be selected as response from the list of acceptable value. | [optional] 
**sub_vertical** | **str** | Functional sub-area that this query falls into. | [optional] 
**objects** | [**list[SummaryMigrationFeedbackRequest]**](SummaryMigrationFeedbackRequest.md) | Collection of feedback requests of a given type | 
**accepted_values** | **list[str]** | List of acceptable values for this feedback request. | [optional] 
**message** | **str** | Detailed feedback request with options. | [optional] 
**accepted_value_type** | **str** | Data type of the items listed in acceptable values list. | [optional] 
**suggested_action** | **str** | The suggested action to resolve this feedback request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

