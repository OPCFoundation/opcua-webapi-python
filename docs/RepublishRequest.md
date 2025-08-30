# RepublishRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.14.6/#5.14.6.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**retransmit_sequence_number** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.republish_request import RepublishRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepublishRequest from a JSON string
republish_request_instance = RepublishRequest.from_json(json)
# print the JSON string representation of the object
print(RepublishRequest.to_json())

# convert the object into a dict
republish_request_dict = republish_request_instance.to_dict()
# create an instance of RepublishRequest from a dict
republish_request_from_dict = RepublishRequest.from_dict(republish_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


