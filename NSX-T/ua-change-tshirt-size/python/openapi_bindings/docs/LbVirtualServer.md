# LbVirtualServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_list_control** | [**LbAccessListControl**](LbAccessListControl.md) |  | [optional] 
**ip_protocol** | **str** | Assigned Internet Protocol in IP header, TCP, UDP are supported.  | [optional] [default to 'TCP']
**log_significant_event_only** | **bool** | The property log_significant_event_only can take effect only when access_log_enabled is true. If log_significant_event_only is true, significant events are logged in access log. For L4 virtual server, significant event means unsuccessful(error or dropped) TCP/UDP connections. For L7 virtual server, significant event means unsuccessful connections or HTTP/HTTPS requests which have error response code(e.g. 4xx, 5xx).  | [optional] [default to False]
**default_pool_member_ports** | **list[str]** | If default_pool_member_ports are configured, both default_pool_member_port and default_pool_member_ports in the response payload would include port settings, notice that the value of default_pool_member_port is the first element of default_pool_member_ports.  | [optional] 
**persistence_profile_id** | **str** | Persistence profile is used to allow related client connections to be sent to the same backend server.  | [optional] 
**server_ssl_profile_binding** | [**ServerSslProfileBinding**](ServerSslProfileBinding.md) |  | [optional] 
**application_profile_id** | **str** | The application profile defines the application protocol characteristics. It is used to influence how load balancing is performed. Currently, LbFastTCPProfile, LbFastUDPProfile and LbHttpProfile, etc are supported.  | 
**pool_id** | **str** | The server pool(LbPool) contains backend servers. Server pool consists of one or more servers, also referred to as pool members, that are similarly configured and are running the same application.  | [optional] 
**access_log_enabled** | **bool** | Whether access log is enabled | [optional] [default to False]
**max_concurrent_connections** | **int** | To ensure one virtual server does not over consume resources, affecting other applications hosted on the same LBS, connections to a virtual server can be capped. If it is not specified, it means that connections are unlimited.  | [optional] 
**rule_ids** | **list[str]** | Load balancer rules allow customization of load balancing behavior using match/action rules. Currently, load balancer rules are supported for only layer 7 virtual servers with LbHttpProfile.  | [optional] 
**max_new_connection_rate** | **int** | To ensure one virtual server does not over consume resources, connections to a member can be rate limited. If it is not specified, it means that connection rate is unlimited.  | [optional] 
**sorry_pool_id** | **str** | When load balancer can not select a backend server to serve the request in default pool or pool in rules, the request would be served by sorry server pool.  | [optional] 
**client_ssl_profile_binding** | [**ClientSslProfileBinding**](ClientSslProfileBinding.md) |  | [optional] 
**default_pool_member_port** | **str** | This is a deprecated property, please use &#x27;default_pool_member_ports&#x27; instead. If default_pool_member_port is configured and default_pool_member_ports are not specified, both default_pool_member_port and default_pool_member_ports in response payload would return the same port value. If both are specified, default_pool_member_ports setting would take effect with higher priority.  | [optional] 
**ip_address** | **str** | virtual server IP address | 
**port** | **str** | This is a deprecated property, please use &#x27;ports&#x27; instead. Port setting could be single port for both L7 mode and L4 mode. For L4 mode, a single port range is also supported. The port setting could be a single port or port range such as \&quot;80\&quot;, \&quot;1234-1236\&quot;. If port is configured and ports are not specified, both port and ports in response payload would return the same port value. If both port and ports are configured, ports setting would take effect with higher priority.  | [optional] 
**enabled** | **bool** | whether the virtual server is enabled | [optional] [default to True]
**ports** | **list[str]** | Port setting could be a single port for both L7 mode and L4 mode. For L4 mode, multiple ports or port ranges are also supported such as \&quot;80\&quot;, \&quot;443\&quot;, \&quot;1234-1236\&quot;. If ports is configured, both port and ports in the response payload would include port settings, notice that the port field value is the first element of ports.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

