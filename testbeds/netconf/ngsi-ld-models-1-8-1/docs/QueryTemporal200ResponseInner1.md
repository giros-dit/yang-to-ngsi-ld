# QueryTemporal200ResponseInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | 
**type** | [**EntityType**](EntityType.md) |  | 
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | 

## Example

```python
from ngsi_ld_models_1_8_1.models.query_temporal200_response_inner1 import QueryTemporal200ResponseInner1

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTemporal200ResponseInner1 from a JSON string
query_temporal200_response_inner1_instance = QueryTemporal200ResponseInner1.from_json(json)
# print the JSON string representation of the object
print(QueryTemporal200ResponseInner1.to_json())

# convert the object into a dict
query_temporal200_response_inner1_dict = query_temporal200_response_inner1_instance.to_dict()
# create an instance of QueryTemporal200ResponseInner1 from a dict
query_temporal200_response_inner1_from_dict = QueryTemporal200ResponseInner1.from_dict(query_temporal200_response_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

