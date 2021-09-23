# CommunityMatchOperation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_operator** | **str** | Match operator for communities from provided community list id. MATCH_ANY will match any community MATCH_ALL will match all communities MATCH_EXACT will do exact match on community MATCH_NONE [operator not supported] will not match any community MATCH_REGEX will match normal communities by evaluating regular expression MATCH_LARGE_COMMUNITY_REGEX will match large communities by evaluating regular expression  | [optional] [default to 'MATCH_ANY']
**regular_expression** | **str** | Regular expression to match BGP communities. If match_operator is MATCH_REGEX then this value must be specified.  | [optional] 
**community_list_id** | **str** | ID of BGP community list. This value is not required when match_operator is MATCH_REGEX otherwise required.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

