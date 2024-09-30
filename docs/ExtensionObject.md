# ExtensionObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **str** |  | [optional] 
**encoding** | **int** |  | [optional] 
**body** | **object** |  | [optional] 

## Example

```python
from opcua_webapi.models.extension_object import ExtensionObject

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionObject from a JSON string
extension_object_instance = ExtensionObject.from_json(json)
# print the JSON string representation of the object
print ExtensionObject.to_json()

# convert the object into a dict
extension_object_dict = extension_object_instance.to_dict()
# create an instance of ExtensionObject from a dict
extension_object_form_dict = extension_object.from_dict(extension_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


