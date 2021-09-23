# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 3.1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.lb_rule_condition import LbRuleCondition  # noqa: F401,E501

class LbHttpSslCondition(LbRuleCondition):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_supported_ssl_ciphers': 'list[str]',
        'client_certificate_issuer_dn': 'LbClientCertificateIssuerDnCondition',
        'client_certificate_subject_dn': 'LbClientCertificateSubjectDnCondition',
        'used_ssl_cipher': 'str',
        'session_reused': 'str',
        'used_protocol': 'str'
    }
    if hasattr(LbRuleCondition, "swagger_types"):
        swagger_types.update(LbRuleCondition.swagger_types)

    attribute_map = {
        'client_supported_ssl_ciphers': 'client_supported_ssl_ciphers',
        'client_certificate_issuer_dn': 'client_certificate_issuer_dn',
        'client_certificate_subject_dn': 'client_certificate_subject_dn',
        'used_ssl_cipher': 'used_ssl_cipher',
        'session_reused': 'session_reused',
        'used_protocol': 'used_protocol'
    }
    if hasattr(LbRuleCondition, "attribute_map"):
        attribute_map.update(LbRuleCondition.attribute_map)

    def __init__(self, client_supported_ssl_ciphers=None, client_certificate_issuer_dn=None, client_certificate_subject_dn=None, used_ssl_cipher=None, session_reused='IGNORE', used_protocol=None, *args, **kwargs):  # noqa: E501
        """LbHttpSslCondition - a model defined in Swagger"""  # noqa: E501
        self._client_supported_ssl_ciphers = None
        self._client_certificate_issuer_dn = None
        self._client_certificate_subject_dn = None
        self._used_ssl_cipher = None
        self._session_reused = None
        self._used_protocol = None
        self.discriminator = None
        if client_supported_ssl_ciphers is not None:
            self.client_supported_ssl_ciphers = client_supported_ssl_ciphers
        if client_certificate_issuer_dn is not None:
            self.client_certificate_issuer_dn = client_certificate_issuer_dn
        if client_certificate_subject_dn is not None:
            self.client_certificate_subject_dn = client_certificate_subject_dn
        if used_ssl_cipher is not None:
            self.used_ssl_cipher = used_ssl_cipher
        if session_reused is not None:
            self.session_reused = session_reused
        if used_protocol is not None:
            self.used_protocol = used_protocol
        LbRuleCondition.__init__(self, *args, **kwargs)

    @property
    def client_supported_ssl_ciphers(self):
        """Gets the client_supported_ssl_ciphers of this LbHttpSslCondition.  # noqa: E501

        Cipher list which supported by client  # noqa: E501

        :return: The client_supported_ssl_ciphers of this LbHttpSslCondition.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_supported_ssl_ciphers

    @client_supported_ssl_ciphers.setter
    def client_supported_ssl_ciphers(self, client_supported_ssl_ciphers):
        """Sets the client_supported_ssl_ciphers of this LbHttpSslCondition.

        Cipher list which supported by client  # noqa: E501

        :param client_supported_ssl_ciphers: The client_supported_ssl_ciphers of this LbHttpSslCondition.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384", "TLS_RSA_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_AES_128_GCM_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA256", "TLS_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384"]  # noqa: E501
        if not set(client_supported_ssl_ciphers).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `client_supported_ssl_ciphers` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(client_supported_ssl_ciphers) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._client_supported_ssl_ciphers = client_supported_ssl_ciphers

    @property
    def client_certificate_issuer_dn(self):
        """Gets the client_certificate_issuer_dn of this LbHttpSslCondition.  # noqa: E501


        :return: The client_certificate_issuer_dn of this LbHttpSslCondition.  # noqa: E501
        :rtype: LbClientCertificateIssuerDnCondition
        """
        return self._client_certificate_issuer_dn

    @client_certificate_issuer_dn.setter
    def client_certificate_issuer_dn(self, client_certificate_issuer_dn):
        """Sets the client_certificate_issuer_dn of this LbHttpSslCondition.


        :param client_certificate_issuer_dn: The client_certificate_issuer_dn of this LbHttpSslCondition.  # noqa: E501
        :type: LbClientCertificateIssuerDnCondition
        """

        self._client_certificate_issuer_dn = client_certificate_issuer_dn

    @property
    def client_certificate_subject_dn(self):
        """Gets the client_certificate_subject_dn of this LbHttpSslCondition.  # noqa: E501


        :return: The client_certificate_subject_dn of this LbHttpSslCondition.  # noqa: E501
        :rtype: LbClientCertificateSubjectDnCondition
        """
        return self._client_certificate_subject_dn

    @client_certificate_subject_dn.setter
    def client_certificate_subject_dn(self, client_certificate_subject_dn):
        """Sets the client_certificate_subject_dn of this LbHttpSslCondition.


        :param client_certificate_subject_dn: The client_certificate_subject_dn of this LbHttpSslCondition.  # noqa: E501
        :type: LbClientCertificateSubjectDnCondition
        """

        self._client_certificate_subject_dn = client_certificate_subject_dn

    @property
    def used_ssl_cipher(self):
        """Gets the used_ssl_cipher of this LbHttpSslCondition.  # noqa: E501

        Cipher used for an established SSL connection  # noqa: E501

        :return: The used_ssl_cipher of this LbHttpSslCondition.  # noqa: E501
        :rtype: str
        """
        return self._used_ssl_cipher

    @used_ssl_cipher.setter
    def used_ssl_cipher(self, used_ssl_cipher):
        """Sets the used_ssl_cipher of this LbHttpSslCondition.

        Cipher used for an established SSL connection  # noqa: E501

        :param used_ssl_cipher: The used_ssl_cipher of this LbHttpSslCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_AES_256_CBC_SHA", "TLS_RSA_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384", "TLS_RSA_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_AES_128_GCM_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA256", "TLS_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA", "TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384"]  # noqa: E501
        if used_ssl_cipher not in allowed_values:
            raise ValueError(
                "Invalid value for `used_ssl_cipher` ({0}), must be one of {1}"  # noqa: E501
                .format(used_ssl_cipher, allowed_values)
            )

        self._used_ssl_cipher = used_ssl_cipher

    @property
    def session_reused(self):
        """Gets the session_reused of this LbHttpSslCondition.  # noqa: E501

        The type of SSL session reused  # noqa: E501

        :return: The session_reused of this LbHttpSslCondition.  # noqa: E501
        :rtype: str
        """
        return self._session_reused

    @session_reused.setter
    def session_reused(self, session_reused):
        """Sets the session_reused of this LbHttpSslCondition.

        The type of SSL session reused  # noqa: E501

        :param session_reused: The session_reused of this LbHttpSslCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["IGNORE", "REUSED", "NEW"]  # noqa: E501
        if session_reused not in allowed_values:
            raise ValueError(
                "Invalid value for `session_reused` ({0}), must be one of {1}"  # noqa: E501
                .format(session_reused, allowed_values)
            )

        self._session_reused = session_reused

    @property
    def used_protocol(self):
        """Gets the used_protocol of this LbHttpSslCondition.  # noqa: E501

        Protocol of an established SSL connection  # noqa: E501

        :return: The used_protocol of this LbHttpSslCondition.  # noqa: E501
        :rtype: str
        """
        return self._used_protocol

    @used_protocol.setter
    def used_protocol(self, used_protocol):
        """Sets the used_protocol of this LbHttpSslCondition.

        Protocol of an established SSL connection  # noqa: E501

        :param used_protocol: The used_protocol of this LbHttpSslCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["SSL_V2", "SSL_V3", "TLS_V1", "TLS_V1_1", "TLS_V1_2"]  # noqa: E501
        if used_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `used_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(used_protocol, allowed_values)
            )

        self._used_protocol = used_protocol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LbHttpSslCondition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LbHttpSslCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
