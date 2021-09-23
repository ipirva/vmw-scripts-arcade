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

class NodeSyslogExporterProperties(Resource):
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
        'tls_ca_pem': 'str',
        'protocol': 'str',
        'exporter_name': 'str',
        'level': 'str',
        'tls_client_ca_pem': 'str',
        'tls_cert_pem': 'str',
        'server': 'str',
        'facilities': 'list[str]',
        'msgids': 'list[str]',
        'structured_data': 'list[str]',
        'port': 'int',
        'tls_key_pem': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'tls_ca_pem': 'tls_ca_pem',
        'protocol': 'protocol',
        'exporter_name': 'exporter_name',
        'level': 'level',
        'tls_client_ca_pem': 'tls_client_ca_pem',
        'tls_cert_pem': 'tls_cert_pem',
        'server': 'server',
        'facilities': 'facilities',
        'msgids': 'msgids',
        'structured_data': 'structured_data',
        'port': 'port',
        'tls_key_pem': 'tls_key_pem'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, tls_ca_pem=None, protocol=None, exporter_name=None, level=None, tls_client_ca_pem=None, tls_cert_pem=None, server=None, facilities=None, msgids=None, structured_data=None, port=None, tls_key_pem=None, *args, **kwargs):  # noqa: E501
        """NodeSyslogExporterProperties - a model defined in Swagger"""  # noqa: E501
        self._tls_ca_pem = None
        self._protocol = None
        self._exporter_name = None
        self._level = None
        self._tls_client_ca_pem = None
        self._tls_cert_pem = None
        self._server = None
        self._facilities = None
        self._msgids = None
        self._structured_data = None
        self._port = None
        self._tls_key_pem = None
        self.discriminator = None
        if tls_ca_pem is not None:
            self.tls_ca_pem = tls_ca_pem
        self.protocol = protocol
        self.exporter_name = exporter_name
        self.level = level
        if tls_client_ca_pem is not None:
            self.tls_client_ca_pem = tls_client_ca_pem
        if tls_cert_pem is not None:
            self.tls_cert_pem = tls_cert_pem
        self.server = server
        if facilities is not None:
            self.facilities = facilities
        if msgids is not None:
            self.msgids = msgids
        if structured_data is not None:
            self.structured_data = structured_data
        if port is not None:
            self.port = port
        if tls_key_pem is not None:
            self.tls_key_pem = tls_key_pem
        Resource.__init__(self, *args, **kwargs)

    @property
    def tls_ca_pem(self):
        """Gets the tls_ca_pem of this NodeSyslogExporterProperties.  # noqa: E501

        CA certificate PEM of TLS server to export to  # noqa: E501

        :return: The tls_ca_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._tls_ca_pem

    @tls_ca_pem.setter
    def tls_ca_pem(self, tls_ca_pem):
        """Sets the tls_ca_pem of this NodeSyslogExporterProperties.

        CA certificate PEM of TLS server to export to  # noqa: E501

        :param tls_ca_pem: The tls_ca_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """

        self._tls_ca_pem = tls_ca_pem

    @property
    def protocol(self):
        """Gets the protocol of this NodeSyslogExporterProperties.  # noqa: E501

        Export protocol  # noqa: E501

        :return: The protocol of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NodeSyslogExporterProperties.

        Export protocol  # noqa: E501

        :param protocol: The protocol of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["TCP", "TLS", "UDP", "LI", "LI-TLS"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def exporter_name(self):
        """Gets the exporter_name of this NodeSyslogExporterProperties.  # noqa: E501

        Syslog exporter name  # noqa: E501

        :return: The exporter_name of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._exporter_name

    @exporter_name.setter
    def exporter_name(self, exporter_name):
        """Sets the exporter_name of this NodeSyslogExporterProperties.

        Syslog exporter name  # noqa: E501

        :param exporter_name: The exporter_name of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """
        if exporter_name is None:
            raise ValueError("Invalid value for `exporter_name`, must not be `None`")  # noqa: E501

        self._exporter_name = exporter_name

    @property
    def level(self):
        """Gets the level of this NodeSyslogExporterProperties.  # noqa: E501

        Logging level to export  # noqa: E501

        :return: The level of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this NodeSyslogExporterProperties.

        Logging level to export  # noqa: E501

        :param level: The level of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501
        allowed_values = ["EMERG", "ALERT", "CRIT", "ERR", "WARNING", "NOTICE", "INFO", "DEBUG"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def tls_client_ca_pem(self):
        """Gets the tls_client_ca_pem of this NodeSyslogExporterProperties.  # noqa: E501

        CA certificate PEM of the rsyslog client  # noqa: E501

        :return: The tls_client_ca_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._tls_client_ca_pem

    @tls_client_ca_pem.setter
    def tls_client_ca_pem(self, tls_client_ca_pem):
        """Sets the tls_client_ca_pem of this NodeSyslogExporterProperties.

        CA certificate PEM of the rsyslog client  # noqa: E501

        :param tls_client_ca_pem: The tls_client_ca_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """

        self._tls_client_ca_pem = tls_client_ca_pem

    @property
    def tls_cert_pem(self):
        """Gets the tls_cert_pem of this NodeSyslogExporterProperties.  # noqa: E501

        Certificate PEM of the rsyslog client  # noqa: E501

        :return: The tls_cert_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._tls_cert_pem

    @tls_cert_pem.setter
    def tls_cert_pem(self, tls_cert_pem):
        """Sets the tls_cert_pem of this NodeSyslogExporterProperties.

        Certificate PEM of the rsyslog client  # noqa: E501

        :param tls_cert_pem: The tls_cert_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """

        self._tls_cert_pem = tls_cert_pem

    @property
    def server(self):
        """Gets the server of this NodeSyslogExporterProperties.  # noqa: E501

        IP address or hostname of server to export to  # noqa: E501

        :return: The server of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this NodeSyslogExporterProperties.

        IP address or hostname of server to export to  # noqa: E501

        :param server: The server of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """
        if server is None:
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

    @property
    def facilities(self):
        """Gets the facilities of this NodeSyslogExporterProperties.  # noqa: E501

        Facilities to export  # noqa: E501

        :return: The facilities of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this NodeSyslogExporterProperties.

        Facilities to export  # noqa: E501

        :param facilities: The facilities of this NodeSyslogExporterProperties.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["KERN", "USER", "MAIL", "DAEMON", "AUTH", "SYSLOG", "LPR", "NEWS", "UUCP", "AUTHPRIV", "FTP", "LOGALERT", "CRON", "LOCAL0", "LOCAL1", "LOCAL2", "LOCAL3", "LOCAL4", "LOCAL5", "LOCAL6", "LOCAL7"]  # noqa: E501
        if not set(facilities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `facilities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(facilities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._facilities = facilities

    @property
    def msgids(self):
        """Gets the msgids of this NodeSyslogExporterProperties.  # noqa: E501

        MSGIDs to export  # noqa: E501

        :return: The msgids of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._msgids

    @msgids.setter
    def msgids(self, msgids):
        """Sets the msgids of this NodeSyslogExporterProperties.

        MSGIDs to export  # noqa: E501

        :param msgids: The msgids of this NodeSyslogExporterProperties.  # noqa: E501
        :type: list[str]
        """

        self._msgids = msgids

    @property
    def structured_data(self):
        """Gets the structured_data of this NodeSyslogExporterProperties.  # noqa: E501

        Structured data to export  # noqa: E501

        :return: The structured_data of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._structured_data

    @structured_data.setter
    def structured_data(self, structured_data):
        """Sets the structured_data of this NodeSyslogExporterProperties.

        Structured data to export  # noqa: E501

        :param structured_data: The structured_data of this NodeSyslogExporterProperties.  # noqa: E501
        :type: list[str]
        """

        self._structured_data = structured_data

    @property
    def port(self):
        """Gets the port of this NodeSyslogExporterProperties.  # noqa: E501

        Port to export to, defaults to 514 for TCP, TLS, UDP protocols or 9000 for LI, LI-TLS protocols  # noqa: E501

        :return: The port of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NodeSyslogExporterProperties.

        Port to export to, defaults to 514 for TCP, TLS, UDP protocols or 9000 for LI, LI-TLS protocols  # noqa: E501

        :param port: The port of this NodeSyslogExporterProperties.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def tls_key_pem(self):
        """Gets the tls_key_pem of this NodeSyslogExporterProperties.  # noqa: E501

        Private key PEM of the rsyslog client  # noqa: E501

        :return: The tls_key_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :rtype: str
        """
        return self._tls_key_pem

    @tls_key_pem.setter
    def tls_key_pem(self, tls_key_pem):
        """Sets the tls_key_pem of this NodeSyslogExporterProperties.

        Private key PEM of the rsyslog client  # noqa: E501

        :param tls_key_pem: The tls_key_pem of this NodeSyslogExporterProperties.  # noqa: E501
        :type: str
        """

        self._tls_key_pem = tls_key_pem

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
        if issubclass(NodeSyslogExporterProperties, dict):
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
        if not isinstance(other, NodeSyslogExporterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
