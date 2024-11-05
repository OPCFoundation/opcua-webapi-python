# SubscriptionAcknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] [default to 0]
**sequence_number** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.subscription_acknowledgement import SubscriptionAcknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAcknowledgement from a JSON string
subscription_acknowledgement_instance = SubscriptionAcknowledgement.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAcknowledgement.to_json())

# convert the object into a dict
subscription_acknowledgement_dict = subscription_acknowledgement_instance.to_dict()
# create an instance of SubscriptionAcknowledgement from a dict
subscription_acknowledgement_from_dict = SubscriptionAcknowledgement.from_dict(subscription_acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


