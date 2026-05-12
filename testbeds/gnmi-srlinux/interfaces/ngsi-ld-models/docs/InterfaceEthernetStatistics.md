# InterfaceEthernetStatistics

 YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceEthernetStatistics. | [default to 'InterfaceEthernetStatistics']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**in_mac_pause_frames** | [**InMacPauseFrames**](InMacPauseFrames.md) |  | [optional] 
**in_oversize_frames** | [**InOversizeFrames**](InOversizeFrames.md) |  | [optional] 
**in_jabber_frames** | [**InJabberFrames**](InJabberFrames.md) |  | [optional] 
**in_fragment_frames** | [**InFragmentFrames**](InFragmentFrames.md) |  | [optional] 
**in_crc_error_frames** | [**InCrcErrorFrames**](InCrcErrorFrames.md) |  | [optional] 
**out_mac_pause_frames** | [**OutMacPauseFrames**](OutMacPauseFrames.md) |  | [optional] 
**in64b_frames** | [**In64bFrames**](In64bFrames.md) |  | [optional] 
**in65b_to127b_frames** | [**In65bTo127bFrames**](In65bTo127bFrames.md) |  | [optional] 
**in128b_to255b_frames** | [**In128bTo255bFrames**](In128bTo255bFrames.md) |  | [optional] 
**in256b_to511b_frames** | [**In256bTo511bFrames**](In256bTo511bFrames.md) |  | [optional] 
**in512b_to1023b_frames** | [**In512bTo1023bFrames**](In512bTo1023bFrames.md) |  | [optional] 
**in1024b_to1518b_frames** | [**In1024bTo1518bFrames**](In1024bTo1518bFrames.md) |  | [optional] 
**in1519b_or_longer_frames** | [**In1519bOrLongerFrames**](In1519bOrLongerFrames.md) |  | [optional] 
**out64b_frames** | [**Out64bFrames**](Out64bFrames.md) |  | [optional] 
**out65b_to127b_frames** | [**Out65bTo127bFrames**](Out65bTo127bFrames.md) |  | [optional] 
**out128b_to255b_frames** | [**Out128bTo255bFrames**](Out128bTo255bFrames.md) |  | [optional] 
**out256b_to511b_frames** | [**Out256bTo511bFrames**](Out256bTo511bFrames.md) |  | [optional] 
**out512b_to1023b_frames** | [**Out512bTo1023bFrames**](Out512bTo1023bFrames.md) |  | [optional] 
**out1024b_to1518b_frames** | [**Out1024bTo1518bFrames**](Out1024bTo1518bFrames.md) |  | [optional] 
**out1519b_or_longer_frames** | [**Out1519bOrLongerFrames**](Out1519bOrLongerFrames.md) |  | [optional] 
**last_clear** | [**InterfaceEthernetStatisticsLastClear**](InterfaceEthernetStatisticsLastClear.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ethernet_statistics import InterfaceEthernetStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceEthernetStatistics from a JSON string
interface_ethernet_statistics_instance = InterfaceEthernetStatistics.from_json(json)
# print the JSON string representation of the object
print InterfaceEthernetStatistics.to_json()

# convert the object into a dict
interface_ethernet_statistics_dict = interface_ethernet_statistics_instance.to_dict()
# create an instance of InterfaceEthernetStatistics from a dict
interface_ethernet_statistics_form_dict = interface_ethernet_statistics.from_dict(interface_ethernet_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


