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

class SVMDeploymentSpec(object):
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
        'ovf_url': 'str',
        'name': 'str',
        'min_host_version': 'str',
        'service_form_factor': 'str',
        'host_type': 'str',
        'svm_version': 'str'
    }

    attribute_map = {
        'ovf_url': 'ovf_url',
        'name': 'name',
        'min_host_version': 'min_host_version',
        'service_form_factor': 'service_form_factor',
        'host_type': 'host_type',
        'svm_version': 'svm_version'
    }

    def __init__(self, ovf_url=None, name=None, min_host_version='6.5', service_form_factor='MEDIUM', host_type=None, svm_version='1.0'):  # noqa: E501
        """SVMDeploymentSpec - a model defined in Swagger"""  # noqa: E501
        self._ovf_url = None
        self._name = None
        self._min_host_version = None
        self._service_form_factor = None
        self._host_type = None
        self._svm_version = None
        self.discriminator = None
        self.ovf_url = ovf_url
        if name is not None:
            self.name = name
        if min_host_version is not None:
            self.min_host_version = min_host_version
        if service_form_factor is not None:
            self.service_form_factor = service_form_factor
        self.host_type = host_type
        if svm_version is not None:
            self.svm_version = svm_version

    @property
    def ovf_url(self):
        """Gets the ovf_url of this SVMDeploymentSpec.  # noqa: E501

        Location of the partner VM OVF to be deployed.  # noqa: E501

        :return: The ovf_url of this SVMDeploymentSpec.  # noqa: E501
        :rtype: str
        """
        return self._ovf_url

    @ovf_url.setter
    def ovf_url(self, ovf_url):
        """Sets the ovf_url of this SVMDeploymentSpec.

        Location of the partner VM OVF to be deployed.  # noqa: E501

        :param ovf_url: The ovf_url of this SVMDeploymentSpec.  # noqa: E501
        :type: str
        """
        if ovf_url is None:
            raise ValueError("Invalid value for `ovf_url`, must not be `None`")  # noqa: E501

        self._ovf_url = ovf_url

    @property
    def name(self):
        """Gets the name of this SVMDeploymentSpec.  # noqa: E501

        Deployment Spec name for ease of use, since multiple DeploymentSpec can be specified.  # noqa: E501

        :return: The name of this SVMDeploymentSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SVMDeploymentSpec.

        Deployment Spec name for ease of use, since multiple DeploymentSpec can be specified.  # noqa: E501

        :param name: The name of this SVMDeploymentSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def min_host_version(self):
        """Gets the min_host_version of this SVMDeploymentSpec.  # noqa: E501

        Minimum host version supported by this ovf. If a host in the deployment cluster is having version less than this, then service deployment will not happen on that host.  # noqa: E501

        :return: The min_host_version of this SVMDeploymentSpec.  # noqa: E501
        :rtype: str
        """
        return self._min_host_version

    @min_host_version.setter
    def min_host_version(self, min_host_version):
        """Sets the min_host_version of this SVMDeploymentSpec.

        Minimum host version supported by this ovf. If a host in the deployment cluster is having version less than this, then service deployment will not happen on that host.  # noqa: E501

        :param min_host_version: The min_host_version of this SVMDeploymentSpec.  # noqa: E501
        :type: str
        """

        self._min_host_version = min_host_version

    @property
    def service_form_factor(self):
        """Gets the service_form_factor of this SVMDeploymentSpec.  # noqa: E501

        Supported ServiceInsertion Form Factor for the OVF deployment. The default FormFactor is Medium.  # noqa: E501

        :return: The service_form_factor of this SVMDeploymentSpec.  # noqa: E501
        :rtype: str
        """
        return self._service_form_factor

    @service_form_factor.setter
    def service_form_factor(self, service_form_factor):
        """Sets the service_form_factor of this SVMDeploymentSpec.

        Supported ServiceInsertion Form Factor for the OVF deployment. The default FormFactor is Medium.  # noqa: E501

        :param service_form_factor: The service_form_factor of this SVMDeploymentSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["SMALL", "MEDIUM", "LARGE"]  # noqa: E501
        if service_form_factor not in allowed_values:
            raise ValueError(
                "Invalid value for `service_form_factor` ({0}), must be one of {1}"  # noqa: E501
                .format(service_form_factor, allowed_values)
            )

        self._service_form_factor = service_form_factor

    @property
    def host_type(self):
        """Gets the host_type of this SVMDeploymentSpec.  # noqa: E501

        Host Type on which the specified OVF can be deployed.  # noqa: E501

        :return: The host_type of this SVMDeploymentSpec.  # noqa: E501
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this SVMDeploymentSpec.

        Host Type on which the specified OVF can be deployed.  # noqa: E501

        :param host_type: The host_type of this SVMDeploymentSpec.  # noqa: E501
        :type: str
        """
        if host_type is None:
            raise ValueError("Invalid value for `host_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ESXI", "RHELKVM", "UBUNTUKVM"]  # noqa: E501
        if host_type not in allowed_values:
            raise ValueError(
                "Invalid value for `host_type` ({0}), must be one of {1}"  # noqa: E501
                .format(host_type, allowed_values)
            )

        self._host_type = host_type

    @property
    def svm_version(self):
        """Gets the svm_version of this SVMDeploymentSpec.  # noqa: E501

        Partner needs to specify the Service VM version which will get deployed.  # noqa: E501

        :return: The svm_version of this SVMDeploymentSpec.  # noqa: E501
        :rtype: str
        """
        return self._svm_version

    @svm_version.setter
    def svm_version(self, svm_version):
        """Sets the svm_version of this SVMDeploymentSpec.

        Partner needs to specify the Service VM version which will get deployed.  # noqa: E501

        :param svm_version: The svm_version of this SVMDeploymentSpec.  # noqa: E501
        :type: str
        """

        self._svm_version = svm_version

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
        if issubclass(SVMDeploymentSpec, dict):
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
        if not isinstance(other, SVMDeploymentSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
