# SetTriggeringRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.5/#5.13.5.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**subscription_id** | **int** |  | [optional] [default to 0]
**triggering_item_id** | **int** |  | [optional] [default to 0]
**links_to_add** | **List[int]** |  | [optional] 
**links_to_remove** | **List[int]** |  | [optional] 

## Example

```python
from opcua_webapi.models.set_triggering_request import SetTriggeringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTriggeringRequest from a JSON string
set_triggering_request_instance = SetTriggeringRequest.from_json(json)
# print the JSON string representation of the object
print(SetTriggeringRequest.to_json())

# convert the object into a dict
set_triggering_request_dict = set_triggering_request_instance.to_dict()
# create an instance of SetTriggeringRequest from a dict
set_triggering_request_from_dict = SetTriggeringRequest.from_dict(set_triggering_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


