# UserNameIdentityToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | [optional] 
**password** | **bytearray** |  | [optional] 
**encryption_algorithm** | **str** |  | [optional] 
**policy_id** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.user_name_identity_token import UserNameIdentityToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserNameIdentityToken from a JSON string
user_name_identity_token_instance = UserNameIdentityToken.from_json(json)
# print the JSON string representation of the object
print(UserNameIdentityToken.to_json())

# convert the object into a dict
user_name_identity_token_dict = user_name_identity_token_instance.to_dict()
# create an instance of UserNameIdentityToken from a dict
user_name_identity_token_from_dict = UserNameIdentityToken.from_dict(user_name_identity_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


