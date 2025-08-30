# LocalizedText

[Link to specification](https://reference.opcfoundation.org/Core/Part3/v105/docs/8.5).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from opcua_webapi.models.localized_text import LocalizedText

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedText from a JSON string
localized_text_instance = LocalizedText.from_json(json)
# print the JSON string representation of the object
print(LocalizedText.to_json())

# convert the object into a dict
localized_text_dict = localized_text_instance.to_dict()
# create an instance of LocalizedText from a dict
localized_text_from_dict = LocalizedText.from_dict(localized_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


