# SecurityGroupDataType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**security_group_folder** | **List[str]** |  | [optional] 
**key_lifetime** | **float** |  | [optional] 
**security_policy_uri** | **str** |  | [optional] 
**max_future_key_count** | **int** |  | [optional] 
**max_past_key_count** | **int** |  | [optional] 
**security_group_id** | **str** |  | [optional] 
**role_permissions** | [**List[RolePermissionType]**](RolePermissionType.md) |  | [optional] 
**group_properties** | [**List[KeyValuePair]**](KeyValuePair.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.security_group_data_type import SecurityGroupDataType

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupDataType from a JSON string
security_group_data_type_instance = SecurityGroupDataType.from_json(json)
# print the JSON string representation of the object
print SecurityGroupDataType.to_json()

# convert the object into a dict
security_group_data_type_dict = security_group_data_type_instance.to_dict()
# create an instance of SecurityGroupDataType from a dict
security_group_data_type_form_dict = security_group_data_type.from_dict(security_group_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


