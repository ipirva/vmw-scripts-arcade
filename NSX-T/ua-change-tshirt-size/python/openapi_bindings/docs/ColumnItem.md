# ColumnItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_key** | **str** | Sorting on column is based on the sort_key. sort_key represents the field in the output data on which sort is requested. | [optional] 
**type** | **str** | Data type of the field. | [default to 'String']
**tooltip** | [**list[Tooltip]**](Tooltip.md) | Multi-line text to be shown on tooltip while hovering over a cell in the grid. | [optional] 
**label** | [**Label**](Label.md) |  | 
**field** | **str** | Field from which values of the column will be derived. | 
**sort_ascending** | **bool** | If true, the value of the column are sorted in ascending order. Otherwise, in descending order. | [optional] [default to True]
**drilldown_id** | **str** | Id of drilldown widget, if any. Id should be a valid id of an existing widget. | [optional] 
**hidden** | **bool** | If set to true, hides the column | [optional] [default to False]
**navigation** | **str** | Hyperlink of the specified UI page that provides details. If drilldown_id is provided, then navigation cannot be used. | [optional] 
**column_identifier** | **str** | Identifies the column and used for fetching content upon an user click or drilldown. If column identifier is not provided, the column&#x27;s data will not participate in searches and drilldowns. | [optional] 
**render_configuration** | [**list[RenderConfiguration]**](RenderConfiguration.md) | Render configuration to be applied, if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

