# PolicyStatementMatch

Match conditions of the policy statement  YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be PolicyStatementMatch. | [default to 'PolicyStatementMatch']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**family** | [**Family**](Family.md) |  | [optional] 
**protocol** | [**Protocol**](Protocol.md) |  | [optional] 
**call_policy** | [**CallPolicy**](CallPolicy.md) |  | [optional] 
**origin_network_instance** | [**PolicyStatementMatchOriginNetworkInstance**](PolicyStatementMatchOriginNetworkInstance.md) |  | [optional] 
**network_instance_leaked_route** | [**NetworkInstanceLeakedRoute**](NetworkInstanceLeakedRoute.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.policy_statement_match import PolicyStatementMatch

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyStatementMatch from a JSON string
policy_statement_match_instance = PolicyStatementMatch.from_json(json)
# print the JSON string representation of the object
print(PolicyStatementMatch.to_json())

# convert the object into a dict
policy_statement_match_dict = policy_statement_match_instance.to_dict()
# create an instance of PolicyStatementMatch from a dict
policy_statement_match_from_dict = PolicyStatementMatch.from_dict(policy_statement_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


