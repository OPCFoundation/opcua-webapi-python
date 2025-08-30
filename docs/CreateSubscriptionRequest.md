# CreateSubscriptionRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.2/#5.14.2.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**requested_publishing_interval** | **float** |  | [optional] [default to 0]
**requested_lifetime_count** | **int** |  | [optional] [default to 0]
**requested_max_keep_alive_count** | **int** |  | [optional] [default to 0]
**max_notifications_per_publish** | **int** |  | [optional] [default to 0]
**publishing_enabled** | **bool** |  | [optional] [default to False]
**priority** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.create_subscription_request import CreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequest from a JSON string
create_subscription_request_instance = CreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionRequest.to_json())

# convert the object into a dict
create_subscription_request_dict = create_subscription_request_instance.to_dict()
# create an instance of CreateSubscriptionRequest from a dict
create_subscription_request_from_dict = CreateSubscriptionRequest.from_dict(create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


