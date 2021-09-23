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

class SecurityCertificate(object):
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
        'text': 'str',
        'valid_from': 'str',
        'ssh_public_key': 'str',
        'valid_to': 'str',
        'pem_encoded': 'str'
    }

    attribute_map = {
        'text': 'text',
        'valid_from': 'valid_from',
        'ssh_public_key': 'ssh_public_key',
        'valid_to': 'valid_to',
        'pem_encoded': 'pem_encoded'
    }

    def __init__(self, text=None, valid_from=None, ssh_public_key=None, valid_to=None, pem_encoded=None):  # noqa: E501
        """SecurityCertificate - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._valid_from = None
        self._ssh_public_key = None
        self._valid_to = None
        self._pem_encoded = None
        self.discriminator = None
        if text is not None:
            self.text = text
        if valid_from is not None:
            self.valid_from = valid_from
        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key
        if valid_to is not None:
            self.valid_to = valid_to
        self.pem_encoded = pem_encoded

    @property
    def text(self):
        """Gets the text of this SecurityCertificate.  # noqa: E501

        X.509 certificate in text form  # noqa: E501

        :return: The text of this SecurityCertificate.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SecurityCertificate.

        X.509 certificate in text form  # noqa: E501

        :param text: The text of this SecurityCertificate.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def valid_from(self):
        """Gets the valid_from of this SecurityCertificate.  # noqa: E501

        The time when the certificate starts being valid  # noqa: E501

        :return: The valid_from of this SecurityCertificate.  # noqa: E501
        :rtype: str
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this SecurityCertificate.

        The time when the certificate starts being valid  # noqa: E501

        :param valid_from: The valid_from of this SecurityCertificate.  # noqa: E501
        :type: str
        """

        self._valid_from = valid_from

    @property
    def ssh_public_key(self):
        """Gets the ssh_public_key of this SecurityCertificate.  # noqa: E501


        :return: The ssh_public_key of this SecurityCertificate.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """Sets the ssh_public_key of this SecurityCertificate.


        :param ssh_public_key: The ssh_public_key of this SecurityCertificate.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

    @property
    def valid_to(self):
        """Gets the valid_to of this SecurityCertificate.  # noqa: E501

        The time when the certificate stops being valid  # noqa: E501

        :return: The valid_to of this SecurityCertificate.  # noqa: E501
        :rtype: str
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this SecurityCertificate.

        The time when the certificate stops being valid  # noqa: E501

        :param valid_to: The valid_to of this SecurityCertificate.  # noqa: E501
        :type: str
        """

        self._valid_to = valid_to

    @property
    def pem_encoded(self):
        """Gets the pem_encoded of this SecurityCertificate.  # noqa: E501

        The certificate must include the enclosing \"-----BEGIN CERTIFICATE-----\" and \"-----END CERTIFICATE-----\"  # noqa: E501

        :return: The pem_encoded of this SecurityCertificate.  # noqa: E501
        :rtype: str
        """
        return self._pem_encoded

    @pem_encoded.setter
    def pem_encoded(self, pem_encoded):
        """Sets the pem_encoded of this SecurityCertificate.

        The certificate must include the enclosing \"-----BEGIN CERTIFICATE-----\" and \"-----END CERTIFICATE-----\"  # noqa: E501

        :param pem_encoded: The pem_encoded of this SecurityCertificate.  # noqa: E501
        :type: str
        """
        if pem_encoded is None:
            raise ValueError("Invalid value for `pem_encoded`, must not be `None`")  # noqa: E501

        self._pem_encoded = pem_encoded

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
        if issubclass(SecurityCertificate, dict):
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
        if not isinstance(other, SecurityCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
