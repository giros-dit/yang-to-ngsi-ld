# NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf

Information about the last full SPF run  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf. | [default to 'NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**run_time** | [**NetworkInstanceProtocolsOspfInstanceSpfLastFullSpfRunTime**](NetworkInstanceProtocolsOspfInstanceSpfLastFullSpfRunTime.md) |  | [optional] 
**total_time** | [**TotalTime**](TotalTime.md) |  | [optional] 
**intra_spf_time** | [**IntraSpfTime**](IntraSpfTime.md) |  | [optional] 
**inter_spf_time** | [**InterSpfTime**](InterSpfTime.md) |  | [optional] 
**extern_spf_time** | [**ExternSpfTime**](ExternSpfTime.md) |  | [optional] 
**rtm_update_time** | [**RtmUpdateTime**](RtmUpdateTime.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_spf_last_full_spf import NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf from a JSON string
network_instance_protocols_ospf_instance_spf_last_full_spf_instance = NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_spf_last_full_spf_dict = network_instance_protocols_ospf_instance_spf_last_full_spf_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf from a dict
network_instance_protocols_ospf_instance_spf_last_full_spf_from_dict = NetworkInstanceProtocolsOspfInstanceSpfLastFullSpf.from_dict(network_instance_protocols_ospf_instance_spf_last_full_spf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


