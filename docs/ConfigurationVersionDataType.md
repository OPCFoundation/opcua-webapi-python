# ConfigurationVersionDataType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**major_version** | **int** |  | [optional] [default to 0]
**minor_version** | **int** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.configuration_version_data_type import ConfigurationVersionDataType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationVersionDataType from a JSON string
configuration_version_data_type_instance = ConfigurationVersionDataType.from_json(json)
# print the JSON string representation of the object
print(ConfigurationVersionDataType.to_json())

# convert the object into a dict
configuration_version_data_type_dict = configuration_version_data_type_instance.to_dict()
# create an instance of ConfigurationVersionDataType from a dict
configuration_version_data_type_from_dict = ConfigurationVersionDataType.from_dict(configuration_version_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


