# LbVirtualServerWithRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**list[LbRule]**](LbRule.md) | It is used to add rules, update rules and bind rules to the virtual server. To add new rules, make sure that the rules have no identifier specified, the new rules are automatically generated and associated to the virtual server. If the virtual server need to consume some existed rules without change, those rules should not be specified in the list, otherwise, the rules are updated. For update_with_rules action, it supports rules delete and update. To delete old rules, the rules should not be configured in new action, the UUID of deleted rules should be removed from rule_ids. To update rules, the rules should be specified with new change and configured with identifier. If there are some rules which are not modified, those rule should not be specified in the rules list, the UUID list of rules should be specified in rule_ids of LbVirtualServer.  | [optional] 
**virtual_server** | [**LbVirtualServer**](LbVirtualServer.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

