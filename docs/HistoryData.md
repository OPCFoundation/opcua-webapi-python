# HistoryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_values** | [**List[DataValue]**](DataValue.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_data import HistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryData from a JSON string
history_data_instance = HistoryData.from_json(json)
# print the JSON string representation of the object
print HistoryData.to_json()

# convert the object into a dict
history_data_dict = history_data_instance.to_dict()
# create an instance of HistoryData from a dict
history_data_form_dict = history_data.from_dict(history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


