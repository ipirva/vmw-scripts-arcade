# NSGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_count** | **int** | Count of the members added to this NSGroup | [optional] 
**members** | [**list[NSGroupSimpleExpression]**](NSGroupSimpleExpression.md) | Reference to the direct/static members of the NSGroup. Can be ID based expressions only. VirtualMachine cannot be added as a static member.  | [optional] 
**membership_criteria** | [**list[NSGroupExpression]**](NSGroupExpression.md) | List of tag or name based expressions which define the dynamic membership criteria for this NSGroup. An object must satisfy atleast one of these expressions to qualify as a member of this group. It is not recommended to use ID based expressions in this section. ID based expression should be used in \&quot;members\&quot; section  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

