# DataTypeDescription

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.32).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.data_type_description import DataTypeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeDescription from a JSON string
data_type_description_instance = DataTypeDescription.from_json(json)
# print the JSON string representation of the object
print(DataTypeDescription.to_json())

# convert the object into a dict
data_type_description_dict = data_type_description_instance.to_dict()
# create an instance of DataTypeDescription from a dict
data_type_description_from_dict = DataTypeDescription.from_dict(data_type_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


