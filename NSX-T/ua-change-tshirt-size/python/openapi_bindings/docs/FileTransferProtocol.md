# FileTransferProtocol

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_name** | **str** | Protocol name | [default to 'sftp']
**ssh_fingerprint** | **str** | The expected SSH fingerprint of the server. If the server&#x27;s fingerprint does not match this fingerprint, the connection will be terminated.  Only ECDSA fingerprints hashed with SHA256 are supported. To obtain the host&#x27;s ssh fingerprint, you should connect via some method other than SSH to obtain this information. You can use one of these commands to view the key&#x27;s fingerprint: 1. ssh-keygen -l -E sha256 -f ssh_host_ecdsa_key.pub 2. awk &#x27;{print $2}&#x27; ssh_host_ecdsa_key.pub | base64 -d | sha256sum -b |    sed &#x27;s/ .*$//&#x27; | xxd -r -p | base64 | sed &#x27;s/.//44g&#x27; |    awk &#x27;{print \&quot;SHA256:\&quot;$1}&#x27;  | 
**authentication_scheme** | [**FileTransferAuthenticationScheme**](FileTransferAuthenticationScheme.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

