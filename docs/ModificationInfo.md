# ModificationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modification_time** | **datetime** |  | [optional] 
**update_type** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.modification_info import ModificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModificationInfo from a JSON string
modification_info_instance = ModificationInfo.from_json(json)
# print the JSON string representation of the object
print(ModificationInfo.to_json())

# convert the object into a dict
modification_info_dict = modification_info_instance.to_dict()
# create an instance of ModificationInfo from a dict
modification_info_from_dict = ModificationInfo.from_dict(modification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


