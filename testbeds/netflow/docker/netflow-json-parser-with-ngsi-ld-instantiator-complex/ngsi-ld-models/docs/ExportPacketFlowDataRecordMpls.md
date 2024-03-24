# ExportPacketFlowDataRecordMpls

This container collects all the metrics associated with MPLS (MultiProtocol Label Switching)  YANG module: netflow-v9.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be ExportPacketFlowDataRecordMpls. | [default to 'ExportPacketFlowDataRecordMpls']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**pal_rd** | [**PalRd**](PalRd.md) |  | [optional] 
**prefix_len** | [**PrefixLen**](PrefixLen.md) |  | [optional] 
**top_label_type** | [**TopLabelType**](TopLabelType.md) |  | [optional] 
**top_label_ip** | [**TopLabelIp**](TopLabelIp.md) |  | [optional] 
**label1** | [**Label1**](Label1.md) |  | [optional] 
**label2** | [**Label2**](Label2.md) |  | [optional] 
**label3** | [**Label3**](Label3.md) |  | [optional] 
**label4** | [**Label4**](Label4.md) |  | [optional] 
**label5** | [**Label5**](Label5.md) |  | [optional] 
**label6** | [**Label6**](Label6.md) |  | [optional] 
**label7** | [**Label7**](Label7.md) |  | [optional] 
**label8** | [**Label8**](Label8.md) |  | [optional] 
**label9** | [**Label9**](Label9.md) |  | [optional] 
**label10** | [**Label10**](Label10.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.export_packet_flow_data_record_mpls import ExportPacketFlowDataRecordMpls

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPacketFlowDataRecordMpls from a JSON string
export_packet_flow_data_record_mpls_instance = ExportPacketFlowDataRecordMpls.from_json(json)
# print the JSON string representation of the object
print ExportPacketFlowDataRecordMpls.to_json()

# convert the object into a dict
export_packet_flow_data_record_mpls_dict = export_packet_flow_data_record_mpls_instance.to_dict()
# create an instance of ExportPacketFlowDataRecordMpls from a dict
export_packet_flow_data_record_mpls_form_dict = export_packet_flow_data_record_mpls.from_dict(export_packet_flow_data_record_mpls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


