# RenderConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The color to use when rendering an entity. For example, set color as &#x27;RED&#x27; to render a portion of donut in red. | [optional] 
**condition** | **str** | If the condition is met then the rendering specified for the condition will be applied. Examples of expression syntax are provided under &#x27;example_request&#x27; section of &#x27;CreateWidgetConfiguration&#x27; API. | [optional] 
**display_value** | **str** | If specified, overrides the field value. This can be used to display a meaningful value in situations where field value is not available or not configured. | [optional] 
**tooltip** | [**list[Tooltip]**](Tooltip.md) | Multi-line text to be shown on tooltip while hovering over the UI element if the condition is met. | [optional] 
**icons** | [**list[Icon]**](Icon.md) | Icons to be applied at dashboard for widgets and UI elements. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

