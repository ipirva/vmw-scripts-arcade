# FirewallSection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category from policy framework. | [optional] 
**enforced_on** | **str** | This attribute represents enforcement point of firewall section. For example, firewall section enforced on logical port with attachment type bridge endpoint will have &#x27;BRIDGEENDPOINT&#x27; value, firewall section enforced on logical router will have &#x27;LOGICALROUTER&#x27; value and rest have &#x27;VIF&#x27; value. | [optional] 
**locked** | **bool** | Section is locked/unlocked. | [optional] [default to False]
**tcp_strict** | **bool** | If TCP strict is enabled on a section and a packet matches rule in it, the following check will be performed. If the packet does not belong to an existing session, the kernel will check to see if the SYN flag of the packet is set. If it is not, then it will drop the packet. | [optional] [default to False]
**lock_modified_by** | **str** | ID of the user who last modified the lock for the section. | [optional] 
**lock_modified_time** | **int** | Section locked/unlocked time in epoch milliseconds. | [optional] 
**priority** | **int** | Priority of current section with respect to other sections. In case the field is empty, the list section api should be used to get section priority. | [optional] 
**firewall_schedule** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**comments** | **str** | Comments for section lock/unlock. | [optional] 
**autoplumbed** | **bool** | This flag indicates whether it is an auto-plumbed section that is associated to a LogicalRouter. Auto-plumbed sections are system owned and cannot be updated via the API. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

