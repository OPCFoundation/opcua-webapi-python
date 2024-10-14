# AggregateFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**aggregate_type** | **str** |  | [optional] 
**processing_interval** | **float** |  | [optional] 
**aggregate_configuration** | [**AggregateConfiguration**](AggregateConfiguration.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.aggregate_filter import AggregateFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateFilter from a JSON string
aggregate_filter_instance = AggregateFilter.from_json(json)
# print the JSON string representation of the object
print(AggregateFilter.to_json())

# convert the object into a dict
aggregate_filter_dict = aggregate_filter_instance.to_dict()
# create an instance of AggregateFilter from a dict
aggregate_filter_from_dict = AggregateFilter.from_dict(aggregate_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


