# TemporalQuery

5.2.21 This datatype represents a temporal query. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timerel** | **str** | Allowed values: \&quot;before\&quot;, \&quot;after\&quot; and \&quot;between\&quot;.  | 
**time_at** | **datetime** | It shall be a DateTime.  | 
**end_time_at** | **datetime** | It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \&quot;between\&quot;.  | [optional] 
**timeproperty** | **str** | Allowed values: \&quot;observedAt\&quot;, \&quot;createdAt\&quot;, \&quot;modifiedAt\&quot; and \&quot;deletedAt\&quot;. If not specified, the default is \&quot;observedAt\&quot;. (See clause 4.8).  | [optional] [default to 'observedAt']

## Example

```python
from ngsi_ld_models.models.temporal_query import TemporalQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TemporalQuery from a JSON string
temporal_query_instance = TemporalQuery.from_json(json)
# print the JSON string representation of the object
print TemporalQuery.to_json()

# convert the object into a dict
temporal_query_dict = temporal_query_instance.to_dict()
# create an instance of TemporalQuery from a dict
temporal_query_form_dict = temporal_query.from_dict(temporal_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


