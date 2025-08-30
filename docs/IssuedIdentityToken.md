# IssuedIdentityToken

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part5/12.3.15/#12.3.15.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_data** | **bytearray** |  | [optional] 
**encryption_algorithm** | **str** |  | [optional] 
**policy_id** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.issued_identity_token import IssuedIdentityToken

# TODO update the JSON string below
json = "{}"
# create an instance of IssuedIdentityToken from a JSON string
issued_identity_token_instance = IssuedIdentityToken.from_json(json)
# print the JSON string representation of the object
print(IssuedIdentityToken.to_json())

# convert the object into a dict
issued_identity_token_dict = issued_identity_token_instance.to_dict()
# create an instance of IssuedIdentityToken from a dict
issued_identity_token_from_dict = IssuedIdentityToken.from_dict(issued_identity_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


