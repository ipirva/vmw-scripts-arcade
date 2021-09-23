# IpfixDfwConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | This priority field is used to resolve conflicts in Logical Ports which are covered by more than one IPFIX profiles. The IPFIX exporter will send records to Collectors in highest priority profile (lowest number) only.  | [default to 0]
**collector** | **str** | Each IPFIX DFW config can have its own collector config.  | 
**active_flow_export_timeout** | **int** | For long standing active flows, IPFIX records will be sent per timeout period  | [optional] [default to 1]
**template_parameters** | [**IpfixDfwTemplateParameters**](IpfixDfwTemplateParameters.md) |  | [optional] 
**observation_domain_id** | **int** | An identifier that is unique to the exporting process and used to meter the Flows.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

