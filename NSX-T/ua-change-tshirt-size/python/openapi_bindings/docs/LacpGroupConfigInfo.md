# LacpGroupConfigInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key represents the identifier for the group that is unique across VC.  | [optional] 
**name** | **str** | The display name of the LACP group. | [optional] 
**uplink_port_keys** | **list[str]** | Keys for the uplink ports in the group. Each uplink port is assigned a key that is unique across VC.  | [optional] 
**load_balance_algorithm** | **str** | Load balance algorithm used in LACP group. The possible values are dictated by the values available in VC. Please refer VMwareDvsLacpLoadBalanceAlgorithm documentation for a full list of values. A few examples are srcDestIp where source and destination IP are considered, srcIp where only source IP is considered.  | [optional] 
**uplink_num** | **int** | The number of uplink ports | [optional] 
**uplink_names** | **list[str]** | Names for the uplink ports in the group. | [optional] 
**mode** | **str** | The mode of LACP can be ACTIVE or PASSIVE. If the mode is ACTIVE, LACP is enabled unconditionally. If the mode is PASSIVE, LACP is enabled only if LACP device is detected.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

