# InterfaceSubinterface

The list of subinterfaces (logical interfaces) associated with a physical interface  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterface. | [default to 'InterfaceSubinterface']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**index** | [**InterfaceSubinterfaceIndex**](InterfaceSubinterfaceIndex.md) |  | [optional] 
**subinterface_type** | [**InterfaceSubinterfaceType**](InterfaceSubinterfaceType.md) |  | [optional] 
**description** | [**InterfaceSubinterfaceDescription**](InterfaceSubinterfaceDescription.md) |  | [optional] 
**admin_state** | [**InterfaceSubinterfaceAdminState**](InterfaceSubinterfaceAdminState.md) |  | [optional] 
**ip_mtu** | [**IpMtu**](IpMtu.md) |  | [optional] 
**l2_mtu** | [**L2Mtu**](L2Mtu.md) |  | [optional] 
**mpls_mtu** | [**MplsMtu**](MplsMtu.md) |  | [optional] 
**name** | [**InterfaceSubinterfaceName**](InterfaceSubinterfaceName.md) |  | [optional] 
**ifindex** | [**InterfaceSubinterfaceIfindex**](InterfaceSubinterfaceIfindex.md) |  | [optional] 
**oper_state** | [**InterfaceSubinterfaceOperState**](InterfaceSubinterfaceOperState.md) |  | [optional] 
**oper_down_reason** | [**InterfaceSubinterfaceOperDownReason**](InterfaceSubinterfaceOperDownReason.md) |  | [optional] 
**last_change** | [**InterfaceSubinterfaceLastChange**](InterfaceSubinterfaceLastChange.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterface import InterfaceSubinterface

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterface from a JSON string
interface_subinterface_instance = InterfaceSubinterface.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterface.to_json()

# convert the object into a dict
interface_subinterface_dict = interface_subinterface_instance.to_dict()
# create an instance of InterfaceSubinterface from a dict
interface_subinterface_form_dict = interface_subinterface.from_dict(interface_subinterface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


