# DnsFailedQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_spent** | **int** | The time the query took before it got a failed answer, in ms. | [optional] 
**record_type** | **str** | The record type be queried, e.g. A, CNAME, SOA, etc. | [optional] 
**client_ip** | **str** | The client host ip address from which the query was issued.  | [optional] 
**upstream_server_ip** | **str** | The upstream server ip address to which the query was forwarded. If the query could not be serviced from the DNS forwarder cache, this property will contain the IP address of the DNS server that serviced the request. If the request was serviced from the cache, this property will be absent.  | [optional] 
**error_message** | **str** | The detailed error message of the failed query, if any. | [optional] 
**address** | **str** | The address be queried, can be a FQDN or an ip address. | [optional] 
**timestamp** | **str** | Timestamp of the request, in YYYY-MM-DD HH:MM:SS.zzz format. | 
**error_type** | **str** | The type of the query failure, e.g. NXDOMAIN, etc. | [optional] 
**source_ip** | **str** | The source ip address that is used to forward a query to an upstream server.  | [optional] 
**forwarder_ip** | **str** | The DNS forwarder ip address to which the query was first received.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

