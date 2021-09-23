# MacLearningSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | This property specifies the limit on the maximum number of MAC addresses that can be learned on a port. It is consumed by vswitch kernel module on the hypervisor while learning MACs per port for VMs that are local to the host.  | [optional] [default to 4096]
**limit_policy** | **str** | The policy after MAC Limit is exceeded | [optional] [default to 'ALLOW']
**remote_overlay_mac_limit** | **int** | This property specifies the limit on the maximum number of MACs learned for a remote Virtual Machine&#x27;s MAC to vtep binding per overlay logical switch.  | [optional] [default to 2048]
**aging_time** | **int** | Aging time in sec for learned MAC address | [optional] [default to 600]
**enabled** | **bool** | Allowing source MAC address learning | 
**unicast_flooding_allowed** | **bool** | Allowing flooding for unlearned MAC for ingress traffic | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

