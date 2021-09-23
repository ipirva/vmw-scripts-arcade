# MetadataProxy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | secret to access metadata server | [optional] 
**metadata_server_ca_ids** | **list[str]** | The CAs referenced here must be uploaded to the truststore using the API POST /api/v1/trust-management/certificates?action&#x3D;import. User needs to ensure a correct CA for this metedata server is used. The REST API can not detect a wrong CA which was used to verify a different server. If the Metadata Proxy reports an ERROR or NO_BACKUP status, user can check the metadata proxy log at transport node for a possible CA issue.  | [optional] 
**edge_cluster_member_indexes** | **list[int]** | If none is provided, the NSX will auto-select two edge-nodes from the given edge cluster. If user provides only one edge node, there will be no HA support.  | [optional] 
**crypto_protocols** | **list[str]** | The cryptographic protocols listed here are supported by the metadata proxy. The TLSv1.1 and TLSv1.2 are supported by default.  | [optional] 
**metadata_server_url** | **str** | The URL in format scheme://host:port/path. Please note, the scheme supports only http and https as of now, port supports range 3000 - 9000, inclusive.  | 
**attached_logical_port_id** | **str** | id of attached logical port | [optional] 
**enable_standby_relocation** | **bool** | Flag to enable the auto-relocation of standby Metadata Proxy in case of edge node failure. Only tier 1 and auto placed Metadata Proxy are considered for the relocation.  | [optional] [default to False]
**edge_cluster_id** | **str** | edge cluster uuid | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

