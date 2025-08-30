# MonitoredItemCreateResult

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/5.13.2/#5.13.2.2).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 
**monitored_item_id** | **int** |  | [optional] [default to 0]
**revised_sampling_interval** | **float** |  | [optional] [default to 0]
**revised_queue_size** | **int** |  | [optional] [default to 0]
**filter_result** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.monitored_item_create_result import MonitoredItemCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoredItemCreateResult from a JSON string
monitored_item_create_result_instance = MonitoredItemCreateResult.from_json(json)
# print the JSON string representation of the object
print(MonitoredItemCreateResult.to_json())

# convert the object into a dict
monitored_item_create_result_dict = monitored_item_create_result_instance.to_dict()
# create an instance of MonitoredItemCreateResult from a dict
monitored_item_create_result_from_dict = MonitoredItemCreateResult.from_dict(monitored_item_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


