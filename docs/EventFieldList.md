# EventFieldList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_handle** | **int** |  | [optional] [default to 0]
**event_fields** | [**List[Variant]**](Variant.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.event_field_list import EventFieldList

# TODO update the JSON string below
json = "{}"
# create an instance of EventFieldList from a JSON string
event_field_list_instance = EventFieldList.from_json(json)
# print the JSON string representation of the object
print(EventFieldList.to_json())

# convert the object into a dict
event_field_list_dict = event_field_list_instance.to_dict()
# create an instance of EventFieldList from a dict
event_field_list_from_dict = EventFieldList.from_dict(event_field_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


