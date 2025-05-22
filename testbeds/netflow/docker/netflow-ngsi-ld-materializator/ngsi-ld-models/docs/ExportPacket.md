# ExportPacket

This container collects all fields that appear in the NetFlow Export Packet header and possible fields of each Flow Data Record that is transmitted in this packet The names and semantics of the fields used follow the Cisco white paper (mentioned in the references section)  YANG module: netflow-v9.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be ExportPacket. | [default to 'ExportPacket']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**sequence_number** | [**SequenceNumber**](SequenceNumber.md) |  | 
**count** | [**Count**](Count.md) |  | [optional] 
**system_uptime** | [**SystemUptime**](SystemUptime.md) |  | [optional] 
**unix_seconds** | [**UnixSeconds**](UnixSeconds.md) |  | [optional] 
**source_id** | [**SourceId**](SourceId.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.export_packet import ExportPacket

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPacket from a JSON string
export_packet_instance = ExportPacket.from_json(json)
# print the JSON string representation of the object
print ExportPacket.to_json()

# convert the object into a dict
export_packet_dict = export_packet_instance.to_dict()
# create an instance of ExportPacket from a dict
export_packet_form_dict = export_packet.from_dict(export_packet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


