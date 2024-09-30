# UpdateEventDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**perform_insert_replace** | **int** |  | [optional] 
**filter** | [**EventFilter**](EventFilter.md) |  | [optional] 
**event_data** | [**List[HistoryEventFieldList]**](HistoryEventFieldList.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.update_event_details import UpdateEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEventDetails from a JSON string
update_event_details_instance = UpdateEventDetails.from_json(json)
# print the JSON string representation of the object
print UpdateEventDetails.to_json()

# convert the object into a dict
update_event_details_dict = update_event_details_instance.to_dict()
# create an instance of UpdateEventDetails from a dict
update_event_details_form_dict = update_event_details.from_dict(update_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


