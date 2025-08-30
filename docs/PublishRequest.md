# PublishRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.5/#5.14.5.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_acknowledgements** | [**List[SubscriptionAcknowledgement]**](SubscriptionAcknowledgement.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.publish_request import PublishRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishRequest from a JSON string
publish_request_instance = PublishRequest.from_json(json)
# print the JSON string representation of the object
print(PublishRequest.to_json())

# convert the object into a dict
publish_request_dict = publish_request_instance.to_dict()
# create an instance of PublishRequest from a dict
publish_request_from_dict = PublishRequest.from_dict(publish_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


