# InterfaceEthernetStateCounters

Ethernet interface counters  YANG module: openconfig-if-ethernet.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceEthernetStateCounters. | [default to 'InterfaceEthernetStateCounters']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_mac_control_frames** | [**InMacControlFrames**](InMacControlFrames.md) |  | [optional] 
**in_mac_pause_frames** | [**InMacPauseFrames**](InMacPauseFrames.md) |  | [optional] 
**in_oversize_frames** | [**InOversizeFrames**](InOversizeFrames.md) |  | [optional] 
**in_jabber_frames** | [**InJabberFrames**](InJabberFrames.md) |  | [optional] 
**in_fragment_frames** | [**InFragmentFrames**](InFragmentFrames.md) |  | [optional] 
**in8021q_frames** | [**In8021qFrames**](In8021qFrames.md) |  | [optional] 
**in_crc_errors** | [**InCrcErrors**](InCrcErrors.md) |  | [optional] 
**out_mac_control_frames** | [**OutMacControlFrames**](OutMacControlFrames.md) |  | [optional] 
**out_mac_pause_frames** | [**OutMacPauseFrames**](OutMacPauseFrames.md) |  | [optional] 
**out8021q_frames** | [**Out8021qFrames**](Out8021qFrames.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ethernet_state_counters import InterfaceEthernetStateCounters

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceEthernetStateCounters from a JSON string
interface_ethernet_state_counters_instance = InterfaceEthernetStateCounters.from_json(json)
# print the JSON string representation of the object
print InterfaceEthernetStateCounters.to_json()

# convert the object into a dict
interface_ethernet_state_counters_dict = interface_ethernet_state_counters_instance.to_dict()
# create an instance of InterfaceEthernetStateCounters from a dict
interface_ethernet_state_counters_form_dict = interface_ethernet_state_counters.from_dict(interface_ethernet_state_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


