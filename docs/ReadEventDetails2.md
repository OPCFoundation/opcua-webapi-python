# ReadEventDetails2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_modified** | **bool** |  | [optional] [default to False]
**num_values_per_node** | **int** |  | [optional] [default to 0]
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**filter** | [**EventFilter**](EventFilter.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.read_event_details2 import ReadEventDetails2

# TODO update the JSON string below
json = "{}"
# create an instance of ReadEventDetails2 from a JSON string
read_event_details2_instance = ReadEventDetails2.from_json(json)
# print the JSON string representation of the object
print(ReadEventDetails2.to_json())

# convert the object into a dict
read_event_details2_dict = read_event_details2_instance.to_dict()
# create an instance of ReadEventDetails2 from a dict
read_event_details2_from_dict = ReadEventDetails2.from_dict(read_event_details2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


