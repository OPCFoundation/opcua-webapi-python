# ReadRawModifiedDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_read_modified** | **bool** |  | [optional] [default to False]
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**num_values_per_node** | **int** |  | [optional] [default to 0]
**return_bounds** | **bool** |  | [optional] [default to False]

## Example

```python
from opcua_webapi.models.read_raw_modified_details import ReadRawModifiedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReadRawModifiedDetails from a JSON string
read_raw_modified_details_instance = ReadRawModifiedDetails.from_json(json)
# print the JSON string representation of the object
print(ReadRawModifiedDetails.to_json())

# convert the object into a dict
read_raw_modified_details_dict = read_raw_modified_details_instance.to_dict()
# create an instance of ReadRawModifiedDetails from a dict
read_raw_modified_details_from_dict = ReadRawModifiedDetails.from_dict(read_raw_modified_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


