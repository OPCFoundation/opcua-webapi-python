# MonitoringParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_handle** | **int** |  | [optional] 
**sampling_interval** | **float** |  | [optional] 
**filter** | [**ExtensionObject**](ExtensionObject.md) |  | [optional] 
**queue_size** | **int** |  | [optional] 
**discard_oldest** | **bool** |  | [optional] 

## Example

```python
from opcua_webapi.models.monitoring_parameters import MonitoringParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringParameters from a JSON string
monitoring_parameters_instance = MonitoringParameters.from_json(json)
# print the JSON string representation of the object
print(MonitoringParameters.to_json())

# convert the object into a dict
monitoring_parameters_dict = monitoring_parameters_instance.to_dict()
# create an instance of MonitoringParameters from a dict
monitoring_parameters_from_dict = MonitoringParameters.from_dict(monitoring_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


