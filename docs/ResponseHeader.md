# ResponseHeader

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.33).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**request_handle** | **int** |  | [optional] [default to 0]
**service_result** | [**StatusCode**](StatusCode.md) |  | [optional] 
**service_diagnostics** | [**DiagnosticInfo**](DiagnosticInfo.md) |  | [optional] 
**string_table** | **List[str]** |  | [optional] 
**additional_header** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.response_header import ResponseHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseHeader from a JSON string
response_header_instance = ResponseHeader.from_json(json)
# print the JSON string representation of the object
print(ResponseHeader.to_json())

# convert the object into a dict
response_header_dict = response_header_instance.to_dict()
# create an instance of ResponseHeader from a dict
response_header_from_dict = ResponseHeader.from_dict(response_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


