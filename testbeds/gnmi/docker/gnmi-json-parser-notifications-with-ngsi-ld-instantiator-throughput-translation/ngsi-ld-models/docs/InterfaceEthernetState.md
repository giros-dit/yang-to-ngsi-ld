# InterfaceEthernetState

State variables for Ethernet interfaces  YANG module: openconfig-if-ethernet.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceEthernetState. | [default to 'InterfaceEthernetState']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**mac_address** | [**InterfaceEthernetStateMacAddress**](InterfaceEthernetStateMacAddress.md) |  | [optional] 
**auto_negotiate** | [**InterfaceEthernetStateAutoNegotiate**](InterfaceEthernetStateAutoNegotiate.md) |  | [optional] 
**duplex_mode** | [**InterfaceEthernetStateDuplexMode**](InterfaceEthernetStateDuplexMode.md) |  | [optional] 
**port_speed** | [**InterfaceEthernetStatePortSpeed**](InterfaceEthernetStatePortSpeed.md) |  | [optional] 
**enable_flow_control** | [**InterfaceEthernetStateEnableFlowControl**](InterfaceEthernetStateEnableFlowControl.md) |  | [optional] 
**hw_mac_address** | [**HwMacAddress**](HwMacAddress.md) |  | [optional] 
**negotiated_duplex_mode** | [**NegotiatedDuplexMode**](NegotiatedDuplexMode.md) |  | [optional] 
**negotiated_port_speed** | [**NegotiatedPortSpeed**](NegotiatedPortSpeed.md) |  | [optional] 
**aggregate_id** | [**InterfaceEthernetStateAggregateId**](InterfaceEthernetStateAggregateId.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ethernet_state import InterfaceEthernetState

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceEthernetState from a JSON string
interface_ethernet_state_instance = InterfaceEthernetState.from_json(json)
# print the JSON string representation of the object
print InterfaceEthernetState.to_json()

# convert the object into a dict
interface_ethernet_state_dict = interface_ethernet_state_instance.to_dict()
# create an instance of InterfaceEthernetState from a dict
interface_ethernet_state_form_dict = interface_ethernet_state.from_dict(interface_ethernet_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


