# DirectoryDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_servers** | [**list[DirectoryLdapServer]**](DirectoryLdapServer.md) | Directory domain LDAP servers&#x27; information including host, name, port, protocol and so on. | 
**name** | **str** | Directory domain name which best describes the domain. It could be unique fqdn name or it could also be descriptive. There is no unique contraint for domain name among different domains. | 
**resource_type** | **str** | Domain resource type comes from multiple sub-classes extending this base class. For example, DirectoryAdDomain is one accepted resource_type. If there are more sub-classes defined, they will also be accepted resource_type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

