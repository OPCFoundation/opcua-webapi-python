# ActivateSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**server_nonce** | **bytearray** |  | [optional] 
**results** | **List[int]** |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.activate_session_response import ActivateSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateSessionResponse from a JSON string
activate_session_response_instance = ActivateSessionResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateSessionResponse.to_json())

# convert the object into a dict
activate_session_response_dict = activate_session_response_instance.to_dict()
# create an instance of ActivateSessionResponse from a dict
activate_session_response_from_dict = ActivateSessionResponse.from_dict(activate_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


