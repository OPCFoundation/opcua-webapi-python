# HistoryEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[HistoryEventFieldList]**](HistoryEventFieldList.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_event import HistoryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryEvent from a JSON string
history_event_instance = HistoryEvent.from_json(json)
# print the JSON string representation of the object
print HistoryEvent.to_json()

# convert the object into a dict
history_event_dict = history_event_instance.to_dict()
# create an instance of HistoryEvent from a dict
history_event_form_dict = history_event.from_dict(history_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


