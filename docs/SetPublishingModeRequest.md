# SetPublishingModeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**publishing_enabled** | **bool** |  | [optional] 
**subscription_ids** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.set_publishing_mode_request import SetPublishingModeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPublishingModeRequest from a JSON string
set_publishing_mode_request_instance = SetPublishingModeRequest.from_json(json)
# print the JSON string representation of the object
print SetPublishingModeRequest.to_json()

# convert the object into a dict
set_publishing_mode_request_dict = set_publishing_mode_request_instance.to_dict()
# create an instance of SetPublishingModeRequest from a dict
set_publishing_mode_request_form_dict = set_publishing_mode_request.from_dict(set_publishing_mode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


