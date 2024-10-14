# ReadAtTimeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**req_times** | **List[datetime]** |  | [optional] 
**use_simple_bounds** | **bool** |  | [optional] 

## Example

```python
from opcua_webapi.models.read_at_time_details import ReadAtTimeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAtTimeDetails from a JSON string
read_at_time_details_instance = ReadAtTimeDetails.from_json(json)
# print the JSON string representation of the object
print(ReadAtTimeDetails.to_json())

# convert the object into a dict
read_at_time_details_dict = read_at_time_details_instance.to_dict()
# create an instance of ReadAtTimeDetails from a dict
read_at_time_details_from_dict = ReadAtTimeDetails.from_dict(read_at_time_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


