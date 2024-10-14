# ReadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**max_age** | **float** |  | [optional] 
**timestamps_to_return** | **int** |  | [optional] 
**nodes_to_read** | [**List[ReadValueId]**](ReadValueId.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.read_request import ReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReadRequest from a JSON string
read_request_instance = ReadRequest.from_json(json)
# print the JSON string representation of the object
print(ReadRequest.to_json())

# convert the object into a dict
read_request_dict = read_request_instance.to_dict()
# create an instance of ReadRequest from a dict
read_request_from_dict = ReadRequest.from_dict(read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


