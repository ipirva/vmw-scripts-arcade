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

class JoinClusterParameters(object):
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
        'username': 'str',
        'certficate_sha256_thumbprint': 'str',
        'token': 'str',
        'cluster_id': 'str',
        'password': 'str',
        'ip_address': 'str',
        'port': 'int'
    }

    attribute_map = {
        'username': 'username',
        'certficate_sha256_thumbprint': 'certficate_sha256_thumbprint',
        'token': 'token',
        'cluster_id': 'cluster_id',
        'password': 'password',
        'ip_address': 'ip_address',
        'port': 'port'
    }

    def __init__(self, username=None, certficate_sha256_thumbprint=None, token=None, cluster_id=None, password=None, ip_address=None, port=443):  # noqa: E501
        """JoinClusterParameters - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._certficate_sha256_thumbprint = None
        self._token = None
        self._cluster_id = None
        self._password = None
        self._ip_address = None
        self._port = None
        self.discriminator = None
        if username is not None:
            self.username = username
        self.certficate_sha256_thumbprint = certficate_sha256_thumbprint
        if token is not None:
            self.token = token
        self.cluster_id = cluster_id
        if password is not None:
            self.password = password
        self.ip_address = ip_address
        if port is not None:
            self.port = port

    @property
    def username(self):
        """Gets the username of this JoinClusterParameters.  # noqa: E501

        Username on the cluster node  # noqa: E501

        :return: The username of this JoinClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this JoinClusterParameters.

        Username on the cluster node  # noqa: E501

        :param username: The username of this JoinClusterParameters.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def certficate_sha256_thumbprint(self):
        """Gets the certficate_sha256_thumbprint of this JoinClusterParameters.  # noqa: E501

        SHA256 Thumbprint of the API certificate of the cluster node  # noqa: E501

        :return: The certficate_sha256_thumbprint of this JoinClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._certficate_sha256_thumbprint

    @certficate_sha256_thumbprint.setter
    def certficate_sha256_thumbprint(self, certficate_sha256_thumbprint):
        """Sets the certficate_sha256_thumbprint of this JoinClusterParameters.

        SHA256 Thumbprint of the API certificate of the cluster node  # noqa: E501

        :param certficate_sha256_thumbprint: The certficate_sha256_thumbprint of this JoinClusterParameters.  # noqa: E501
        :type: str
        """
        if certficate_sha256_thumbprint is None:
            raise ValueError("Invalid value for `certficate_sha256_thumbprint`, must not be `None`")  # noqa: E501

        self._certficate_sha256_thumbprint = certficate_sha256_thumbprint

    @property
    def token(self):
        """Gets the token of this JoinClusterParameters.  # noqa: E501

        Limited time OAuth token instead of the username/password  # noqa: E501

        :return: The token of this JoinClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this JoinClusterParameters.

        Limited time OAuth token instead of the username/password  # noqa: E501

        :param token: The token of this JoinClusterParameters.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def cluster_id(self):
        """Gets the cluster_id of this JoinClusterParameters.  # noqa: E501

        UUID of the cluster to join  # noqa: E501

        :return: The cluster_id of this JoinClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this JoinClusterParameters.

        UUID of the cluster to join  # noqa: E501

        :param cluster_id: The cluster_id of this JoinClusterParameters.  # noqa: E501
        :type: str
        """
        if cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def password(self):
        """Gets the password of this JoinClusterParameters.  # noqa: E501

        Password of the user on the cluster node  # noqa: E501

        :return: The password of this JoinClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this JoinClusterParameters.

        Password of the user on the cluster node  # noqa: E501

        :param password: The password of this JoinClusterParameters.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def ip_address(self):
        """Gets the ip_address of this JoinClusterParameters.  # noqa: E501

        IP address of a node already part of the cluster to join  # noqa: E501

        :return: The ip_address of this JoinClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this JoinClusterParameters.

        IP address of a node already part of the cluster to join  # noqa: E501

        :param ip_address: The ip_address of this JoinClusterParameters.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def port(self):
        """Gets the port of this JoinClusterParameters.  # noqa: E501

        API port on the cluster node  # noqa: E501

        :return: The port of this JoinClusterParameters.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this JoinClusterParameters.

        API port on the cluster node  # noqa: E501

        :param port: The port of this JoinClusterParameters.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if issubclass(JoinClusterParameters, dict):
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
        if not isinstance(other, JoinClusterParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other