# ExportPacketFlowDataRecordIpv4

This container collects all metrics related to IPv4  YANG module: netflow-v9.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be ExportPacketFlowDataRecordIpv4. | [default to 'ExportPacketFlowDataRecordIpv4']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**src_address** | [**ExportPacketFlowDataRecordIpv4SrcAddress**](ExportPacketFlowDataRecordIpv4SrcAddress.md) |  | [optional] 
**dst_address** | [**ExportPacketFlowDataRecordIpv4DstAddress**](ExportPacketFlowDataRecordIpv4DstAddress.md) |  | [optional] 
**src_mask** | [**ExportPacketFlowDataRecordIpv4SrcMask**](ExportPacketFlowDataRecordIpv4SrcMask.md) |  | [optional] 
**dst_mask** | [**ExportPacketFlowDataRecordIpv4DstMask**](ExportPacketFlowDataRecordIpv4DstMask.md) |  | [optional] 
**src_prefix** | [**SrcPrefix**](SrcPrefix.md) |  | [optional] 
**dst_prefix** | [**DstPrefix**](DstPrefix.md) |  | [optional] 
**next_hop** | [**ExportPacketFlowDataRecordIpv4NextHop**](ExportPacketFlowDataRecordIpv4NextHop.md) |  | [optional] 
**identification** | [**Identification**](Identification.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.export_packet_flow_data_record_ipv4 import ExportPacketFlowDataRecordIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPacketFlowDataRecordIpv4 from a JSON string
export_packet_flow_data_record_ipv4_instance = ExportPacketFlowDataRecordIpv4.from_json(json)
# print the JSON string representation of the object
print ExportPacketFlowDataRecordIpv4.to_json()

# convert the object into a dict
export_packet_flow_data_record_ipv4_dict = export_packet_flow_data_record_ipv4_instance.to_dict()
# create an instance of ExportPacketFlowDataRecordIpv4 from a dict
export_packet_flow_data_record_ipv4_form_dict = export_packet_flow_data_record_ipv4.from_dict(export_packet_flow_data_record_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


