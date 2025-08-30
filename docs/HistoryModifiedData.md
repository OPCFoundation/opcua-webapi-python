# HistoryModifiedData

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part11/6.6.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modification_infos** | [**List[ModificationInfo]**](ModificationInfo.md) |  | [optional] 
**data_values** | [**List[DataValue]**](DataValue.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_modified_data import HistoryModifiedData

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryModifiedData from a JSON string
history_modified_data_instance = HistoryModifiedData.from_json(json)
# print the JSON string representation of the object
print(HistoryModifiedData.to_json())

# convert the object into a dict
history_modified_data_dict = history_modified_data_instance.to_dict()
# create an instance of HistoryModifiedData from a dict
history_modified_data_from_dict = HistoryModifiedData.from_dict(history_modified_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


