# AggregateConfiguration

[Link to specification](https://reference.opcfoundation.org/v105/Core/docs/Part4/7.22.4).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_server_capabilities_defaults** | **bool** |  | [optional] [default to False]
**treat_uncertain_as_bad** | **bool** |  | [optional] [default to False]
**percent_data_bad** | **int** |  | [optional] [default to 0]
**percent_data_good** | **int** |  | [optional] [default to 0]
**use_sloped_extrapolation** | **bool** |  | [optional] [default to False]

## Example

```python
from opcua_webapi.models.aggregate_configuration import AggregateConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateConfiguration from a JSON string
aggregate_configuration_instance = AggregateConfiguration.from_json(json)
# print the JSON string representation of the object
print(AggregateConfiguration.to_json())

# convert the object into a dict
aggregate_configuration_dict = aggregate_configuration_instance.to_dict()
# create an instance of AggregateConfiguration from a dict
aggregate_configuration_from_dict = AggregateConfiguration.from_dict(aggregate_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


