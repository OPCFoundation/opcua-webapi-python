# UserTokenPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | [optional] 
**token_type** | **int** |  | [optional] 
**issued_token_type** | **str** |  | [optional] 
**issuer_endpoint_url** | **str** |  | [optional] 
**security_policy_uri** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.user_token_policy import UserTokenPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UserTokenPolicy from a JSON string
user_token_policy_instance = UserTokenPolicy.from_json(json)
# print the JSON string representation of the object
print UserTokenPolicy.to_json()

# convert the object into a dict
user_token_policy_dict = user_token_policy_instance.to_dict()
# create an instance of UserTokenPolicy from a dict
user_token_policy_form_dict = user_token_policy.from_dict(user_token_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


