# InterfaceAggregationState

Operational state variables for logical aggregate / LAG interfaces  YANG module: openconfig-if-aggregate.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceAggregationState. | [default to 'InterfaceAggregationState']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**lag_type** | [**InterfaceAggregationStateLagType**](InterfaceAggregationStateLagType.md) |  | [optional] 
**min_links** | [**InterfaceAggregationStateMinLinks**](InterfaceAggregationStateMinLinks.md) |  | [optional] 
**lag_speed** | [**LagSpeed**](LagSpeed.md) |  | [optional] 
**member** | [**InterfaceAggregationStateMember**](InterfaceAggregationStateMember.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_aggregation_state import InterfaceAggregationState

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceAggregationState from a JSON string
interface_aggregation_state_instance = InterfaceAggregationState.from_json(json)
# print the JSON string representation of the object
print InterfaceAggregationState.to_json()

# convert the object into a dict
interface_aggregation_state_dict = interface_aggregation_state_instance.to_dict()
# create an instance of InterfaceAggregationState from a dict
interface_aggregation_state_form_dict = interface_aggregation_state.from_dict(interface_aggregation_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


