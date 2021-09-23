# IntelligenceHostConfigurationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_inactive_flow_count** | **int** | Maximum inactive network flow to collect in collection interval.  | [optional] [default to 50000]
**context_data_collection_interval** | **int** | Interval in minute of reporting VM guest context data to NSX-Intelligence. Recommend to keep this value the same as flow_data_collection_interval.  | [optional] [default to 5]
**broker_truststore** | **str** | A truststore to establish the trust between NSX and NSX-Intelligence brokers.  | [optional] 
**flow_data_collection_interval** | **int** | Interval in minute of reporting network flow data to NSX-Intelligence. Recommend to keep this value the same as context_data_collection_interval.  | [optional] [default to 5]
**broker_certificate** | **str** | A broker certificate to verify the identity of brokers.  | [optional] 
**context_user_sids** | **list[str]** | List of windows user sid to collect context data. Empty implies all users.  | [optional] 
**enable_context_data_collection** | **bool** | Enable NSX-Intelligence context data collection in host nodes.  | [optional] [default to True]
**context_user_uids** | **list[str]** | List of linux user uid to collect context data. Empty implies all users.  | [optional] 
**enable_flow_data_collection** | **bool** | Enable NSX-Intelligence flow data collection in host nodes.  | [optional] [default to True]
**enable_deep_packet_inspection** | **bool** | Enable NSX-Intelligence deep packet inspection in host nodes.  | [optional] [default to True]
**context_process_hashes** | **list[str]** | List of hashes of processes to collect context data. Empty implies all processes.  | [optional] 
**enable_data_collection** | **bool** | Enable NSX-Intelligence data collection in host nodes.  This property has been deprecated. To enable flow data collection, use property enable_flow_data_collection instead. To enable context data collection, use property enable_context_data_collection instead.  When this property is set to false, no data collection is performed even if enable_flow_data_collection or enable_context_data_collection is set to true.  When this property is set to true, property enable_flow_data_collection and enable_context_data_collection control whether to collect flow data and context data separately.  | [optional] [default to True]
**private_ip_prefix** | [**list[IntelligenceFlowPrivateIpPrefixInfo]**](IntelligenceFlowPrivateIpPrefixInfo.md) | List of private IP prefix that NSX-Intelligence network flow is collected from.  | [optional] 
**broker_bootstrap_servers** | [**list[IntelligenceBrokerEndpointInfo]**](IntelligenceBrokerEndpointInfo.md) | List of NSX-Intelligence broker endpoints that host nodes contact initially.  | [optional] 
**max_inactive_flow_count_bm** | **int** | Maximum inactive network flow to collect in collection interval for Bare Metal server.  | [optional] [default to 25000]
**max_active_flow_count_bm** | **int** | Maximum active network flow to collect in collection interval for Bare Metal server.  | [optional] [default to 12500]
**context_process_names** | **list[str]** | List of processes to collect context data. Empty implies all processes.  | [optional] 
**max_active_flow_count** | **int** | Maximum active network flow to collect in collection interval.  | [optional] [default to 25000]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

