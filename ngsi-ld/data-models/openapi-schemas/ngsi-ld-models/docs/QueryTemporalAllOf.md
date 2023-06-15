# QueryTemporalAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temporal_q** | [**TemporalQuery**](TemporalQuery.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.query_temporal_all_of import QueryTemporalAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTemporalAllOf from a JSON string
query_temporal_all_of_instance = QueryTemporalAllOf.from_json(json)
# print the JSON string representation of the object
print QueryTemporalAllOf.to_json()

# convert the object into a dict
query_temporal_all_of_dict = query_temporal_all_of_instance.to_dict()
# create an instance of QueryTemporalAllOf from a dict
query_temporal_all_of_form_dict = query_temporal_all_of.from_dict(query_temporal_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


