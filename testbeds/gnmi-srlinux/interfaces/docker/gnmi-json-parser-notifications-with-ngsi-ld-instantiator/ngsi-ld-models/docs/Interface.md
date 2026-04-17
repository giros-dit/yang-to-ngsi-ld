# Interface

The list of named interfaces on the device  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be Interface. | [default to 'Interface']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**InterfaceName**](InterfaceName.md) |  | 
**description** | [**InterfaceDescription**](InterfaceDescription.md) |  | [optional] 
**admin_state** | [**InterfaceAdminState**](InterfaceAdminState.md) |  | [optional] 
**mtu** | [**Mtu**](Mtu.md) |  | [optional] 
**ifindex** | [**InterfaceIfindex**](InterfaceIfindex.md) |  | [optional] 
**oper_state** | [**InterfaceOperState**](InterfaceOperState.md) |  | [optional] 
**oper_down_reason** | [**InterfaceOperDownReason**](InterfaceOperDownReason.md) |  | [optional] 
**last_change** | [**InterfaceLastChange**](InterfaceLastChange.md) |  | [optional] 
**linecard** | [**InterfaceLinecard**](InterfaceLinecard.md) |  | [optional] 
**forwarding_complex** | [**InterfaceForwardingComplex**](InterfaceForwardingComplex.md) |  | [optional] 
**phy_group_members** | [**PhyGroupMembers**](PhyGroupMembers.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print Interface.to_json()

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_form_dict = interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


