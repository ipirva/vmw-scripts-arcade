# IdsEventFlowData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip** | **str** | IP address of the destination VM on the intrusion flow. | [optional] 
**protocol** | **str** | Traffic protocol pertaining to the detected intrusion, could be TCP/UDP etc. | [optional] 
**bytes_toserver** | **int** | Bytes sent to server. | [optional] 
**local_vm_ip** | **str** | IP address of VM on the host where IDS engine is running. | [optional] 
**profile_id** | **str** | The IDS profile id that is associated with the IDS rule pertaining to the intrusion event detected. | [optional] 
**source_ip** | **str** | IP address of the source VM on the intrusion flow. | [optional] 
**client_ip** | **str** | IP address of the VM that initiated the communication. | [optional] 
**action_type** | **str** | The action pertaining to the detected intrusion. Possible values are ALERT, DROP, REJECT, and INVALID. ALERT - If there is a signature match on the packet, it is allowed to pass but a notification is sent to the user notifying an intrusion was detected. DROP - On a signature match, the packet is silently dropped. An alert is sent to the user that an intrusion was detected. REJECT - On a signature match, the packet is dropped and TCP RST or ICMP error messages (for non-TCP pkts) are sent to the endpoints. An alert is sent to the user that an intrusion was detected. INVALID - If the action doesn&#x27;t belong to any of the above mentioned categories, it is marked as INVALID. | [optional] 
**source_port** | **int** | Source port through which traffic was initiated that caused the intrusion to be detected. | [optional] 
**bytes_toclient** | **int** | Bytes sent to client. | [optional] 
**destination_port** | **int** | Port on the destination VM where the traffic was sent to. | [optional] 
**rule_id** | **int** | The IDS Rule id pertaining to the detected intrusion. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

