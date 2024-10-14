# CallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[CallMethodResult]**](CallMethodResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.call_response import CallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallResponse from a JSON string
call_response_instance = CallResponse.from_json(json)
# print the JSON string representation of the object
print(CallResponse.to_json())

# convert the object into a dict
call_response_dict = call_response_instance.to_dict()
# create an instance of CallResponse from a dict
call_response_from_dict = CallResponse.from_dict(call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


