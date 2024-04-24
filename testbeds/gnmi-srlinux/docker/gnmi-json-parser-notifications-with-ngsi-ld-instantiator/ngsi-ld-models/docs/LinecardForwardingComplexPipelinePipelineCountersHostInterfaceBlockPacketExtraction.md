# LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction

Packet extraction from the NPU towards the CPU  YANG module: srl_nokia-platform-lc.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction. | [default to 'LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**extracted_packets** | [**LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractedPackets**](LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractedPackets.md) |  | [optional] 
**extracted_octets** | [**LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractedOctets**](LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtractionExtractedOctets.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction import LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction

# TODO update the JSON string below
json = "{}"
# create an instance of LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction from a JSON string
linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_instance = LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction.from_json(json)
# print the JSON string representation of the object
print LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction.to_json()

# convert the object into a dict
linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_dict = linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_instance.to_dict()
# create an instance of LinecardForwardingComplexPipelinePipelineCountersHostInterfaceBlockPacketExtraction from a dict
linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_form_dict = linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction.from_dict(linecard_forwarding_complex_pipeline_pipeline_counters_host_interface_block_packet_extraction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


