# SourceNsxApiEndpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vc_port** | **int** | VC port that will be used to fetch details. | [optional] [default to 443]
**vc_username** | **str** | Username for connecting to VC. | 
**vc_ip** | **str** | IP address or host name of VC. | 
**ip** | **str** | IP address or hostname of a source NSX API endpoint. This field is not applicable in case of vSphere network migration. | [optional] 
**auth_token** | **str** | Auth token used to make REST calls to source NSX API endpoint. This field is not applicable in case of vSphere network migration. | [optional] 
**nsx_syncrole** | **str** | Signifies Universal Sync role status (STANDALONE, PRIMARY, SECONDARY) of a source NSX API endpoint. | [optional] 
**vc_version** | **str** | Build version of VC. | [optional] 
**nsx_username** | **str** | Username for connecting to NSX manager. This field is not applicable in case of vSphere network migration. | [optional] 
**nsx_version** | **str** | Build version (major, minor, patch) of a source NSX API endpoint. | [optional] 
**nsx_password** | **str** | Password for connecting to NSX manager. This field is not applicable in case of vSphere network migration. | [optional] 
**vc_password** | **str** | Password for connecting to VC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

