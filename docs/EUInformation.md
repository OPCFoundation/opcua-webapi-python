# EUInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_uri** | **str** |  | [optional] 
**unit_id** | **int** |  | [optional] 
**display_name** | [**LocalizedText**](LocalizedText.md) |  | [optional] 
**description** | [**LocalizedText**](LocalizedText.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.eu_information import EUInformation

# TODO update the JSON string below
json = "{}"
# create an instance of EUInformation from a JSON string
eu_information_instance = EUInformation.from_json(json)
# print the JSON string representation of the object
print(EUInformation.to_json())

# convert the object into a dict
eu_information_dict = eu_information_instance.to_dict()
# create an instance of EUInformation from a dict
eu_information_from_dict = EUInformation.from_dict(eu_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


