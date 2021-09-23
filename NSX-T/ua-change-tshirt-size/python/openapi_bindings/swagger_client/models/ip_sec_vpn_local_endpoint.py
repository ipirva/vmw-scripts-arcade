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
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class IPSecVPNLocalEndpoint(ManagedResource):
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
        'ipsec_vpn_service_id': 'ResourceReference',
        'trust_ca_ids': 'list[str]',
        'local_id': 'str',
        'local_address': 'str',
        'certificate_id': 'str',
        'trust_crl_ids': 'list[str]'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'ipsec_vpn_service_id': 'ipsec_vpn_service_id',
        'trust_ca_ids': 'trust_ca_ids',
        'local_id': 'local_id',
        'local_address': 'local_address',
        'certificate_id': 'certificate_id',
        'trust_crl_ids': 'trust_crl_ids'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, ipsec_vpn_service_id=None, trust_ca_ids=None, local_id=None, local_address=None, certificate_id=None, trust_crl_ids=None, *args, **kwargs):  # noqa: E501
        """IPSecVPNLocalEndpoint - a model defined in Swagger"""  # noqa: E501
        self._ipsec_vpn_service_id = None
        self._trust_ca_ids = None
        self._local_id = None
        self._local_address = None
        self._certificate_id = None
        self._trust_crl_ids = None
        self.discriminator = None
        self.ipsec_vpn_service_id = ipsec_vpn_service_id
        if trust_ca_ids is not None:
            self.trust_ca_ids = trust_ca_ids
        if local_id is not None:
            self.local_id = local_id
        self.local_address = local_address
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if trust_crl_ids is not None:
            self.trust_crl_ids = trust_crl_ids
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def ipsec_vpn_service_id(self):
        """Gets the ipsec_vpn_service_id of this IPSecVPNLocalEndpoint.  # noqa: E501


        :return: The ipsec_vpn_service_id of this IPSecVPNLocalEndpoint.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._ipsec_vpn_service_id

    @ipsec_vpn_service_id.setter
    def ipsec_vpn_service_id(self, ipsec_vpn_service_id):
        """Sets the ipsec_vpn_service_id of this IPSecVPNLocalEndpoint.


        :param ipsec_vpn_service_id: The ipsec_vpn_service_id of this IPSecVPNLocalEndpoint.  # noqa: E501
        :type: ResourceReference
        """
        if ipsec_vpn_service_id is None:
            raise ValueError("Invalid value for `ipsec_vpn_service_id`, must not be `None`")  # noqa: E501

        self._ipsec_vpn_service_id = ipsec_vpn_service_id

    @property
    def trust_ca_ids(self):
        """Gets the trust_ca_ids of this IPSecVPNLocalEndpoint.  # noqa: E501

        Certificate authority (CA) identifier list to verify peer certificates.  # noqa: E501

        :return: The trust_ca_ids of this IPSecVPNLocalEndpoint.  # noqa: E501
        :rtype: list[str]
        """
        return self._trust_ca_ids

    @trust_ca_ids.setter
    def trust_ca_ids(self, trust_ca_ids):
        """Sets the trust_ca_ids of this IPSecVPNLocalEndpoint.

        Certificate authority (CA) identifier list to verify peer certificates.  # noqa: E501

        :param trust_ca_ids: The trust_ca_ids of this IPSecVPNLocalEndpoint.  # noqa: E501
        :type: list[str]
        """

        self._trust_ca_ids = trust_ca_ids

    @property
    def local_id(self):
        """Gets the local_id of this IPSecVPNLocalEndpoint.  # noqa: E501

        Local identifier.  # noqa: E501

        :return: The local_id of this IPSecVPNLocalEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this IPSecVPNLocalEndpoint.

        Local identifier.  # noqa: E501

        :param local_id: The local_id of this IPSecVPNLocalEndpoint.  # noqa: E501
        :type: str
        """

        self._local_id = local_id

    @property
    def local_address(self):
        """Gets the local_address of this IPSecVPNLocalEndpoint.  # noqa: E501

        IPV4 Address for local endpoint.  # noqa: E501

        :return: The local_address of this IPSecVPNLocalEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """Sets the local_address of this IPSecVPNLocalEndpoint.

        IPV4 Address for local endpoint.  # noqa: E501

        :param local_address: The local_address of this IPSecVPNLocalEndpoint.  # noqa: E501
        :type: str
        """
        if local_address is None:
            raise ValueError("Invalid value for `local_address`, must not be `None`")  # noqa: E501

        self._local_address = local_address

    @property
    def certificate_id(self):
        """Gets the certificate_id of this IPSecVPNLocalEndpoint.  # noqa: E501

        Site certificate identifier.  # noqa: E501

        :return: The certificate_id of this IPSecVPNLocalEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this IPSecVPNLocalEndpoint.

        Site certificate identifier.  # noqa: E501

        :param certificate_id: The certificate_id of this IPSecVPNLocalEndpoint.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def trust_crl_ids(self):
        """Gets the trust_crl_ids of this IPSecVPNLocalEndpoint.  # noqa: E501

        Certificate revocation list (CRL) identifier list of peer certificates.  # noqa: E501

        :return: The trust_crl_ids of this IPSecVPNLocalEndpoint.  # noqa: E501
        :rtype: list[str]
        """
        return self._trust_crl_ids

    @trust_crl_ids.setter
    def trust_crl_ids(self, trust_crl_ids):
        """Sets the trust_crl_ids of this IPSecVPNLocalEndpoint.

        Certificate revocation list (CRL) identifier list of peer certificates.  # noqa: E501

        :param trust_crl_ids: The trust_crl_ids of this IPSecVPNLocalEndpoint.  # noqa: E501
        :type: list[str]
        """

        self._trust_crl_ids = trust_crl_ids

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
        if issubclass(IPSecVPNLocalEndpoint, dict):
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
        if not isinstance(other, IPSecVPNLocalEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other