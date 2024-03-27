# ExportPacketFlowDataRecord

This list contains all possible fields of a Flow Data Record sent in a Export Packet  YANG module: netflow-v9.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be ExportPacketFlowDataRecord. | [default to 'ExportPacketFlowDataRecord']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**flow_id** | [**FlowId**](FlowId.md) |  | [optional] 
**bytes_in** | [**ExportPacketFlowDataRecordBytesIn**](ExportPacketFlowDataRecordBytesIn.md) |  | 
**bytes_out** | [**BytesOut**](BytesOut.md) |  | [optional] 
**pkts_in** | [**ExportPacketFlowDataRecordPktsIn**](ExportPacketFlowDataRecordPktsIn.md) |  | 
**pkts_out** | [**PktsOut**](PktsOut.md) |  | [optional] 
**flows** | [**Flows**](Flows.md) |  | [optional] 
**protocol** | [**Protocol**](Protocol.md) |  | 
**src_tos** | [**SrcTos**](SrcTos.md) |  | [optional] 
**dst_tos** | [**DstTos**](DstTos.md) |  | [optional] 
**tcp_flags** | [**TcpFlags**](TcpFlags.md) |  | [optional] 
**src_port** | [**SrcPort**](SrcPort.md) |  | 
**dst_port** | [**DstPort**](DstPort.md) |  | 
**snmp_in** | [**SnmpIn**](SnmpIn.md) |  | [optional] 
**snmp_out** | [**SnmpOut**](SnmpOut.md) |  | [optional] 
**bytes_out_mul** | [**BytesOutMul**](BytesOutMul.md) |  | [optional] 
**pkts_out_mul** | [**PktsOutMul**](PktsOutMul.md) |  | [optional] 
**first_switched** | [**FirstSwitched**](FirstSwitched.md) |  | 
**last_switched** | [**LastSwitched**](LastSwitched.md) |  | 
**min_pkt_len** | [**MinPktLen**](MinPktLen.md) |  | [optional] 
**max_pkt_len** | [**MaxPktLen**](MaxPktLen.md) |  | [optional] 
**icmp_type** | [**IcmpType**](IcmpType.md) |  | [optional] 
**igmp_type** | [**IgmpType**](IgmpType.md) |  | [optional] 
**sampler_name** | [**SamplerName**](SamplerName.md) |  | [optional] 
**sampling_interval** | [**SamplingInterval**](SamplingInterval.md) |  | [optional] 
**sampling_algorithm** | [**SamplingAlgorithm**](SamplingAlgorithm.md) |  | [optional] 
**flow_active_tout** | [**FlowActiveTout**](FlowActiveTout.md) |  | [optional] 
**flow_inactive_tout** | [**FlowInactiveTout**](FlowInactiveTout.md) |  | [optional] 
**engine_type** | [**EngineType**](EngineType.md) |  | [optional] 
**engine_id** | [**EngineId**](EngineId.md) |  | [optional] 
**tot_bytes_exp** | [**TotBytesExp**](TotBytesExp.md) |  | [optional] 
**tot_pkts_exp** | [**TotPktsExp**](TotPktsExp.md) |  | [optional] 
**tot_flows_exp** | [**TotFlowsExp**](TotFlowsExp.md) |  | [optional] 
**flow_sampler_id** | [**FlowSamplerId**](FlowSamplerId.md) |  | [optional] 
**flow_sampler_mode** | [**FlowSamplerMode**](FlowSamplerMode.md) |  | [optional] 
**flow_sampler_random** | [**FlowSamplerRandom**](FlowSamplerRandom.md) |  | [optional] 
**min_ttl** | [**MinTtl**](MinTtl.md) |  | [optional] 
**max_ttl** | [**MaxTtl**](MaxTtl.md) |  | [optional] 
**src_mac_in** | [**SrcMacIn**](SrcMacIn.md) |  | 
**dst_mac_in** | [**DstMacIn**](DstMacIn.md) |  | 
**src_mac_out** | [**SrcMacOut**](SrcMacOut.md) |  | [optional] 
**dst_mac_out** | [**DstMacOut**](DstMacOut.md) |  | [optional] 
**ip_version** | [**IpVersion**](IpVersion.md) |  | 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**if_name** | [**IfName**](IfName.md) |  | [optional] 
**if_desc** | [**IfDesc**](IfDesc.md) |  | [optional] 
**frag_offset** | [**FragOffset**](FragOffset.md) |  | [optional] 
**forwarding_status** | [**ForwardingStatus**](ForwardingStatus.md) |  | [optional] 
**postip_dscp** | [**PostipDscp**](PostipDscp.md) |  | [optional] 
**repl_factor_mul** | [**ReplFactorMul**](ReplFactorMul.md) |  | [optional] 
**flow_duration** | [**FlowDuration**](FlowDuration.md) |  | [optional] 
**bytes_in_per_second** | [**BytesInPerSecond**](BytesInPerSecond.md) |  | [optional] 
**bytes_out_per_second** | [**BytesOutPerSecond**](BytesOutPerSecond.md) |  | [optional] 
**pkts_in_per_second** | [**PktsInPerSecond**](PktsInPerSecond.md) |  | [optional] 
**pkts_out_per_second** | [**PktsOutPerSecond**](PktsOutPerSecond.md) |  | [optional] 
**bytes_in_per_packet** | [**BytesInPerPacket**](BytesInPerPacket.md) |  | [optional] 
**bytes_out_per_packet** | [**BytesOutPerPacket**](BytesOutPerPacket.md) |  | [optional] 
**ratio_bytes_in_per_out** | [**RatioBytesInPerOut**](RatioBytesInPerOut.md) |  | [optional] 
**ratio_pkts_in_per_out** | [**RatioPktsInPerOut**](RatioPktsInPerOut.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.export_packet_flow_data_record import ExportPacketFlowDataRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPacketFlowDataRecord from a JSON string
export_packet_flow_data_record_instance = ExportPacketFlowDataRecord.from_json(json)
# print the JSON string representation of the object
print ExportPacketFlowDataRecord.to_json()

# convert the object into a dict
export_packet_flow_data_record_dict = export_packet_flow_data_record_instance.to_dict()
# create an instance of ExportPacketFlowDataRecord from a dict
export_packet_flow_data_record_form_dict = export_packet_flow_data_record.from_dict(export_packet_flow_data_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


