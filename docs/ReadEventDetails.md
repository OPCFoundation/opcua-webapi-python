# ReadEventDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_values_per_node** | **int** |  | [optional] [default to 0]
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**filter** | [**EventFilter**](EventFilter.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.read_event_details import ReadEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReadEventDetails from a JSON string
read_event_details_instance = ReadEventDetails.from_json(json)
# print the JSON string representation of the object
print(ReadEventDetails.to_json())

# convert the object into a dict
read_event_details_dict = read_event_details_instance.to_dict()
# create an instance of ReadEventDetails from a dict
read_event_details_from_dict = ReadEventDetails.from_dict(read_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


