# IPSecVPNIKEProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest_algorithms** | **list[str]** | Algorithm to be used for message digest during Internet Key Exchange(IKE) negotiation. Default is SHA2_256. | [optional] 
**encryption_algorithms** | **list[str]** | Encryption algorithm is used during Internet Key Exchange(IKE) negotiation. Default is AES_128. | [optional] 
**dh_groups** | **list[str]** | Diffie-Hellman group to be used if PFS is enabled. Default is GROUP14. | [optional] 
**sa_life_time** | **int** | Life time for security association. Default is 86400 seconds (1 day). | [optional] [default to 86400]
**ike_version** | **str** | IKE protocol version to be used. IKE-Flex will initiate IKE-V2 and responds to both IKE-V1 and IKE-V2. | [optional] [default to 'IKE_V2']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

