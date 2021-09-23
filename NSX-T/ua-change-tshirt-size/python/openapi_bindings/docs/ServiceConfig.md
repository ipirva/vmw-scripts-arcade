# ServiceConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_to** | [**list[ResourceReference]**](ResourceReference.md) | The list of entities that the configurations should be applied to. This can either be a NSGroup or any other entity like TransportNode, LogicalPorts etc.  | [optional] 
**precedence** | **int** | Every ServiceConfig has a priority based upon its precedence value. Lower the value of precedence, higher will be its priority. If user doesnt specify the precedence, it is generated automatically by system. The precedence is generated based upon the type of profile used in ServiceConfig. Precedence are auto-generated in decreasing order with difference of 100. Automatically generated precedence value will be 100 less than the current minimum value of precedence of ServiceConfig of a given profile type in system.There cannot be duplicate precedence for ServiceConfig of same profile type.  | [optional] 
**profiles** | [**list[NSXProfileReference]**](NSXProfileReference.md) | These are the NSX Profiles which will be added to service config, which will be applied to entities/groups provided to applied_to field of service config.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

