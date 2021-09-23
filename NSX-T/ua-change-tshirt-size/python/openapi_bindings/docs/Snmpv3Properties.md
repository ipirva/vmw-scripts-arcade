# Snmpv3Properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_protocol** | **str** | Authentication protocol used for SNMP v3 communication. | [optional] [default to 'SHA1']
**priv_protocol** | **str** | Privacy protocol used for SNMP v3 communication. | [optional] [default to 'AES128']
**users** | [**list[Snmpv3User]**](Snmpv3User.md) | List of SNMP v3 users allowed to poll NSX nodes over SNMP. Also, users specified in a SNMP v3 target must exist in this list. | [optional] 
**targets** | [**list[Snmpv3Target]**](Snmpv3Target.md) | List of SNMP v3 targets/receivers where SNMP v3 traps/notifications will be sent from NSX nodes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

