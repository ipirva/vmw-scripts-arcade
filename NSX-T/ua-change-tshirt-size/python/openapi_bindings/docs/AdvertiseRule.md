# AdvertiseRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | ALLOW action enables the advertisment and DENY action disables the advertisement of a filtered routes to the connected TIER0 router. | [optional] [default to 'ALLOW']
**rule_filter** | [**AdvertisementRuleFilter**](AdvertisementRuleFilter.md) |  | [optional] 
**display_name** | **str** | Display name | [optional] 
**networks** | **list[str]** | network(CIDR) to be routed | 
**description** | **str** | Description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

