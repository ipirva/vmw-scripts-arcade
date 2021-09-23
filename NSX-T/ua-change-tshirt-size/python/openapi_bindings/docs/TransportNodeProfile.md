# TransportNodeProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_switch_spec** | [**HostSwitchSpec**](HostSwitchSpec.md) |  | [optional] 
**ignore_overridden_hosts** | **bool** | Transport Node Profiles specify the configuration that is applied to all hosts in a cluster. The user has the ability to update the configuration on individual hosts within a cluster which will cause the host configuration to differ from the Transport Node Profile and results in the host to be marked as overridden. If a Transport Node Profile is edited or a new Transport Node Profile is applied on a Transport Node Collection, by default, the host configuration will be overwritten with the Transport Node Profile configuration and the overridden flag will be reset to false. This flag should be used when hosts that are set as overridden should not adopt the Transport Node Profile configuration when it is being updated or a new one is applied to the Transport Node Collection. In other words, when this flag is set to the default value of false and configuration is applied at the cluster level, the configuration will be applied on all hosts regardless if overridden or not. When this flag is set to true, all hosts that are set as overridden, i.e., have been updated invidivually, will be ignored and the cluster-level configuration will not be applied. Note, Transport Node Profiles can be applied on multiple clusters. This field will dictate the behavior followed by all clusters using this Transport Node Profile.  | [optional] [default to False]
**transport_zone_endpoints** | [**list[TransportZoneEndPoint]**](TransportZoneEndPoint.md) | This is deprecated. TransportZoneEndPoints should be specified per host switch at StandardHostSwitch through Transport Node or Transport Node Profile configuration. This will ONLY include the TransportZoneEndpoints that were were specified here during the TransportNode configuration. If TransportZoneEndpoints are specified directly in {$ref: StandardHostSwitch}, such TransportZoneEndpoints will not be populated here.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
