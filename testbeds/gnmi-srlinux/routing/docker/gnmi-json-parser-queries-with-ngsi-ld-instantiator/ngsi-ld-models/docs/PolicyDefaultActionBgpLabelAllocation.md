# PolicyDefaultActionBgpLabelAllocation

Actions that determine the method used to assign labels to BGP LU routes matched and accepted by route-table-import policies  YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be PolicyDefaultActionBgpLabelAllocation. | [default to 'PolicyDefaultActionBgpLabelAllocation']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.policy_default_action_bgp_label_allocation import PolicyDefaultActionBgpLabelAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyDefaultActionBgpLabelAllocation from a JSON string
policy_default_action_bgp_label_allocation_instance = PolicyDefaultActionBgpLabelAllocation.from_json(json)
# print the JSON string representation of the object
print(PolicyDefaultActionBgpLabelAllocation.to_json())

# convert the object into a dict
policy_default_action_bgp_label_allocation_dict = policy_default_action_bgp_label_allocation_instance.to_dict()
# create an instance of PolicyDefaultActionBgpLabelAllocation from a dict
policy_default_action_bgp_label_allocation_from_dict = PolicyDefaultActionBgpLabelAllocation.from_dict(policy_default_action_bgp_label_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


