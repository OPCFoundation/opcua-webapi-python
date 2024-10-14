# HistoryEventFieldList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_fields** | [**List[Variant]**](Variant.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_event_field_list import HistoryEventFieldList

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryEventFieldList from a JSON string
history_event_field_list_instance = HistoryEventFieldList.from_json(json)
# print the JSON string representation of the object
print(HistoryEventFieldList.to_json())

# convert the object into a dict
history_event_field_list_dict = history_event_field_list_instance.to_dict()
# create an instance of HistoryEventFieldList from a dict
history_event_field_list_from_dict = HistoryEventFieldList.from_dict(history_event_field_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


