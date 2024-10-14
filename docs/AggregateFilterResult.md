# AggregateFilterResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revised_start_time** | **datetime** |  | [optional] 
**revised_processing_interval** | **float** |  | [optional] 
**revised_aggregate_configuration** | [**AggregateConfiguration**](AggregateConfiguration.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.aggregate_filter_result import AggregateFilterResult

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateFilterResult from a JSON string
aggregate_filter_result_instance = AggregateFilterResult.from_json(json)
# print the JSON string representation of the object
print(AggregateFilterResult.to_json())

# convert the object into a dict
aggregate_filter_result_dict = aggregate_filter_result_instance.to_dict()
# create an instance of AggregateFilterResult from a dict
aggregate_filter_result_from_dict = AggregateFilterResult.from_dict(aggregate_filter_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


