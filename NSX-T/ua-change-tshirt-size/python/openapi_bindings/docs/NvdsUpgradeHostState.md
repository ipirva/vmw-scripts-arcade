# NvdsUpgradeHostState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_state** | **str** | Overall state of N-VDSes on the TransportNodes | [optional] 
**state_details** | **list[str]** | Details of the N-VDS upgrade state on the host | [optional] 
**host** | **str** | TransportNode identifier | [optional] 
**upgrade_stage** | **str** | This field returns current stage of Migration task. Here is a sequence of stages the task cycles through, RETRIEVE_SAVED_CONFIG, TN_VALIDATE, TN_STATELESS_WAIT_FOR_HP, DETACH_TNP, TNP_WAIT, TN_SEND_HS_MIGRATION_MSG, TN_ADD_HOST_TO_VDS, TN_UPDATE, TN_UPDATE_WAIT, TN_DELETE, TN_DELETE_WAIT, FN_DELETE_WAIT, TN_RECONFIG_HOST, TN_CREATE, TN_CREATE_WAIT, UPDATE_TNP_AND_APPLY, TN_EXIT_MM, TN_MIGRATION_COMPLETED Depending on the type of host (stateful, stateless, Sddc, etc.) migration task may not cycle through all stages but in will follow above sequence. If stage is TN_MIGRATION_COMPLETED refer to field overall_state for SUCCESS or UPGRADE_FAILURE and state_details for details on same.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

