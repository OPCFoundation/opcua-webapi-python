# JsonApplicationDescriptionMessage

[Link to specification]().

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**message_type** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | [**ApplicationDescription**](ApplicationDescription.md) |  | [optional] 
**server_capabilities** | **List[str]** |  | [optional] 

## Example

```python
from opcua_webapi.models.json_application_description_message import JsonApplicationDescriptionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApplicationDescriptionMessage from a JSON string
json_application_description_message_instance = JsonApplicationDescriptionMessage.from_json(json)
# print the JSON string representation of the object
print(JsonApplicationDescriptionMessage.to_json())

# convert the object into a dict
json_application_description_message_dict = json_application_description_message_instance.to_dict()
# create an instance of JsonApplicationDescriptionMessage from a dict
json_application_description_message_from_dict = JsonApplicationDescriptionMessage.from_dict(json_application_description_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


