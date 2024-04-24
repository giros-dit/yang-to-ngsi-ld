# LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason

List of extraction reasons that are possible for the pipeline  YANG module: srl_nokia-platform-lc.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason. | [default to 'LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**reason** | [**Reason**](Reason.md) |  | [optional] 
**extracted_packets** | [**LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReasonExtractedPackets**](LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReasonExtractedPackets.md) |  | [optional] 
**extracted_octets** | [**LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReasonExtractedOctets**](LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReasonExtractedOctets.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason import LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason

# TODO update the JSON string below
json = "{}"
# create an instance of LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason from a JSON string
linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason_instance = LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason.from_json(json)
# print the JSON string representation of the object
print LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason.to_json()

# convert the object into a dict
linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason_dict = linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason_instance.to_dict()
# create an instance of LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractionReason from a dict
linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason_form_dict = linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason.from_dict(linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_extraction_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


