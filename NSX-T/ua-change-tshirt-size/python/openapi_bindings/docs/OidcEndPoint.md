# OidcEndPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userinfo_endpoint** | **str** | The URL of the OpenID provider&#x27;s userinfo endpoint. | [optional] 
**claims_supported** | **list[str]** | The list of claims that the OpenID provider supports. | [optional] 
**name** | **str** | A short, unique name for this OpenID Connect end-point. OIDC endpoint names may not contain spaces. If not provided, defaults to the ID of the OidcEndPoint. | [optional] 
**oidc_type** | **str** | Type used to distinguish the OIDC end-points by IDP. | [optional] 
**oidc_uri** | **str** | URI of the OpenID Connect end-point. | 
**token_endpoint** | **str** | The URL of the OpenID provider&#x27;s token endpoint. | [optional] 
**thumbprint** | **str** | Thumbprint in SHA-256 format used to verify the server certificate at the URI.  | 
**jwks_uri** | **str** | The URI where the JWKS document is located that has the key used to validate the JWT signature.  | [optional] 
**authorization_endpoint** | **str** | The URL of the OpenID provider&#x27;s authorization endpoint. | [optional] 
**override_roles** | **list[str]** | When specified this role or roles are used instead of the nsx-role in the JWT | [optional] 
**issuer** | **str** | Issuer of the JWT tokens for the given type. This field is fetched from the meta-data located at the oidc_uri.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

