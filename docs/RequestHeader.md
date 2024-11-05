# RequestHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_token** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**request_handle** | **int** |  | [optional] [default to 0]
**return_diagnostics** | **int** |  | [optional] [default to 0]
**audit_entry_id** | **str** |  | [optional] 
**timeout_hint** | **int** |  | [optional] [default to 0]
**additional_header** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.request_header import RequestHeader

# TODO update the JSON string below
json = "{}"
# create an instance of RequestHeader from a JSON string
request_header_instance = RequestHeader.from_json(json)
# print the JSON string representation of the object
print(RequestHeader.to_json())

# convert the object into a dict
request_header_dict = request_header_instance.to_dict()
# create an instance of RequestHeader from a dict
request_header_from_dict = RequestHeader.from_dict(request_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


