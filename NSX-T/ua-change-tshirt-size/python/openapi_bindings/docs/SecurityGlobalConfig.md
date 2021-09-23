# SecurityGlobalConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eku_checking_enabled** | **bool** | When this flag is set to true, during certificate checking the Extended Key Usage extension is expected to be present, indicating whether the certificate is to be used a client certificate or server certificate. Setting this value to false is not recommended as it leads to lower security and operational risk. | [optional] [default to True]
**ca_signed_only** | **bool** | When this flag is set to true (for NDcPP compliance) only ca-signed certificates will be allowed to be applied as server certificates. | [optional] [default to False]
**crl_checking_enabled** | **bool** | When this flag is set to true, during certificate checking the CRL is fetched and checked whether the certificate is revoked or not. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

