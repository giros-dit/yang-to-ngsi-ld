# NetworkNodeSupportingNode

NGSI-LD Entity Type that represents another node that is in an underlay network and that supports this node. Used to represent layering structure. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkNodeSupportingNode. | [optional] [default to 'NetworkNodeSupportingNode']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**network_ref** | [**NetworkRef**](NetworkRef.md) |  | 
**node_ref** | [**NodeRef**](NodeRef.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_node_supporting_node import NetworkNodeSupportingNode

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkNodeSupportingNode from a JSON string
network_node_supporting_node_instance = NetworkNodeSupportingNode.from_json(json)
# print the JSON string representation of the object
print NetworkNodeSupportingNode.to_json()

# convert the object into a dict
network_node_supporting_node_dict = network_node_supporting_node_instance.to_dict()
# create an instance of NetworkNodeSupportingNode from a dict
network_node_supporting_node_form_dict = network_node_supporting_node.from_dict(network_node_supporting_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


