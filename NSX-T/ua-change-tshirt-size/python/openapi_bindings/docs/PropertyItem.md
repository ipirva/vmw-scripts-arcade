# PropertyItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Represents field value of the property. | 
**separator** | **bool** | If true, separates this property in a widget. | [optional] [default to False]
**navigation** | **str** | Hyperlink of the specified UI page that provides details. This will be linked with value of the property. | [optional] 
**render_configuration** | [**list[RenderConfiguration]**](RenderConfiguration.md) | Render configuration to be applied, if any. | [optional] 
**type** | **str** | Data type of the field. | [default to 'String']
**heading** | **bool** | Set to true if the field is a heading. Default is false. | [optional] [default to False]
**condition** | **str** | If the condition is met then the property will be displayed. Examples of expression syntax are provided under &#x27;example_request&#x27; section of &#x27;CreateWidgetConfiguration&#x27; API. | [optional] 
**label** | [**Label**](Label.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

