# HistoryReadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_header** | [**RequestHeader**](RequestHeader.md) |  | [optional] 
**history_read_details** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**timestamps_to_return** | **int** |  | [optional] 
**release_continuation_points** | **bool** |  | [optional] [default to False]
**nodes_to_read** | [**List[HistoryReadValueId]**](HistoryReadValueId.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.history_read_request import HistoryReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryReadRequest from a JSON string
history_read_request_instance = HistoryReadRequest.from_json(json)
# print the JSON string representation of the object
print(HistoryReadRequest.to_json())

# convert the object into a dict
history_read_request_dict = history_read_request_instance.to_dict()
# create an instance of HistoryReadRequest from a dict
history_read_request_from_dict = HistoryReadRequest.from_dict(history_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


