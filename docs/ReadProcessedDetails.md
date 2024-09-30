# ReadProcessedDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**processing_interval** | **float** |  | [optional] 
**aggregate_type** | **List[str]** |  | [optional] 
**aggregate_configuration** | [**AggregateConfiguration**](AggregateConfiguration.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.read_processed_details import ReadProcessedDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReadProcessedDetails from a JSON string
read_processed_details_instance = ReadProcessedDetails.from_json(json)
# print the JSON string representation of the object
print ReadProcessedDetails.to_json()

# convert the object into a dict
read_processed_details_dict = read_processed_details_instance.to_dict()
# create an instance of ReadProcessedDetails from a dict
read_processed_details_form_dict = read_processed_details.from_dict(read_processed_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


