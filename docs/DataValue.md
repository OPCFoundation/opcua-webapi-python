# DataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ua_type** | **int** |  | [optional] [default to 0]
**value** | **object** |  | [optional] 
**status_code** | [**StatusCode**](StatusCode.md) |  | [optional] 
**source_timestamp** | **datetime** |  | [optional] 
**source_picoseconds** | **int** |  | [optional] 
**server_timestamp** | **datetime** |  | [optional] 
**server_picoseconds** | **int** |  | [optional] 

## Example

```python
from opcua_webapi.models.data_value import DataValue

# TODO update the JSON string below
json = "{}"
# create an instance of DataValue from a JSON string
data_value_instance = DataValue.from_json(json)
# print the JSON string representation of the object
print(DataValue.to_json())

# convert the object into a dict
data_value_dict = data_value_instance.to_dict()
# create an instance of DataValue from a dict
data_value_from_dict = DataValue.from_dict(data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


