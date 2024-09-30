# CreateSubscriptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**revised_publishing_interval** | **float** |  | [optional] 
**revised_lifetime_count** | **int** |  | [optional] 
**revised_max_keep_alive_count** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.create_subscription_response import CreateSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionResponse from a JSON string
create_subscription_response_instance = CreateSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print CreateSubscriptionResponse.to_json()

# convert the object into a dict
create_subscription_response_dict = create_subscription_response_instance.to_dict()
# create an instance of CreateSubscriptionResponse from a dict
create_subscription_response_form_dict = create_subscription_response.from_dict(create_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


