# AdvertisementConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_nsx_connected_routes** | **bool** | Flag to advertise all connected routes | [optional] [default to False]
**advertise_lb_vip** | **bool** | Flag to advertise lb vip ips | [optional] [default to False]
**advertise_static_routes** | **bool** | Flag to advertise all static routes | [optional] [default to False]
**logical_router_id** | **str** | TIER1 logical router id on which to enable this configuration | [optional] 
**advertise_dns_forwarder** | **bool** | Flag to advertise all routes of dns forwarder listener ips and source ips | [optional] [default to False]
**advertise_nat_routes** | **bool** | Flag to advertise all routes of nat | [optional] [default to False]
**advertise_ipsec_local_ip** | **bool** | Flag to advertise all IPSec VPN local endpoint ips to linked TIER0 logical router | [optional] [default to False]
**enabled** | **bool** | Flag to enable this configuration | [optional] [default to False]
**advertise_lb_snat_ip** | **bool** | Flag to advertise all lb SNAT ips | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

