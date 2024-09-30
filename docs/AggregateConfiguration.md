# AggregateConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_server_capabilities_defaults** | **bool** |  | [optional] 
**treat_uncertain_as_bad** | **bool** |  | [optional] 
**percent_data_bad** | **int** |  | [optional] 
**percent_data_good** | **int** |  | [optional] 
**use_sloped_extrapolation** | **bool** |  | [optional] 

## Example

```python
from opcua_webapi.models.aggregate_configuration import AggregateConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateConfiguration from a JSON string
aggregate_configuration_instance = AggregateConfiguration.from_json(json)
# print the JSON string representation of the object
print AggregateConfiguration.to_json()

# convert the object into a dict
aggregate_configuration_dict = aggregate_configuration_instance.to_dict()
# create an instance of AggregateConfiguration from a dict
aggregate_configuration_form_dict = aggregate_configuration.from_dict(aggregate_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


