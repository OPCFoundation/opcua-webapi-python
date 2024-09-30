# RolePermissionType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** |  | [optional] 
**permissions** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.role_permission_type import RolePermissionType

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissionType from a JSON string
role_permission_type_instance = RolePermissionType.from_json(json)
# print the JSON string representation of the object
print RolePermissionType.to_json()

# convert the object into a dict
role_permission_type_dict = role_permission_type_instance.to_dict()
# create an instance of RolePermissionType from a dict
role_permission_type_form_dict = role_permission_type.from_dict(role_permission_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


