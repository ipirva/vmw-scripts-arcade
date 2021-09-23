# WidgetConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_set** | [**FeatureSet**](FeatureSet.md) |  | [optional] 
**default_filter_value** | [**list[DefaultFilterValue]**](DefaultFilterValue.md) | Default filter values to be passed to datasources. This will be used when the report is requested without filter values. | [optional] 
**display_name** | **str** | Title of the widget. If display_name is omitted, the widget will be shown without a title. | [optional] 
**datasources** | [**list[Datasource]**](Datasource.md) | The &#x27;datasources&#x27; represent the sources from which data will be fetched. Currently, only NSX-API is supported as a &#x27;default&#x27; datasource. An example of specifying &#x27;default&#x27; datasource along with the urls to fetch data from is given at &#x27;example_request&#x27; section of &#x27;CreateWidgetConfiguration&#x27; API. | [optional] 
**weight** | **int** | Specify relavite weight in WidgetItem for placement in a view. Please see WidgetItem for details. | [optional] 
**footer** | [**Footer**](Footer.md) |  | [optional] 
**filter_value_required** | **bool** | Flag to indicate that widget will continue to work without filter value. If this flag is set to false then default_filter_value is manadatory. | [optional] [default to True]
**span** | **int** | Represents the horizontal span of the widget / container. | [optional] 
**icons** | [**list[Icon]**](Icon.md) | Icons to be applied at dashboard for widgets and UI elements. | [optional] 
**is_drilldown** | **bool** | Set to true if this widget should be used as a drilldown. | [optional] [default to False]
**filter** | **str** | Id of filter widget for subscription, if any. Id should be a valid id of an existing filter widget. Filter widget should be from the same view. Datasource URLs should have placeholder values equal to filter alias to accept the filter value on filter change. | [optional] 
**drilldown_id** | **str** | Id of drilldown widget, if any. Id should be a valid id of an existing widget. A widget is considered as drilldown widget when it is associated with any other widget and provides more detailed information about any data item from the parent widget. | [optional] 
**shared** | **bool** | Please use the property &#x27;shared&#x27; of View instead of this. The widgets of a shared view are visible to other users. | [optional] 
**legend** | [**Legend**](Legend.md) |  | [optional] 
**resource_type** | **str** | Supported visualization types are LabelValueConfiguration, DonutConfiguration, GridConfiguration, StatsConfiguration, MultiWidgetConfiguration, GraphConfiguration, ContainerConfiguration, CustomWidgetConfiguration and DropdownFilterWidgetConfiguration. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

