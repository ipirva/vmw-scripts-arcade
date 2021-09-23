# ServiceInsertionServiceProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**list[Attribute]**](Attribute.md) | List of attributes specific to a partner for which the service is created. These attributes are passed on to the partner appliance and are opaque to the NSX Manager. If a vendor template exposes configurables, then the values are specified here. | [optional] 
**service_id** | **str** | The service to which the service profile belongs. | [optional] 
**redirection_action** | **str** | The redirection action represents if the packet is exclusively redirected to the service, or if a copy is forwarded to the service. The service insertion profile inherits the redirection action if already specified at the vendor template. However the service profile cannot overide the action specified at the vendor template. | [optional] [default to 'PUNT']
**vendor_template_id** | **str** | Id of the vendor template to be used by the servive profile. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

