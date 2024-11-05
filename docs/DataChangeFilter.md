# DataChangeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | **int** |  | [optional] 
**deadband_type** | **int** |  | [optional] [default to 0]
**deadband_value** | **float** |  | [optional] [default to 0]

## Example

```python
from opcua_webapi.models.data_change_filter import DataChangeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DataChangeFilter from a JSON string
data_change_filter_instance = DataChangeFilter.from_json(json)
# print the JSON string representation of the object
print(DataChangeFilter.to_json())

# convert the object into a dict
data_change_filter_dict = data_change_filter_instance.to_dict()
# create an instance of DataChangeFilter from a dict
data_change_filter_from_dict = DataChangeFilter.from_dict(data_change_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


