# HistoryUpdateRequest

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.11.5/#5.11.5.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**history_update_details** | [**List[ExtensionObject]**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_update_request import HistoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryUpdateRequest from a JSON string
history_update_request_instance = HistoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(HistoryUpdateRequest.to_json())

# convert the object into a dict
history_update_request_dict = history_update_request_instance.to_dict()
# create an instance of HistoryUpdateRequest from a dict
history_update_request_from_dict = HistoryUpdateRequest.from_dict(history_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


