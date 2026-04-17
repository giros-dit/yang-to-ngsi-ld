# PolicyStatementMatchPrefix

 YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be PolicyStatementMatchPrefix. | [default to 'PolicyStatementMatchPrefix']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**prefix_set** | [**PolicyStatementMatchPrefixPrefixSet**](PolicyStatementMatchPrefixPrefixSet.md) |  | [optional] 
**match_set_options** | [**PolicyStatementMatchPrefixMatchSetOptions**](PolicyStatementMatchPrefixMatchSetOptions.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.policy_statement_match_prefix import PolicyStatementMatchPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyStatementMatchPrefix from a JSON string
policy_statement_match_prefix_instance = PolicyStatementMatchPrefix.from_json(json)
# print the JSON string representation of the object
print(PolicyStatementMatchPrefix.to_json())

# convert the object into a dict
policy_statement_match_prefix_dict = policy_statement_match_prefix_instance.to_dict()
# create an instance of PolicyStatementMatchPrefix from a dict
policy_statement_match_prefix_from_dict = PolicyStatementMatchPrefix.from_dict(policy_statement_match_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


