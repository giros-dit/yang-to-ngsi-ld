# PolicyStatementMatchMulticastGroupAddress

Multicast group IP address  To match a <S,G> the source needs to be present in the multicast source-address leafref and the group needs to present in the group-address leafref. To match a <*,G> the group has to be programmed in the group-address leafref and no source in the source-address leafref. Group address can be configured as a prefix.  YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be PolicyStatementMatchMulticastGroupAddress. | [default to 'PolicyStatementMatchMulticastGroupAddress']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**prefix_set** | [**PolicyStatementMatchMulticastGroupAddressPrefixSet**](PolicyStatementMatchMulticastGroupAddressPrefixSet.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.policy_statement_match_multicast_group_address import PolicyStatementMatchMulticastGroupAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyStatementMatchMulticastGroupAddress from a JSON string
policy_statement_match_multicast_group_address_instance = PolicyStatementMatchMulticastGroupAddress.from_json(json)
# print the JSON string representation of the object
print(PolicyStatementMatchMulticastGroupAddress.to_json())

# convert the object into a dict
policy_statement_match_multicast_group_address_dict = policy_statement_match_multicast_group_address_instance.to_dict()
# create an instance of PolicyStatementMatchMulticastGroupAddress from a dict
policy_statement_match_multicast_group_address_from_dict = PolicyStatementMatchMulticastGroupAddress.from_dict(policy_statement_match_multicast_group_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


