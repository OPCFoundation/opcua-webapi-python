# WriteResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.4/#5.11.4.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[StatusCode]**](StatusCode.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.write_response import WriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WriteResponse from a JSON string
write_response_instance = WriteResponse.from_json(json)
# print the JSON string representation of the object
print(WriteResponse.to_json())

# convert the object into a dict
write_response_dict = write_response_instance.to_dict()
# create an instance of WriteResponse from a dict
write_response_from_dict = WriteResponse.from_dict(write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


