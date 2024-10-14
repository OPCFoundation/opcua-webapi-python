# DeleteMonitoredItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | **List[int]** |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.delete_monitored_items_response import DeleteMonitoredItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMonitoredItemsResponse from a JSON string
delete_monitored_items_response_instance = DeleteMonitoredItemsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteMonitoredItemsResponse.to_json())

# convert the object into a dict
delete_monitored_items_response_dict = delete_monitored_items_response_instance.to_dict()
# create an instance of DeleteMonitoredItemsResponse from a dict
delete_monitored_items_response_from_dict = DeleteMonitoredItemsResponse.from_dict(delete_monitored_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


