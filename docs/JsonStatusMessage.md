# JsonStatusMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**is_cyclic** | **bool** |  | [optional] [default to False]
**status** | **int** | [Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part14/6.2.1). | [optional] 
**next_report_time** | **datetime** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_status_message import JsonStatusMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonStatusMessage from a JSON string
json_status_message_instance = JsonStatusMessage.from_json(json)
# print the JSON string representation of the object
print(JsonStatusMessage.to_json())

# convert the object into a dict
json_status_message_dict = json_status_message_instance.to_dict()
# create an instance of JsonStatusMessage from a dict
json_status_message_from_dict = JsonStatusMessage.from_dict(json_status_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


