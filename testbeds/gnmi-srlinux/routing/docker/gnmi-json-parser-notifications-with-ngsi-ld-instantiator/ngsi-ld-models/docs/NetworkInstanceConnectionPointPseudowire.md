# NetworkInstanceConnectionPointPseudowire

Pseudowire that can be used for this connection point  Multiple pseudowires can be configured within the same connection point. The active pseudowire is selected based on the precedence that it is configured with the endpoint.  YANG module: srl_nokia-network-instance.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceConnectionPointPseudowire. | [default to 'NetworkInstanceConnectionPointPseudowire']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**NetworkInstanceConnectionPointPseudowireName**](NetworkInstanceConnectionPointPseudowireName.md) |  | [optional] 
**admin_state** | [**NetworkInstanceConnectionPointPseudowireAdminState**](NetworkInstanceConnectionPointPseudowireAdminState.md) |  | [optional] 
**oper_state** | [**NetworkInstanceConnectionPointPseudowireOperState**](NetworkInstanceConnectionPointPseudowireOperState.md) |  | [optional] 
**oper_down_reason** | [**NetworkInstanceConnectionPointPseudowireOperDownReason**](NetworkInstanceConnectionPointPseudowireOperDownReason.md) |  | [optional] 
**index** | [**NetworkInstanceConnectionPointPseudowireIndex**](NetworkInstanceConnectionPointPseudowireIndex.md) |  | [optional] 
**destination_index** | [**DestinationIndex**](DestinationIndex.md) |  | [optional] 
**last_change** | [**NetworkInstanceConnectionPointPseudowireLastChange**](NetworkInstanceConnectionPointPseudowireLastChange.md) |  | [optional] 
**pw_tunnel** | [**PwTunnel**](PwTunnel.md) |  | 
**control_word** | [**ControlWord**](ControlWord.md) |  | [optional] 
**flow_label** | [**FlowLabel**](FlowLabel.md) |  | [optional] 
**flow_label_oper_state** | [**FlowLabelOperState**](FlowLabelOperState.md) |  | [optional] 
**precedence** | [**Precedence**](Precedence.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_connection_point_pseudowire import NetworkInstanceConnectionPointPseudowire

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceConnectionPointPseudowire from a JSON string
network_instance_connection_point_pseudowire_instance = NetworkInstanceConnectionPointPseudowire.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceConnectionPointPseudowire.to_json())

# convert the object into a dict
network_instance_connection_point_pseudowire_dict = network_instance_connection_point_pseudowire_instance.to_dict()
# create an instance of NetworkInstanceConnectionPointPseudowire from a dict
network_instance_connection_point_pseudowire_from_dict = NetworkInstanceConnectionPointPseudowire.from_dict(network_instance_connection_point_pseudowire_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


