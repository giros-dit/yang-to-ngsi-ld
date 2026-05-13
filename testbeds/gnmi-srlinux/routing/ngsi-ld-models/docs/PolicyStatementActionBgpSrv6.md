# PolicyStatementActionBgpSrv6

Enter the srv6 context  YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be PolicyStatementActionBgpSrv6. | [default to 'PolicyStatementActionBgpSrv6']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**locator** | [**PolicyStatementActionBgpSrv6Locator**](PolicyStatementActionBgpSrv6Locator.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.policy_statement_action_bgp_srv6 import PolicyStatementActionBgpSrv6

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyStatementActionBgpSrv6 from a JSON string
policy_statement_action_bgp_srv6_instance = PolicyStatementActionBgpSrv6.from_json(json)
# print the JSON string representation of the object
print(PolicyStatementActionBgpSrv6.to_json())

# convert the object into a dict
policy_statement_action_bgp_srv6_dict = policy_statement_action_bgp_srv6_instance.to_dict()
# create an instance of PolicyStatementActionBgpSrv6 from a dict
policy_statement_action_bgp_srv6_from_dict = PolicyStatementActionBgpSrv6.from_dict(policy_statement_action_bgp_srv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


