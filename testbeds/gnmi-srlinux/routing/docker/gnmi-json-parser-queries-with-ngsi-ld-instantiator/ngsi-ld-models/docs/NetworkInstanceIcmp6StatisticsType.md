# NetworkInstanceIcmp6StatisticsType

 YANG module: srl_nokia-network-instance.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceIcmp6StatisticsType. | [default to 'NetworkInstanceIcmp6StatisticsType']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**NetworkInstanceIcmp6StatisticsTypeName**](NetworkInstanceIcmp6StatisticsTypeName.md) |  | [optional] 
**in_packets** | [**NetworkInstanceIcmp6StatisticsTypeInPackets**](NetworkInstanceIcmp6StatisticsTypeInPackets.md) |  | [optional] 
**out_packets** | [**NetworkInstanceIcmp6StatisticsTypeOutPackets**](NetworkInstanceIcmp6StatisticsTypeOutPackets.md) |  | [optional] 
**out_error_packets** | [**NetworkInstanceIcmp6StatisticsTypeOutErrorPackets**](NetworkInstanceIcmp6StatisticsTypeOutErrorPackets.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_icmp6_statistics_type import NetworkInstanceIcmp6StatisticsType

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceIcmp6StatisticsType from a JSON string
network_instance_icmp6_statistics_type_instance = NetworkInstanceIcmp6StatisticsType.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceIcmp6StatisticsType.to_json())

# convert the object into a dict
network_instance_icmp6_statistics_type_dict = network_instance_icmp6_statistics_type_instance.to_dict()
# create an instance of NetworkInstanceIcmp6StatisticsType from a dict
network_instance_icmp6_statistics_type_from_dict = NetworkInstanceIcmp6StatisticsType.from_dict(network_instance_icmp6_statistics_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


