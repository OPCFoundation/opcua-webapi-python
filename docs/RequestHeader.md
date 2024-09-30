# RequestHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_token** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**request_handle** | **int** |  | [optional] 
**return_diagnostics** | **int** |  | [optional] 
**audit_entry_id** | **str** |  | [optional] 
**timeout_hint** | **int** |  | [optional] 
**additional_header** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.request_header import RequestHeader

# TODO update the JSON string below
json = "{}"
# create an instance of RequestHeader from a JSON string
request_header_instance = RequestHeader.from_json(json)
# print the JSON string representation of the object
print RequestHeader.to_json()

# convert the object into a dict
request_header_dict = request_header_instance.to_dict()
# create an instance of RequestHeader from a dict
request_header_form_dict = request_header.from_dict(request_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


