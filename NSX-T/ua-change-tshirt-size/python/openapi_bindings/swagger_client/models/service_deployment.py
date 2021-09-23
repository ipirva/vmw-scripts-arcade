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

class ServiceDeployment(ManagedResource):
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
        'perimeter': 'str',
        'deployment_spec_name': 'str',
        'deployment_mode': 'str',
        'instance_deployment_template': 'DeploymentTemplate',
        'service_deployment_config': 'ServiceDeploymentConfig',
        'service_id': 'str',
        'clustered_deployment_count': 'int',
        'deployed_to': 'list[ResourceReference]',
        'deployment_type': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'perimeter': 'perimeter',
        'deployment_spec_name': 'deployment_spec_name',
        'deployment_mode': 'deployment_mode',
        'instance_deployment_template': 'instance_deployment_template',
        'service_deployment_config': 'service_deployment_config',
        'service_id': 'service_id',
        'clustered_deployment_count': 'clustered_deployment_count',
        'deployed_to': 'deployed_to',
        'deployment_type': 'deployment_type'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, perimeter='HOST', deployment_spec_name=None, deployment_mode='STAND_ALONE', instance_deployment_template=None, service_deployment_config=None, service_id=None, clustered_deployment_count=1, deployed_to=None, deployment_type='CLUSTERED', *args, **kwargs):  # noqa: E501
        """ServiceDeployment - a model defined in Swagger"""  # noqa: E501
        self._perimeter = None
        self._deployment_spec_name = None
        self._deployment_mode = None
        self._instance_deployment_template = None
        self._service_deployment_config = None
        self._service_id = None
        self._clustered_deployment_count = None
        self._deployed_to = None
        self._deployment_type = None
        self.discriminator = None
        if perimeter is not None:
            self.perimeter = perimeter
        self.deployment_spec_name = deployment_spec_name
        if deployment_mode is not None:
            self.deployment_mode = deployment_mode
        self.instance_deployment_template = instance_deployment_template
        self.service_deployment_config = service_deployment_config
        if service_id is not None:
            self.service_id = service_id
        if clustered_deployment_count is not None:
            self.clustered_deployment_count = clustered_deployment_count
        if deployed_to is not None:
            self.deployed_to = deployed_to
        if deployment_type is not None:
            self.deployment_type = deployment_type
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def perimeter(self):
        """Gets the perimeter of this ServiceDeployment.  # noqa: E501

        This indicates the deployment perimeter, such as a VC cluster or a host.  # noqa: E501

        :return: The perimeter of this ServiceDeployment.  # noqa: E501
        :rtype: str
        """
        return self._perimeter

    @perimeter.setter
    def perimeter(self, perimeter):
        """Sets the perimeter of this ServiceDeployment.

        This indicates the deployment perimeter, such as a VC cluster or a host.  # noqa: E501

        :param perimeter: The perimeter of this ServiceDeployment.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER", "HOST"]  # noqa: E501
        if perimeter not in allowed_values:
            raise ValueError(
                "Invalid value for `perimeter` ({0}), must be one of {1}"  # noqa: E501
                .format(perimeter, allowed_values)
            )

        self._perimeter = perimeter

    @property
    def deployment_spec_name(self):
        """Gets the deployment_spec_name of this ServiceDeployment.  # noqa: E501

        Name of the deployment spec to be used for deployment, which specifies the OVF provided by the partner and the form factor.  # noqa: E501

        :return: The deployment_spec_name of this ServiceDeployment.  # noqa: E501
        :rtype: str
        """
        return self._deployment_spec_name

    @deployment_spec_name.setter
    def deployment_spec_name(self, deployment_spec_name):
        """Sets the deployment_spec_name of this ServiceDeployment.

        Name of the deployment spec to be used for deployment, which specifies the OVF provided by the partner and the form factor.  # noqa: E501

        :param deployment_spec_name: The deployment_spec_name of this ServiceDeployment.  # noqa: E501
        :type: str
        """
        if deployment_spec_name is None:
            raise ValueError("Invalid value for `deployment_spec_name`, must not be `None`")  # noqa: E501

        self._deployment_spec_name = deployment_spec_name

    @property
    def deployment_mode(self):
        """Gets the deployment_mode of this ServiceDeployment.  # noqa: E501

        Mode of deployment. Currently, only stand alone deployment is supported. It is a single VM deployed through this deployment spec. In future, HA configurations will be supported here.  # noqa: E501

        :return: The deployment_mode of this ServiceDeployment.  # noqa: E501
        :rtype: str
        """
        return self._deployment_mode

    @deployment_mode.setter
    def deployment_mode(self, deployment_mode):
        """Sets the deployment_mode of this ServiceDeployment.

        Mode of deployment. Currently, only stand alone deployment is supported. It is a single VM deployed through this deployment spec. In future, HA configurations will be supported here.  # noqa: E501

        :param deployment_mode: The deployment_mode of this ServiceDeployment.  # noqa: E501
        :type: str
        """
        allowed_values = ["STAND_ALONE", "ACTIVE_STANDBY"]  # noqa: E501
        if deployment_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_mode, allowed_values)
            )

        self._deployment_mode = deployment_mode

    @property
    def instance_deployment_template(self):
        """Gets the instance_deployment_template of this ServiceDeployment.  # noqa: E501


        :return: The instance_deployment_template of this ServiceDeployment.  # noqa: E501
        :rtype: DeploymentTemplate
        """
        return self._instance_deployment_template

    @instance_deployment_template.setter
    def instance_deployment_template(self, instance_deployment_template):
        """Sets the instance_deployment_template of this ServiceDeployment.


        :param instance_deployment_template: The instance_deployment_template of this ServiceDeployment.  # noqa: E501
        :type: DeploymentTemplate
        """
        if instance_deployment_template is None:
            raise ValueError("Invalid value for `instance_deployment_template`, must not be `None`")  # noqa: E501

        self._instance_deployment_template = instance_deployment_template

    @property
    def service_deployment_config(self):
        """Gets the service_deployment_config of this ServiceDeployment.  # noqa: E501


        :return: The service_deployment_config of this ServiceDeployment.  # noqa: E501
        :rtype: ServiceDeploymentConfig
        """
        return self._service_deployment_config

    @service_deployment_config.setter
    def service_deployment_config(self, service_deployment_config):
        """Sets the service_deployment_config of this ServiceDeployment.


        :param service_deployment_config: The service_deployment_config of this ServiceDeployment.  # noqa: E501
        :type: ServiceDeploymentConfig
        """
        if service_deployment_config is None:
            raise ValueError("Invalid value for `service_deployment_config`, must not be `None`")  # noqa: E501

        self._service_deployment_config = service_deployment_config

    @property
    def service_id(self):
        """Gets the service_id of this ServiceDeployment.  # noqa: E501

        The Service to which the service deployment is associated.  # noqa: E501

        :return: The service_id of this ServiceDeployment.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ServiceDeployment.

        The Service to which the service deployment is associated.  # noqa: E501

        :param service_id: The service_id of this ServiceDeployment.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def clustered_deployment_count(self):
        """Gets the clustered_deployment_count of this ServiceDeployment.  # noqa: E501

        Number of instances in case of clustered deployment.  # noqa: E501

        :return: The clustered_deployment_count of this ServiceDeployment.  # noqa: E501
        :rtype: int
        """
        return self._clustered_deployment_count

    @clustered_deployment_count.setter
    def clustered_deployment_count(self, clustered_deployment_count):
        """Sets the clustered_deployment_count of this ServiceDeployment.

        Number of instances in case of clustered deployment.  # noqa: E501

        :param clustered_deployment_count: The clustered_deployment_count of this ServiceDeployment.  # noqa: E501
        :type: int
        """

        self._clustered_deployment_count = clustered_deployment_count

    @property
    def deployed_to(self):
        """Gets the deployed_to of this ServiceDeployment.  # noqa: E501

        List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion. Service Attachment in case of E-W ServiceInsertion.  # noqa: E501

        :return: The deployed_to of this ServiceDeployment.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._deployed_to

    @deployed_to.setter
    def deployed_to(self, deployed_to):
        """Sets the deployed_to of this ServiceDeployment.

        List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion. Service Attachment in case of E-W ServiceInsertion.  # noqa: E501

        :param deployed_to: The deployed_to of this ServiceDeployment.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._deployed_to = deployed_to

    @property
    def deployment_type(self):
        """Gets the deployment_type of this ServiceDeployment.  # noqa: E501

        Specifies whether the service VM should be deployed on each host such that it provides partner service locally on the host, or whether the service VMs can be deployed as a cluster. If deployment_type is CLUSTERED, then the clustered_deployment_count should be provided.  # noqa: E501

        :return: The deployment_type of this ServiceDeployment.  # noqa: E501
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this ServiceDeployment.

        Specifies whether the service VM should be deployed on each host such that it provides partner service locally on the host, or whether the service VMs can be deployed as a cluster. If deployment_type is CLUSTERED, then the clustered_deployment_count should be provided.  # noqa: E501

        :param deployment_type: The deployment_type of this ServiceDeployment.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOSTLOCAL", "CLUSTERED"]  # noqa: E501
        if deployment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

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
        if issubclass(ServiceDeployment, dict):
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
        if not isinstance(other, ServiceDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other