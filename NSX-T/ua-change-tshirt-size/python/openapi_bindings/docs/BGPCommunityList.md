# BGPCommunityList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communities** | **list[str]** | Array of BGP communities | 
**logical_router_id** | **str** | Logical router id | [optional] 
**community_type** | **str** | BGP community type. It has two types as NormalBGPCommunity BGP normal community which includes well-known community name as well as community value in range from [1-4294967295] or value in aa:nn format(aa/nn range from 1-65535). LargeBGPCommunity BGP large community which includes community value in aa:bb:nn format where aa, bb, nn are unsigned integers in the range [1-4294967295].  | [optional] [default to 'NormalBGPCommunity']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

