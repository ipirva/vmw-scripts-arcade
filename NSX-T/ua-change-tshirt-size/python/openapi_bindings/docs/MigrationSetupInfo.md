# MigrationSetupInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_nsx** | [**DestinationNsxApiEndpoint**](DestinationNsxApiEndpoint.md) |  | [optional] 
**source_nsx** | [**list[SourceNsxApiEndpoint]**](SourceNsxApiEndpoint.md) | List of source NSX manager endpoints. | [optional] 
**migration_mode** | **str** | Migration mode can be VMC_V2T, ONPREMISE_V2T, ONPREMISE_VSPHERE2T, DFW_ONLY, DFW_WITH_BRIDGED_SEG, CMP_VRA, DFW_AND_HOST_AND_WORKLOAD, DFW_AND_HOST_AND_WORKLOAD_WITH_BRIDGED_SEG, NS_CUTOVER | [optional] [default to 'ONPREMISE_V2T']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

