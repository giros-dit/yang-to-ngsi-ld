# NetworkInstanceTrafficEngineering

Container with traffic engineering options for the network-instance  YANG module: srl_nokia-traffic-engineering.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceTrafficEngineering. | [default to 'NetworkInstanceTrafficEngineering']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**autonomous_system** | [**AutonomousSystem**](AutonomousSystem.md) |  | [optional] 
**ipv4_te_router_id** | [**Ipv4TeRouterId**](Ipv4TeRouterId.md) |  | [optional] 
**ipv6_te_router_id** | [**Ipv6TeRouterId**](Ipv6TeRouterId.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_traffic_engineering import NetworkInstanceTrafficEngineering

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceTrafficEngineering from a JSON string
network_instance_traffic_engineering_instance = NetworkInstanceTrafficEngineering.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceTrafficEngineering.to_json())

# convert the object into a dict
network_instance_traffic_engineering_dict = network_instance_traffic_engineering_instance.to_dict()
# create an instance of NetworkInstanceTrafficEngineering from a dict
network_instance_traffic_engineering_from_dict = NetworkInstanceTrafficEngineering.from_dict(network_instance_traffic_engineering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


