# FirewallFloodProtectionProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icmp_active_flow_limit** | **int** | The maximum limit of active icmp connections. If this property is omitted, or set to null, then there is no limit on active icmp connections for those components if it&#x27;s applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it&#x27;s applied to EDGE components (such as, gateway), it will be set to default limit (10,000) on the specific components. | [optional] 
**other_active_conn_limit** | **int** | The maximum limit of other active connections besides udp, icmp and half open tcp connections. If this property is omitted, or set to null, then there is no limit on other active connections besides udp, icmp and tcp half open connections for those components if it&#x27;s applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it&#x27;s applied to EDGE components (such as, gateway), it will be set to default limit (10,000) on the specific components. | [optional] 
**enable_syncache** | **bool** | The flag to indicate syncache is enabled or not. This option does not apply to EDGE components. | [optional] [default to False]
**enable_rst_spoofing** | **bool** | The flag to indicate RST spoofing is enabled or not. This option does not apply to EDGE components. This can be enabled only if syncache is enabled. | [optional] [default to False]
**tcp_half_open_conn_limit** | **int** | The maximum limit of tcp half open connections. If this property is omitted, or set to null, then there is no limit on active tcp half open connections for those components if it&#x27;s applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it&#x27;s applied to EDGE components (such as, gateway), it will be set to default limit (1,000,000) on the specific components. | [optional] 
**udp_active_flow_limit** | **int** | The maximum limit of active udp connections. If this property is omitted, or set to null, then there is no limit on active udp connections for those components if it&#x27;s applied to ESX components (such as segment, segment port, virtual machine, etc); on the other side, if it&#x27;s applied to EDGE components (such as, gateway), it will be set to default limit (100,000) on the specific component. | [optional] 
**nat_active_conn_limit** | **int** | The maximum limit of active NAT connections. This limit only apply to EDGE components (such as, gateway). If this property is omitted, or set to null, then there is no limit on the specific component. Meanwhile there is an implicit limit which depends on the underlying hardware resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

