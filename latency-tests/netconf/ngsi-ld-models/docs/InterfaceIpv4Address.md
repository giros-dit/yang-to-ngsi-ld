# InterfaceIpv4Address

NGSI-LD Entity Type that represents the IPv4 address on interfaces of a YANG model-based network device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceIpv4Address. | [optional] [default to 'InterfaceIpv4Address']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**ip** | [**Ipv4Ip**](Ipv4Ip.md) |  | [optional] 
**prefix_length** | [**Ipv4PrefixLength**](Ipv4PrefixLength.md) |  | [optional] 
**netmask** | [**Ipv4Netmask**](Ipv4Netmask.md) |  | [optional] 
**origin** | [**IpOrigin**](IpOrigin.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ipv4_address import InterfaceIpv4Address

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceIpv4Address from a JSON string
interface_ipv4_address_instance = InterfaceIpv4Address.from_json(json)
# print the JSON string representation of the object
print InterfaceIpv4Address.to_json()

# convert the object into a dict
interface_ipv4_address_dict = interface_ipv4_address_instance.to_dict()
# create an instance of InterfaceIpv4Address from a dict
interface_ipv4_address_form_dict = interface_ipv4_address.from_dict(interface_ipv4_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


