# UserIdentityToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.user_identity_token import UserIdentityToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentityToken from a JSON string
user_identity_token_instance = UserIdentityToken.from_json(json)
# print the JSON string representation of the object
print(UserIdentityToken.to_json())

# convert the object into a dict
user_identity_token_dict = user_identity_token_instance.to_dict()
# create an instance of UserIdentityToken from a dict
user_identity_token_from_dict = UserIdentityToken.from_dict(user_identity_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


