# ServiceManager

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Integer port value to specify a standard/non-standard HTTPS port. | 
**service_ids** | [**list[ResourceReference]**](ResourceReference.md) | The IDs of services, provided by partner. | 
**authentication_scheme** | [**CallbackAuthenticationScheme**](CallbackAuthenticationScheme.md) |  | 
**thumbprint** | **str** | Thumbprint (SHA-256 hash represented in lower case hex) for the certificate on the partner console. This will be required to establish secure communication with the console and to avoid man-in-the-middle attacks. | [optional] 
**vendor_id** | **str** | Id which is unique to a vendor or partner for which the service is created. | [optional] 
**uri** | **str** | URI on which notification requests should be made on the specified server. | 
**server** | **str** | IP address or fully qualified domain name of the partner REST server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

