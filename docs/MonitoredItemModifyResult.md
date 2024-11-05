# MonitoredItemModifyResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 
**revised_sampling_interval** | **float** |  | [optional] [default to 0]
**revised_queue_size** | **int** |  | [optional] [default to 0]
**filter_result** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.monitored_item_modify_result import MonitoredItemModifyResult

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredItemModifyResult from a JSON string
monitored_item_modify_result_instance = MonitoredItemModifyResult.from_json(json)
# print the JSON string representation of the object
print(MonitoredItemModifyResult.to_json())

# convert the object into a dict
monitored_item_modify_result_dict = monitored_item_modify_result_instance.to_dict()
# create an instance of MonitoredItemModifyResult from a dict
monitored_item_modify_result_from_dict = MonitoredItemModifyResult.from_dict(monitored_item_modify_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


