# ReferenceDescription

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.29).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_type_id** | **str** |  | [optional] 
**is_forward** | **bool** |  | [optional] [default to False]
**node_id** | **str** |  | [optional] 
**browse_name** | **str** |  | [optional] 
**display_name** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**node_class** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.2.5/#12.2.5.2). | [optional] 
**type_definition** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.reference_description import ReferenceDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceDescription from a JSON string
reference_description_instance = ReferenceDescription.from_json(json)
# print the JSON string representation of the object
print(ReferenceDescription.to_json())

# convert the object into a dict
reference_description_dict = reference_description_instance.to_dict()
# create an instance of ReferenceDescription from a dict
reference_description_from_dict = ReferenceDescription.from_dict(reference_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


