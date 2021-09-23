# IPSecVPNDPDProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_count** | **int** | Maximum number of DPD messages retry attempts. This value is applicable for both dpd probe modes, periodic and on-demand. | [optional] [default to 5]
**enabled** | **bool** | If true, enable dead peer detection. | [optional] [default to True]
**dpd_probe_mode** | **str** | DPD probe mode is used to query the liveliness of the peer. Two modes are possible - PERIODIC - is used to query the liveliness of the peer at regular intervals (dpd_probe_interval). It does not take into consideration traffic coming from the peer. The benefit of this mode over the on-demand mode is earlier detection of dead peers. However, use of periodic DPD incurs extra overhead. When communicating to large numbers of peers, please consider using on-demand DPD instead. ON_DEMAND - is used to query the liveliness of the peer by instructing the local endpoint to send DPD message to a peer if there is traffic to send to the peer AND the peer was idle for dpd_probe_interval seconds (i.e. there was no traffic from the peer for dpd_probe_interval seconds)  | [optional] [default to 'PERIODIC']
**dpd_probe_interval** | **int** | When the DPD probe mode is periodic, this interval is the number of seconds between DPD messages. When the DPD probe mode is on-demand, this interval is the number of seconds during which traffic is not received from the peer before DPD retry messages are sent if there is IPSec traffic to send. For PERIODIC Mode:    Minimum: 3    Maximum: 360    Default: 60 For ON_DEMAND Mode:    Minimum: 1    Maximum: 10    Default: 3  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

