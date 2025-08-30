# WriteRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.4/#5.11.4.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**nodes_to_write** | [**List[WriteValue]**](WriteValue.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.write_request import WriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WriteRequest from a JSON string
write_request_instance = WriteRequest.from_json(json)
# print the JSON string representation of the object
print(WriteRequest.to_json())

# convert the object into a dict
write_request_dict = write_request_instance.to_dict()
# create an instance of WriteRequest from a dict
write_request_from_dict = WriteRequest.from_dict(write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


