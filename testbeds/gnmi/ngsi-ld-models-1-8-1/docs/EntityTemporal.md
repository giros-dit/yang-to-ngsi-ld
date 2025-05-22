# EntityTemporal

5.2.20 This is the same data type as mandated by clause 5.2.4 with the only deviation that the representation of Properties and Relationships shall be the temporal one (arrays of (Property or Relationship) instances represented by JSON-LD objects) as defined in clauses 4.5.7 and 4.5.8. Alternatively it is possible to specify the EntityTemporal by using the \"Simplified Temporal Representation of an Entity\", as defined in clause 4.5.9. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 

## Example

```python
from ngsi_ld_models_1_8_1.models.entity_temporal import EntityTemporal

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTemporal from a JSON string
entity_temporal_instance = EntityTemporal.from_json(json)
# print the JSON string representation of the object
print(EntityTemporal.to_json())

# convert the object into a dict
entity_temporal_dict = entity_temporal_instance.to_dict()
# create an instance of EntityTemporal from a dict
entity_temporal_from_dict = EntityTemporal.from_dict(entity_temporal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


