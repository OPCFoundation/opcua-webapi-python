# ResponseHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**request_handle** | **int** |  | [optional] 
**service_result** | **int** |  | [optional] 
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
print ResponseHeader.to_json()

# convert the object into a dict
response_header_dict = response_header_instance.to_dict()
# create an instance of ResponseHeader from a dict
response_header_form_dict = response_header.from_dict(response_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


