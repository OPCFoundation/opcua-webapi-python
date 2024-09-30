# ModifySubscriptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**revised_publishing_interval** | **float** |  | [optional] 
**revised_lifetime_count** | **int** |  | [optional] 
**revised_max_keep_alive_count** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.modify_subscription_response import ModifySubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySubscriptionResponse from a JSON string
modify_subscription_response_instance = ModifySubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print ModifySubscriptionResponse.to_json()

# convert the object into a dict
modify_subscription_response_dict = modify_subscription_response_instance.to_dict()
# create an instance of ModifySubscriptionResponse from a dict
modify_subscription_response_form_dict = modify_subscription_response.from_dict(modify_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


