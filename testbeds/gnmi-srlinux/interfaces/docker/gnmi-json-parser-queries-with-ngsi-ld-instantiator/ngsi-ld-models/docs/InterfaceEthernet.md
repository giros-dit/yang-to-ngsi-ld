# InterfaceEthernet

 YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceEthernet. | [default to 'InterfaceEthernet']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**aggregate_id** | [**AggregateId**](AggregateId.md) |  | [optional] 
**forwarding_viable** | [**ForwardingViable**](ForwardingViable.md) |  | [optional] 
**auto_negotiate** | [**AutoNegotiate**](AutoNegotiate.md) |  | [optional] 
**duplex_mode** | [**DuplexMode**](DuplexMode.md) |  | [optional] 
**dac_link_training** | [**DacLinkTraining**](DacLinkTraining.md) |  | [optional] 
**lacp_port_priority** | [**LacpPortPriority**](LacpPortPriority.md) |  | [optional] 
**port_speed** | [**PortSpeed**](PortSpeed.md) |  | [optional] 
**hw_mac_address** | [**HwMacAddress**](HwMacAddress.md) |  | [optional] 
**mac_address** | [**MacAddress**](MacAddress.md) |  | [optional] 
**physical_medium** | [**PhysicalMedium**](PhysicalMedium.md) |  | [optional] 
**ptp_asymmetry** | [**PtpAsymmetry**](PtpAsymmetry.md) |  | [optional] 
**standby_signaling** | [**StandbySignaling**](StandbySignaling.md) |  | [optional] 
**reload_delay** | [**ReloadDelay**](ReloadDelay.md) |  | [optional] 
**reload_delay_expires** | [**ReloadDelayExpires**](ReloadDelayExpires.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ethernet import InterfaceEthernet

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceEthernet from a JSON string
interface_ethernet_instance = InterfaceEthernet.from_json(json)
# print the JSON string representation of the object
print InterfaceEthernet.to_json()

# convert the object into a dict
interface_ethernet_dict = interface_ethernet_instance.to_dict()
# create an instance of InterfaceEthernet from a dict
interface_ethernet_form_dict = interface_ethernet.from_dict(interface_ethernet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


