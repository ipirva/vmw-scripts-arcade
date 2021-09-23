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
from swagger_client.models.resource import Resource  # noqa: F401,E501

class MPAConfigProperties(Resource):
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
        'rmq_client_type': 'object',
        'rmq_broker_cluster': 'list[BrokerProperties]',
        'shared_secret': 'str',
        'account_name': 'object'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'rmq_client_type': 'RmqClientType',
        'rmq_broker_cluster': 'RmqBrokerCluster',
        'shared_secret': 'SharedSecret',
        'account_name': 'AccountName'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, rmq_client_type=None, rmq_broker_cluster=None, shared_secret=None, account_name=None, *args, **kwargs):  # noqa: E501
        """MPAConfigProperties - a model defined in Swagger"""  # noqa: E501
        self._rmq_client_type = None
        self._rmq_broker_cluster = None
        self._shared_secret = None
        self._account_name = None
        self.discriminator = None
        if rmq_client_type is not None:
            self.rmq_client_type = rmq_client_type
        if rmq_broker_cluster is not None:
            self.rmq_broker_cluster = rmq_broker_cluster
        if shared_secret is not None:
            self.shared_secret = shared_secret
        if account_name is not None:
            self.account_name = account_name
        Resource.__init__(self, *args, **kwargs)

    @property
    def rmq_client_type(self):
        """Gets the rmq_client_type of this MPAConfigProperties.  # noqa: E501

        The nodes client type.  # noqa: E501

        :return: The rmq_client_type of this MPAConfigProperties.  # noqa: E501
        :rtype: object
        """
        return self._rmq_client_type

    @rmq_client_type.setter
    def rmq_client_type(self, rmq_client_type):
        """Sets the rmq_client_type of this MPAConfigProperties.

        The nodes client type.  # noqa: E501

        :param rmq_client_type: The rmq_client_type of this MPAConfigProperties.  # noqa: E501
        :type: object
        """

        self._rmq_client_type = rmq_client_type

    @property
    def rmq_broker_cluster(self):
        """Gets the rmq_broker_cluster of this MPAConfigProperties.  # noqa: E501

        The list of messaging brokers this controller is configured with.  # noqa: E501

        :return: The rmq_broker_cluster of this MPAConfigProperties.  # noqa: E501
        :rtype: list[BrokerProperties]
        """
        return self._rmq_broker_cluster

    @rmq_broker_cluster.setter
    def rmq_broker_cluster(self, rmq_broker_cluster):
        """Sets the rmq_broker_cluster of this MPAConfigProperties.

        The list of messaging brokers this controller is configured with.  # noqa: E501

        :param rmq_broker_cluster: The rmq_broker_cluster of this MPAConfigProperties.  # noqa: E501
        :type: list[BrokerProperties]
        """

        self._rmq_broker_cluster = rmq_broker_cluster

    @property
    def shared_secret(self):
        """Gets the shared_secret of this MPAConfigProperties.  # noqa: E501

        The shared secret to use when autnenticating to the management plane's message bus. Not returned in REST responses.  # noqa: E501

        :return: The shared_secret of this MPAConfigProperties.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this MPAConfigProperties.

        The shared secret to use when autnenticating to the management plane's message bus. Not returned in REST responses.  # noqa: E501

        :param shared_secret: The shared_secret of this MPAConfigProperties.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

    @property
    def account_name(self):
        """Gets the account_name of this MPAConfigProperties.  # noqa: E501

        The account name to use when authenticating to the management plane's message bus.  # noqa: E501

        :return: The account_name of this MPAConfigProperties.  # noqa: E501
        :rtype: object
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this MPAConfigProperties.

        The account name to use when authenticating to the management plane's message bus.  # noqa: E501

        :param account_name: The account_name of this MPAConfigProperties.  # noqa: E501
        :type: object
        """

        self._account_name = account_name

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
        if issubclass(MPAConfigProperties, dict):
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
        if not isinstance(other, MPAConfigProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other