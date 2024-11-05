# ViewDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**view_version** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.view_description import ViewDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDescription from a JSON string
view_description_instance = ViewDescription.from_json(json)
# print the JSON string representation of the object
print(ViewDescription.to_json())

# convert the object into a dict
view_description_dict = view_description_instance.to_dict()
# create an instance of ViewDescription from a dict
view_description_from_dict = ViewDescription.from_dict(view_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


