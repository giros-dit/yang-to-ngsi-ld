# LinecardForwardingComplex

List of forwarding complexes on the linecard  YANG module: srl_nokia-platform-lc.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be LinecardForwardingComplex. | [default to 'LinecardForwardingComplex']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**LinecardForwardingComplexName**](LinecardForwardingComplexName.md) |  | [optional] 
**interfaces** | [**Interfaces**](Interfaces.md) |  | [optional] 
**oper_state** | [**LinecardForwardingComplexOperState**](LinecardForwardingComplexOperState.md) |  | [optional] 
**last_booted** | [**LinecardForwardingComplexLastBooted**](LinecardForwardingComplexLastBooted.md) |  | [optional] 
**last_booted_reason** | [**LinecardForwardingComplexLastBootedReason**](LinecardForwardingComplexLastBootedReason.md) |  | [optional] 
**last_change** | [**LinecardForwardingComplexLastChange**](LinecardForwardingComplexLastChange.md) |  | [optional] 
**part_number** | [**LinecardForwardingComplexPartNumber**](LinecardForwardingComplexPartNumber.md) |  | [optional] 
**removable** | [**LinecardForwardingComplexRemovable**](LinecardForwardingComplexRemovable.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.linecard_forwarding_complex import LinecardForwardingComplex

# TODO update the JSON string below
json = "{}"
# create an instance of LinecardForwardingComplex from a JSON string
linecard_forwarding_complex_instance = LinecardForwardingComplex.from_json(json)
# print the JSON string representation of the object
print LinecardForwardingComplex.to_json()

# convert the object into a dict
linecard_forwarding_complex_dict = linecard_forwarding_complex_instance.to_dict()
# create an instance of LinecardForwardingComplex from a dict
linecard_forwarding_complex_form_dict = linecard_forwarding_complex.from_dict(linecard_forwarding_complex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


