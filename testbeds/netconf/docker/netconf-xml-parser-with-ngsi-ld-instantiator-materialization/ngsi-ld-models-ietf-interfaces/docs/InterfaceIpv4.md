# InterfaceIpv4

Interface-specific parameters for the IPv4 address family.  YANG module: ietf-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceIpv4. | [default to 'InterfaceIpv4']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**forwarding** | [**InterfaceIpv4Forwarding**](InterfaceIpv4Forwarding.md) |  | [optional] 
**mtu** | [**InterfaceIpv4Mtu**](InterfaceIpv4Mtu.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_ipv4 import InterfaceIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceIpv4 from a JSON string
interface_ipv4_instance = InterfaceIpv4.from_json(json)
# print the JSON string representation of the object
print(InterfaceIpv4.to_json())

# convert the object into a dict
interface_ipv4_dict = interface_ipv4_instance.to_dict()
# create an instance of InterfaceIpv4 from a dict
interface_ipv4_from_dict = InterfaceIpv4.from_dict(interface_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


