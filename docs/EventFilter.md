# EventFilter

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.22.3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**select_clauses** | [**List[SimpleAttributeOperand]**](SimpleAttributeOperand.md) |  | [optional] 
**where_clause** | [**ContentFilter**](ContentFilter.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.event_filter import EventFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilter from a JSON string
event_filter_instance = EventFilter.from_json(json)
# print the JSON string representation of the object
print(EventFilter.to_json())

# convert the object into a dict
event_filter_dict = event_filter_instance.to_dict()
# create an instance of EventFilter from a dict
event_filter_from_dict = EventFilter.from_dict(event_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


