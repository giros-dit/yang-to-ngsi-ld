# ExportPacketFlowDataRecordApplication

This container collects all application-related metrics  YANG module: netflow-v9.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be ExportPacketFlowDataRecordApplication. | [default to 'ExportPacketFlowDataRecordApplication']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**desc** | [**Desc**](Desc.md) |  | [optional] 
**tag** | [**Tag**](Tag.md) |  | [optional] 
**name** | [**Name**](Name.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.export_packet_flow_data_record_application import ExportPacketFlowDataRecordApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPacketFlowDataRecordApplication from a JSON string
export_packet_flow_data_record_application_instance = ExportPacketFlowDataRecordApplication.from_json(json)
# print the JSON string representation of the object
print ExportPacketFlowDataRecordApplication.to_json()

# convert the object into a dict
export_packet_flow_data_record_application_dict = export_packet_flow_data_record_application_instance.to_dict()
# create an instance of ExportPacketFlowDataRecordApplication from a dict
export_packet_flow_data_record_application_form_dict = export_packet_flow_data_record_application.from_dict(export_packet_flow_data_record_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


