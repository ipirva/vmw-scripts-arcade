# IPSecVPNTunnelTrafficStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packets_sent_other_error** | **int** | Total number of packets dropped while sending for any reason. | [optional] 
**packets_out** | **int** | Total number of outgoing packets on outbound Security association (SA). | [optional] 
**dropped_packets_out** | **int** | Total number of outgoing packets dropped on outbound security association. | [optional] 
**integrity_failures** | **int** | Total number of packets dropped due to integrity failures. | [optional] 
**nomatching_policy_errors** | **int** | Number of packets dropped because of no matching policy is available. | [optional] 
**sa_mismatch_errors_in** | **int** | Totoal number of security association (SA) mismatch errors on incoming packets. | [optional] 
**peer_subnet** | **str** | Peer subnet to which a tunnel belongs. | [optional] 
**replay_errors** | **int** | Total number of packets dropped due to replay check on that Security association (SA). | [optional] 
**bytes_out** | **int** | Total number of outgoing bytes on outbound Security association (SA). | [optional] 
**local_subnet** | **str** | Local subnet to which a tunnel belongs. | [optional] 
**dropped_packets_in** | **int** | Total number of incoming packets dropped on inbound security association. | [optional] 
**encryption_failures** | **int** | Total number of packets dropped because of failure in encryption. | [optional] 
**sa_mismatch_errors_out** | **int** | Totoal number of security association (SA) mismatch errors on outgoing packets. | [optional] 
**tunnel_down_reason** | **str** | Gives the detailed reason about the tunnel when it is down. If tunnel is UP tunnel down reason will be empty. | [optional] 
**packets_receive_other_error** | **int** | Total number of incoming packets dropped on inbound Security association (SA)(misc). | [optional] 
**bytes_in** | **int** | Total number of incoming bytes on inbound Security association (SA). | [optional] 
**decryption_failures** | **int** | Total number of packets dropped due to decryption failures. | [optional] 
**seq_number_overflow_error** | **int** | Total number of packets dropped while sending due to overflow in sequence number. | [optional] 
**packets_in** | **int** | Total number of incoming packets on inbound Security association (SA). | [optional] 
**tunnel_status** | **str** | Specifies the status of tunnel. If all the SA (Security association) are negotiated then tunnels status will be UP. If negotiation fails for the SAs status will be DOWN, if SAs are in negotiating phase tunnels status will be NEGOTIATING. | [optional] 
**policy_id** | **str** | Policy UUID of IPSec Tunnel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

