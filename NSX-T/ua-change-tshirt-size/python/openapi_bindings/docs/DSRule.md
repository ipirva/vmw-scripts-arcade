# DSRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | Flag to indicate whether rule is default. | [optional] 
**direction** | **str** | Rule direction in case of stateless distributed service rules. This will only considered if section level parameter is set to stateless. Default to IN_OUT if not specified. | [optional] [default to 'IN_OUT']
**rule_tag** | **str** | User level field which will be printed in CLI and packet logs. | [optional] 
**ip_protocol** | **str** | Type of IP packet that should be matched while enforcing the rule. | [optional] [default to 'IPV4_IPV6']
**notes** | **str** | User notes specific to the rule. | [optional] 
**applied_tos** | [**list[ResourceReference]**](ResourceReference.md) | List of object where rule will be enforced. The section level field overrides this one. Null will be treated as any. | [optional] 
**logged** | **bool** | Flag to enable packet logging. Default is disabled. | [optional] [default to False]
**disabled** | **bool** | Flag to disable rule. Disabled will only be persisted but never provisioned/realized. | [optional] [default to False]
**sources** | [**list[ResourceReference]**](ResourceReference.md) | List of sources. Null will be treated as any. | [optional] 
**action** | **str** | Action enforced on the packets which matches the distributed service rule. Currently DS Layer supports below actions. ALLOW           - Forward any packet when a rule with this action gets a match (Used by Firewall). DROP            - Drop any packet when a rule with this action gets a match. Packets won&#x27;t go further(Used by Firewall). REJECT          - Terminate TCP connection by sending TCP reset for a packet when a rule with this action gets a match (Used by Firewall). REDIRECT        - Redirect any packet to a partner appliance when a rule with this action gets a match (Used by Service Insertion). DO_NOT_REDIRECT - Do not redirect any packet to a partner appliance when a rule with this action gets a match (Used by Service Insertion). DETECT          - Detect IDS Signatures. ALLOW_CONTINUE  - Allows rules to jump from this rule. Action on matching rules in the destination category will decide next step. Application is default destination until new categories are supported to jump to. DETECT_PREVENT  - Detect and Prevent IDS Signatures. | 
**priority** | **int** | Priority of the rule. | [optional] 
**sources_excluded** | **bool** | Negation of the source. | [optional] [default to False]
**destinations_excluded** | **bool** | Negation of the destination. | [optional] [default to False]
**destinations** | [**list[ResourceReference]**](ResourceReference.md) | List of the destinations. Null will be treated as any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

