# RolePermissionType

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.2.12/#12.2.12.9).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** |  | [optional] 
**permissions** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.role_permission_type import RolePermissionType

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissionType from a JSON string
role_permission_type_instance = RolePermissionType.from_json(json)
# print the JSON string representation of the object
print(RolePermissionType.to_json())

# convert the object into a dict
role_permission_type_dict = role_permission_type_instance.to_dict()
# create an instance of RolePermissionType from a dict
role_permission_type_from_dict = RolePermissionType.from_dict(role_permission_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


