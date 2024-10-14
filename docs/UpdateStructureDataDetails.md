# UpdateStructureDataDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**perform_insert_replace** | **int** |  | [optional] 
**update_values** | [**List[DataValue]**](DataValue.md) |  | [optional] 

## Example

```python
from opcua_webapi.models.update_structure_data_details import UpdateStructureDataDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStructureDataDetails from a JSON string
update_structure_data_details_instance = UpdateStructureDataDetails.from_json(json)
# print the JSON string representation of the object
print(UpdateStructureDataDetails.to_json())

# convert the object into a dict
update_structure_data_details_dict = update_structure_data_details_instance.to_dict()
# create an instance of UpdateStructureDataDetails from a dict
update_structure_data_details_from_dict = UpdateStructureDataDetails.from_dict(update_structure_data_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


