# ModifyMonitoredItemsResponse

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.3/#5.13.3.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**results** | [**List[MonitoredItemModifyResult]**](MonitoredItemModifyResult.md) |  | [optional] 
**diagnostic_infos** | [**List[DiagnosticInfo]**](DiagnosticInfo.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.modify_monitored_items_response import ModifyMonitoredItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyMonitoredItemsResponse from a JSON string
modify_monitored_items_response_instance = ModifyMonitoredItemsResponse.from_json(json)
# print the JSON string representation of the object
print(ModifyMonitoredItemsResponse.to_json())

# convert the object into a dict
modify_monitored_items_response_dict = modify_monitored_items_response_instance.to_dict()
# create an instance of ModifyMonitoredItemsResponse from a dict
modify_monitored_items_response_from_dict = ModifyMonitoredItemsResponse.from_dict(modify_monitored_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


