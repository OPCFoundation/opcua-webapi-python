# CreateSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**revised_publishing_interval** | **float** |  | [optional] [default to 0]
**revised_lifetime_count** | **int** |  | [optional] [default to 0]
**revised_max_keep_alive_count** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.create_subscription_response import CreateSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionResponse from a JSON string
create_subscription_response_instance = CreateSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionResponse.to_json())

# convert the object into a dict
create_subscription_response_dict = create_subscription_response_instance.to_dict()
# create an instance of CreateSubscriptionResponse from a dict
create_subscription_response_from_dict = CreateSubscriptionResponse.from_dict(create_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


