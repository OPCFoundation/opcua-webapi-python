# X509IdentityToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_data** | **bytearray** |  | [optional] 
**policy_id** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.x509_identity_token import X509IdentityToken

# TODO update the JSON string below
json = "{}"
# create an instance of X509IdentityToken from a JSON string
x509_identity_token_instance = X509IdentityToken.from_json(json)
# print the JSON string representation of the object
print(X509IdentityToken.to_json())

# convert the object into a dict
x509_identity_token_dict = x509_identity_token_instance.to_dict()
# create an instance of X509IdentityToken from a dict
x509_identity_token_from_dict = X509IdentityToken.from_dict(x509_identity_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


