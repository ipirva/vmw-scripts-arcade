# VendorTemplate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_template_key** | **str** | Different VMs in data center can have Different protection levels as specified by administrator in the policy. The identifier for the policy with which the partner appliance identifies this policy. This identifier will be passed to the partner appliance at runtime to specify which protection level is applicable for the VM being protected. | [optional] 
**attributes** | [**list[Attribute]**](Attribute.md) | List of attributes specific to a partner for which the vendor template is created. There attributes are passed on to the partner appliance and is opaque to the NSX Manager. Attributes are not supported by guest introspection service. | [optional] 
**redirection_action** | **str** | The redirection action represents if the packet is exclusively redirected to the service, or if a copy is forwarded to the service. Service profile inherits the redirection action specified at the vendor template and cannot override the action specified at the vendor template. Redirection action is not applicable to guest introspection service. | [optional] [default to 'PUNT']
**functionality** | **str** | The capabilities provided by the services. Needs to be one of the following | NG_FW - Next Generation Firewall | IDS_IPS - Intrusion detection System / Intrusion Prevention System | NET_MON - Network Monitoring | HCX - Hybrid Cloud Exchange | BYOD - Bring Your Own Device | EPP - Endpoint Protection.(Third party AntiVirus partners using NXGI should use this functionality for the service) | [optional] 
**service_id** | **str** | The service to which the vendor template belongs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

