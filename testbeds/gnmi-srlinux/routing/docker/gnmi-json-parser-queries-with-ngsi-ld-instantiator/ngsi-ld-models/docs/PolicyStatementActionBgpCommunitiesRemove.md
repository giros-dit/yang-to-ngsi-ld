# PolicyStatementActionBgpCommunitiesRemove

Reference to a community-set name  The communities in the route are compared to all of the community members in the referenced community-set, and all matching communities are removed from the COMMUNITIES and LARGE_COMMUNITIES attributes.  YANG module: srl_nokia-routing-policy.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Relationship']
**object** | **str** | Relationship with Entity type CommunitySet. | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of target relationship objects.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Relationship instance (see clause 4.5.8). System generated.  | [optional] [readonly] 
**previous_object** | **str** | Previous Relationship&#39;s target object. Only used in notifications.  | [optional] [readonly] 

## Example

```python
from ngsi_ld_models.models.policy_statement_action_bgp_communities_remove import PolicyStatementActionBgpCommunitiesRemove

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyStatementActionBgpCommunitiesRemove from a JSON string
policy_statement_action_bgp_communities_remove_instance = PolicyStatementActionBgpCommunitiesRemove.from_json(json)
# print the JSON string representation of the object
print(PolicyStatementActionBgpCommunitiesRemove.to_json())

# convert the object into a dict
policy_statement_action_bgp_communities_remove_dict = policy_statement_action_bgp_communities_remove_instance.to_dict()
# create an instance of PolicyStatementActionBgpCommunitiesRemove from a dict
policy_statement_action_bgp_communities_remove_from_dict = PolicyStatementActionBgpCommunitiesRemove.from_dict(policy_statement_action_bgp_communities_remove_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


