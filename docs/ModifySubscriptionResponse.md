# ModifySubscriptionResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.3/#5.14.3.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**revised_publishing_interval** | **float** |  | [optional] [default to 0]
**revised_lifetime_count** | **int** |  | [optional] [default to 0]
**revised_max_keep_alive_count** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.modify_subscription_response import ModifySubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifySubscriptionResponse from a JSON string
modify_subscription_response_instance = ModifySubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(ModifySubscriptionResponse.to_json())

# convert the object into a dict
modify_subscription_response_dict = modify_subscription_response_instance.to_dict()
# create an instance of ModifySubscriptionResponse from a dict
modify_subscription_response_from_dict = ModifySubscriptionResponse.from_dict(modify_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


