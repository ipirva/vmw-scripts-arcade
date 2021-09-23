# GraphConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_value_type** | **str** | x value type. | [optional] [default to 'string']
**graphs** | [**list[GraphDefinition]**](GraphDefinition.md) | Graphs | 
**axes** | [**Axes**](Axes.md) |  | [optional] 
**navigation** | **str** | Hyperlink of the specified UI page that provides details. | [optional] 
**sub_type** | **str** | Describes the the type of graph. LINE_GRAPH shows a line graph chart BAR_GRAPH shows a simple bar graph chart STACKED_BAR_GRAPH shows a stacked bar graph chart | [optional] [default to 'BAR_GRAPH']
**display_x_value** | **bool** | If true, value of a point is shown as label on X axis. If false, value of point is not shown as label on X axis. false can be useful in situations where there are too many points and showing the X value as label can clutter the X axis. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

