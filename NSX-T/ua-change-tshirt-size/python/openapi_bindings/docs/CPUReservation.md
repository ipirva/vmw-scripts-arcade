# CPUReservation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_in_mhz** | **int** | The CPU reservation in MHz is the guaranteed minimum amount of clock cycles that the vmkernel CPU scheduler will give the Edge VM in case of contention. If an Edge VM is not using its reserved resources, then other machines can use them thus preventing waste of CPU cycles on the physical host. Note: We recommend use of reservation_in_shares instead of this absolute configuration. When you specify this value, set reservation_in_shares to LOW_PRIORITY.  | [optional] 
**reservation_in_shares** | **str** | Shares specify the relative importance of a virtual machine on a given host. When you assign shares to a virtual machine, you always specify the priority for that virtual machine relative to other powered-on virtual machines on the same host. The default priority for shares is HIGH_PRIORITY.  | [optional] [default to 'HIGH_PRIORITY']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

