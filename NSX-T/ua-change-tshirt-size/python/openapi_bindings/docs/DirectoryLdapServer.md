# DirectoryLdapServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Directory LDAP server connection user name. | [optional] 
**host** | **str** | Directory LDAP server DNS host name or ip address which is reachable by NSX manager to be connected and do object synchronization. | 
**protocol** | **str** | Directory LDAP server connection protocol which is either LDAP or LDAPS. | [optional] [default to 'LDAP']
**thumbprint** | **str** | Directory LDAP server certificate thumbprint used in secure LDAPS connection. | [optional] 
**password** | **str** | Directory LDAP server connection password. | [optional] 
**domain_name** | **str** | Directory domain name which best describes the domain. It could be unique fqdn name or it could also be descriptive. There is no unique contraint for domain name among different domains. | [optional] 
**port** | **int** | Directory LDAP server connection TCP/UDP port. | [optional] [default to 389]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

