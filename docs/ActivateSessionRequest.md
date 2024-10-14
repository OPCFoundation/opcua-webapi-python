# ActivateSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**client_signature** | [**SignatureData**](SignatureData.md) |  | [optional] 
**client_software_certificates** | [**List[SignedSoftwareCertificate]**](SignedSoftwareCertificate.md) |  | [optional] 
**locale_ids** | **List[str]** |  | [optional] 
**user_identity_token** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**user_token_signature** | [**SignatureData**](SignatureData.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.activate_session_request import ActivateSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateSessionRequest from a JSON string
activate_session_request_instance = ActivateSessionRequest.from_json(json)
# print the JSON string representation of the object
print(ActivateSessionRequest.to_json())

# convert the object into a dict
activate_session_request_dict = activate_session_request_instance.to_dict()
# create an instance of ActivateSessionRequest from a dict
activate_session_request_from_dict = ActivateSessionRequest.from_dict(activate_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


