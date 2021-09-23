# X509Certificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecdsa_ec_field_f2mks** | **list[int]** | The order of the middle term(s) of the reduction polynomial in elliptic curve (EC) | characteristic 2 finite field.| Contents of this array are copied to protect against subsequent modification in ECDSA. | [optional] 
**version** | **str** | Certificate version (default v1). | [optional] 
**is_ca** | **bool** | True if this is a CA certificate. | [optional] 
**signature_algorithm** | **str** | The algorithm used by the Certificate Authority to sign the certificate. | [optional] 
**ecdsa_public_key_a** | **str** | The first coefficient of this elliptic curve in ECDSA. | [optional] 
**rsa_public_key_exponent** | **str** | An RSA public key is made up of the modulus and the public exponent. Exponent is a power number. | [optional] 
**ecdsa_ec_field_f2mm** | **int** | The first coefficient of this elliptic curve in elliptic curve (EC) | characteristic 2 finite field for ECDSA. | [optional] 
**issuer_cn** | **str** | The certificate issuer&#x27;s common name. | [optional] 
**subject_cn** | **str** | The certificate owner&#x27;s common name. | [optional] 
**ecdsa_public_key_order** | **str** | The order of generator G in ECDSA. | [optional] 
**ecdsa_ec_field_f2mrp** | **str** | The value whose i-th bit corresponds to the i-th coefficient of the reduction polynomial | in elliptic curve (EC) characteristic 2 finite field for ECDSA. | [optional] 
**public_key_length** | **int** | Size measured in bits of the public/private keys used in a cryptographic algorithm. | [optional] 
**not_before** | **int** | The time in epoch milliseconds at which the certificate becomes valid. | [optional] 
**ecdsa_ec_field_f2pp** | **str** | The specified prime for the elliptic curve prime finite field in ECDSA. | [optional] 
**issuer** | **str** | The certificate issuers complete distinguished name. | [optional] 
**ecdsa_public_key_b** | **str** | The second coefficient of this elliptic curve in ECDSA. | [optional] 
**rsa_public_key_modulus** | **str** | An RSA public key is made up of the modulus and the public exponent. Modulus is wrap around number. | [optional] 
**dsa_public_key_y** | **str** | One of the DSA cryptogaphic algorithm&#x27;s strength parameters. | [optional] 
**ecdsa_public_key_cofactor** | **int** | The co-factor in ECDSA. | [optional] 
**not_after** | **int** | The time in epoch milliseconds at which the certificate becomes invalid. | [optional] 
**dsa_public_key_q** | **str** | One of the DSA cryptogaphic algorithm&#x27;s strength parameters, sub-prime. | [optional] 
**dsa_public_key_p** | **str** | One of the DSA cryptogaphic algorithm&#x27;s strength parameters, prime. | [optional] 
**ecdsa_public_key_generator_y** | **str** | Y co-ordinate of G (the generator which is also known as the base point) in ECDSA. | [optional] 
**ecdsa_public_key_generator_x** | **str** | X co-ordinate of G (the generator which is also known as the base point) in ECDSA. | [optional] 
**public_key_algo** | **str** | Cryptographic algorithm used by the public key for data encryption. | [optional] 
**is_valid** | **bool** | True if this certificate is valid. | [optional] 
**ecdsa_public_key_seed** | **list[str]** | The bytes used during curve generation for later validation in ECDSA.| Contents of this array are copied to protect against subsequent modification. | [optional] 
**signature** | **str** | The signature value(the raw signature bits) used for signing and validate the cert. | [optional] 
**serial_number** | **str** | Certificate&#x27;s serial number. | [optional] 
**dsa_public_key_g** | **str** | One of the DSA cryptogaphic algorithm&#x27;s strength parameters, base. | [optional] 
**subject** | **str** | The certificate owners complete distinguished name. | [optional] 
**ecdsa_ec_field** | **str** | Represents an elliptic curve (EC) finite field in ECDSA. | [optional] 
**ecdsa_curve_name** | **str** | The Curve name for the ECDSA certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

