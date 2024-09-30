# CallRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**methods_to_call** | [**List[CallMethodRequest]**](CallMethodRequest.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.call_request import CallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallRequest from a JSON string
call_request_instance = CallRequest.from_json(json)
# print the JSON string representation of the object
print CallRequest.to_json()

# convert the object into a dict
call_request_dict = call_request_instance.to_dict()
# create an instance of CallRequest from a dict
call_request_form_dict = call_request.from_dict(call_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


