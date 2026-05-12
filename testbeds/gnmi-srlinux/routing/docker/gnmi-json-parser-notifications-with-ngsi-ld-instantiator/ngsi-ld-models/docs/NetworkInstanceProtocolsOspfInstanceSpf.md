# NetworkInstanceProtocolsOspfInstanceSpf

SPF related information  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceSpf. | [default to 'NetworkInstanceProtocolsOspfInstanceSpf']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**full_spf_runs** | [**NetworkInstanceProtocolsOspfInstanceSpfFullSpfRuns**](NetworkInstanceProtocolsOspfInstanceSpfFullSpfRuns.md) |  | [optional] 
**ext_spf_runs** | [**ExtSpfRuns**](ExtSpfRuns.md) |  | [optional] 
**incremental_inter_spf_runs** | [**IncrementalInterSpfRuns**](IncrementalInterSpfRuns.md) |  | [optional] 
**incremental_ext_spf_runs** | [**IncrementalExtSpfRuns**](IncrementalExtSpfRuns.md) |  | [optional] 
**spf_attempts_failed** | [**SpfAttemptsFailed**](SpfAttemptsFailed.md) |  | [optional] 
**max_spf_run_interval** | [**MaxSpfRunInterval**](MaxSpfRunInterval.md) |  | [optional] 
**min_spf_run_interval** | [**MinSpfRunInterval**](MinSpfRunInterval.md) |  | [optional] 
**avg_spf_run_interval** | [**AvgSpfRunInterval**](AvgSpfRunInterval.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_spf import NetworkInstanceProtocolsOspfInstanceSpf

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceSpf from a JSON string
network_instance_protocols_ospf_instance_spf_instance = NetworkInstanceProtocolsOspfInstanceSpf.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceSpf.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_spf_dict = network_instance_protocols_ospf_instance_spf_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceSpf from a dict
network_instance_protocols_ospf_instance_spf_from_dict = NetworkInstanceProtocolsOspfInstanceSpf.from_dict(network_instance_protocols_ospf_instance_spf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


