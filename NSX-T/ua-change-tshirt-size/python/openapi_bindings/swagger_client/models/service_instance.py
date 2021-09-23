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
from swagger_client.models.base_service_instance import BaseServiceInstance  # noqa: F401,E501

class ServiceInstance(BaseServiceInstance):
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
        'deployment_spec_name': 'str',
        'instance_deployment_template': 'DeploymentTemplate',
        'implementation_type': 'str',
        'attachment_point': 'str',
        'instance_deployment_config': 'InstanceDeploymentConfig',
        'deployment_mode': 'str',
        'deployed_to': 'list[ResourceReference]',
        'service_deployment_id': 'str'
    }
    if hasattr(BaseServiceInstance, "swagger_types"):
        swagger_types.update(BaseServiceInstance.swagger_types)

    attribute_map = {
        'deployment_spec_name': 'deployment_spec_name',
        'instance_deployment_template': 'instance_deployment_template',
        'implementation_type': 'implementation_type',
        'attachment_point': 'attachment_point',
        'instance_deployment_config': 'instance_deployment_config',
        'deployment_mode': 'deployment_mode',
        'deployed_to': 'deployed_to',
        'service_deployment_id': 'service_deployment_id'
    }
    if hasattr(BaseServiceInstance, "attribute_map"):
        attribute_map.update(BaseServiceInstance.attribute_map)

    def __init__(self, deployment_spec_name=None, instance_deployment_template=None, implementation_type=None, attachment_point=None, instance_deployment_config=None, deployment_mode='ACTIVE_STANDBY', deployed_to=None, service_deployment_id=None, *args, **kwargs):  # noqa: E501
        """ServiceInstance - a model defined in Swagger"""  # noqa: E501
        self._deployment_spec_name = None
        self._instance_deployment_template = None
        self._implementation_type = None
        self._attachment_point = None
        self._instance_deployment_config = None
        self._deployment_mode = None
        self._deployed_to = None
        self._service_deployment_id = None
        self.discriminator = None
        self.deployment_spec_name = deployment_spec_name
        self.instance_deployment_template = instance_deployment_template
        self.implementation_type = implementation_type
        self.attachment_point = attachment_point
        if instance_deployment_config is not None:
            self.instance_deployment_config = instance_deployment_config
        self.deployment_mode = deployment_mode
        self.deployed_to = deployed_to
        if service_deployment_id is not None:
            self.service_deployment_id = service_deployment_id
        BaseServiceInstance.__init__(self, *args, **kwargs)

    @property
    def deployment_spec_name(self):
        """Gets the deployment_spec_name of this ServiceInstance.  # noqa: E501

        Name of the deployment spec to be used by this service instance.  # noqa: E501

        :return: The deployment_spec_name of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._deployment_spec_name

    @deployment_spec_name.setter
    def deployment_spec_name(self, deployment_spec_name):
        """Sets the deployment_spec_name of this ServiceInstance.

        Name of the deployment spec to be used by this service instance.  # noqa: E501

        :param deployment_spec_name: The deployment_spec_name of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if deployment_spec_name is None:
            raise ValueError("Invalid value for `deployment_spec_name`, must not be `None`")  # noqa: E501

        self._deployment_spec_name = deployment_spec_name

    @property
    def instance_deployment_template(self):
        """Gets the instance_deployment_template of this ServiceInstance.  # noqa: E501


        :return: The instance_deployment_template of this ServiceInstance.  # noqa: E501
        :rtype: DeploymentTemplate
        """
        return self._instance_deployment_template

    @instance_deployment_template.setter
    def instance_deployment_template(self, instance_deployment_template):
        """Sets the instance_deployment_template of this ServiceInstance.


        :param instance_deployment_template: The instance_deployment_template of this ServiceInstance.  # noqa: E501
        :type: DeploymentTemplate
        """
        if instance_deployment_template is None:
            raise ValueError("Invalid value for `instance_deployment_template`, must not be `None`")  # noqa: E501

        self._instance_deployment_template = instance_deployment_template

    @property
    def implementation_type(self):
        """Gets the implementation_type of this ServiceInstance.  # noqa: E501

        Implementation to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :return: The implementation_type of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._implementation_type

    @implementation_type.setter
    def implementation_type(self, implementation_type):
        """Sets the implementation_type of this ServiceInstance.

        Implementation to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :param implementation_type: The implementation_type of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if implementation_type is None:
            raise ValueError("Invalid value for `implementation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["NORTH_SOUTH", "EAST_WEST"]  # noqa: E501
        if implementation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `implementation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(implementation_type, allowed_values)
            )

        self._implementation_type = implementation_type

    @property
    def attachment_point(self):
        """Gets the attachment_point of this ServiceInstance.  # noqa: E501

        Attachment point to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :return: The attachment_point of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._attachment_point

    @attachment_point.setter
    def attachment_point(self, attachment_point):
        """Sets the attachment_point of this ServiceInstance.

        Attachment point to be used by this service instance for deploying the Service-VM.  # noqa: E501

        :param attachment_point: The attachment_point of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if attachment_point is None:
            raise ValueError("Invalid value for `attachment_point`, must not be `None`")  # noqa: E501
        allowed_values = ["TIER0_LR", "TIER1_LR", "SERVICE_PLANE", "HOST"]  # noqa: E501
        if attachment_point not in allowed_values:
            raise ValueError(
                "Invalid value for `attachment_point` ({0}), must be one of {1}"  # noqa: E501
                .format(attachment_point, allowed_values)
            )

        self._attachment_point = attachment_point

    @property
    def instance_deployment_config(self):
        """Gets the instance_deployment_config of this ServiceInstance.  # noqa: E501


        :return: The instance_deployment_config of this ServiceInstance.  # noqa: E501
        :rtype: InstanceDeploymentConfig
        """
        return self._instance_deployment_config

    @instance_deployment_config.setter
    def instance_deployment_config(self, instance_deployment_config):
        """Sets the instance_deployment_config of this ServiceInstance.


        :param instance_deployment_config: The instance_deployment_config of this ServiceInstance.  # noqa: E501
        :type: InstanceDeploymentConfig
        """

        self._instance_deployment_config = instance_deployment_config

    @property
    def deployment_mode(self):
        """Gets the deployment_mode of this ServiceInstance.  # noqa: E501

        Deployment mode specifies where the partner appliance will be deployed in HA or non-HA i.e standalone mode.  # noqa: E501

        :return: The deployment_mode of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        """Sets the deployment_mode of this ServiceInstance.

        Deployment mode specifies where the partner appliance will be deployed in HA or non-HA i.e standalone mode.  # noqa: E501

        :param deployment_mode: The deployment_mode of this ServiceInstance.  # noqa: E501
        :type: str
        """
        if deployment_mode is None:
            raise ValueError("Invalid value for `deployment_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["STAND_ALONE", "ACTIVE_STANDBY"]  # noqa: E501
        if deployment_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_mode, allowed_values)
            )

        self._deployment_mode = deployment_mode

    @property
    def deployed_to(self):
        """Gets the deployed_to of this ServiceInstance.  # noqa: E501

        List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion.  # noqa: E501

        :return: The deployed_to of this ServiceInstance.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._deployed_to

    @deployed_to.setter
    def deployed_to(self, deployed_to):
        """Sets the deployed_to of this ServiceInstance.

        List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion.  # noqa: E501

        :param deployed_to: The deployed_to of this ServiceInstance.  # noqa: E501
        :type: list[ResourceReference]
        """
        if deployed_to is None:
            raise ValueError("Invalid value for `deployed_to`, must not be `None`")  # noqa: E501

        self._deployed_to = deployed_to

    @property
    def service_deployment_id(self):
        """Gets the service_deployment_id of this ServiceInstance.  # noqa: E501

        Id of the Service Deployment using which the instances were deployed. Its available only for instances that were deployed using service deployment API.  # noqa: E501

        :return: The service_deployment_id of this ServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._service_deployment_id

    @service_deployment_id.setter
    def service_deployment_id(self, service_deployment_id):
        """Sets the service_deployment_id of this ServiceInstance.

        Id of the Service Deployment using which the instances were deployed. Its available only for instances that were deployed using service deployment API.  # noqa: E501

        :param service_deployment_id: The service_deployment_id of this ServiceInstance.  # noqa: E501
        :type: str
        """

        self._service_deployment_id = service_deployment_id

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
        if issubclass(ServiceInstance, dict):
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
        if not isinstance(other, ServiceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
