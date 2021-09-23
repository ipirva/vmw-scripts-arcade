# ServiceChain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse_path_service_profiles** | [**list[ResourceReference]**](ResourceReference.md) | List of ServiceInsertionServiceProfiles id. Reverse path service profiles are applied to egress traffic and is optional. 2 different set of profiles can be defined for forward and reverse path. If not defined, the reverse of the forward path service profile is applied. | [optional] 
**service_attachments** | [**list[ResourceReference]**](ResourceReference.md) | Service attachment specifies the scope i.e Service plane at which the SVMs are deployed. | 
**forward_path_service_profiles** | [**list[ResourceReference]**](ResourceReference.md) | List of ServiceInsertionServiceProfiles that constitutes the the service chain. The forward path service profiles are applied to ingress traffic. | 
**service_chain_id** | **str** | A unique id generated for every service chain. This is not a uuid. | [optional] 
**path_selection_policy** | **str** | Path selection policy can be - ANY - Service Insertion is free to redirect to any service path regardless of any load balancing considerations or flow pinning. LOCAL - means to prefer local service insances. REMOTE - preference is to redirect to the SVM co-located on the same host. | [optional] [default to 'ANY']
**on_failure_policy** | **str** | Failure policy for the service tells datapath, the action to take i.e to allow or block traffic during failure scenarios. | [optional] [default to 'ALLOW']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

