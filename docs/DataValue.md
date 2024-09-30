# DataValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Variant**](Variant.md) |  | [optional] 
**status_code** | **int** |  | [optional] 
**source_timestamp** | **datetime** |  | [optional] 
**source_pico_seconds** | **int** |  | [optional] 
**server_timestamp** | **datetime** |  | [optional] 
**server_pico_seconds** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.data_value import DataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DataValue from a JSON string
data_value_instance = DataValue.from_json(json)
# print the JSON string representation of the object
print DataValue.to_json()

# convert the object into a dict
data_value_dict = data_value_instance.to_dict()
# create an instance of DataValue from a dict
data_value_form_dict = data_value.from_dict(data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


