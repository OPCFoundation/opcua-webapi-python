# ExtensionObject

[Link to specification](https://reference.opcfoundation.org/Core/Part6/v105/docs/5.4.2.16).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ua_type_id** | **str** |  | [optional] 
**ua_encoding** | **int** |  | [optional] 
**ua_body** | **bytearray** |  | [optional] 

## Example

```python
from opcua_webapi.models.extension_object import ExtensionObject

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionObject from a JSON string
extension_object_instance = ExtensionObject.from_json(json)
# print the JSON string representation of the object
print(ExtensionObject.to_json())

# convert the object into a dict
extension_object_dict = extension_object_instance.to_dict()
# create an instance of ExtensionObject from a dict
extension_object_from_dict = ExtensionObject.from_dict(extension_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


