# Ipv4

NGSI-LD Entity Type that represents the IPv4 parameters on interfaces of a YANG model-based network device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be Ipv4. | [optional] [default to 'Ipv4']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**enabled** | [**IpEnabled**](IpEnabled.md) |  | [optional] 
**forwarding** | [**Forwarding**](Forwarding.md) |  | [optional] 
**mtu** | [**Ipv4Mtu**](Ipv4Mtu.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.ipv4 import Ipv4

# TODO update the JSON string below
json = "{}"
# create an instance of Ipv4 from a JSON string
ipv4_instance = Ipv4.from_json(json)
# print the JSON string representation of the object
print Ipv4.to_json()

# convert the object into a dict
ipv4_dict = ipv4_instance.to_dict()
# create an instance of Ipv4 from a dict
ipv4_form_dict = ipv4.from_dict(ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


