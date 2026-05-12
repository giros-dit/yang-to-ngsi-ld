# PeeringAddress

List of IP addresses to be sent for BGP auto discovery  Default values for this sub-TLV is to populate the addresses of the first subinterface of the interface the LLDPDU is being generated from, along with a unicast AFI/SAFI for IPv4 if an IPv4 address exists, and/or IPv6 if an IPv6 address exists.  If neither of these exist in the system, LLDP will not add the TLV to outgoing LLDPDUs, unless the peering-address is manually configured on a per-LLDP-port basis.  YANG module: srl_nokia-lldp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
**observed_at** | **datetime** | Is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instance_id** | **str** | A URI uniquely identifying a Property instance, as mandated by (see clause 4.5.7). System generated.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.peering_address import PeeringAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringAddress from a JSON string
peering_address_instance = PeeringAddress.from_json(json)
# print the JSON string representation of the object
print(PeeringAddress.to_json())

# convert the object into a dict
peering_address_dict = peering_address_instance.to_dict()
# create an instance of PeeringAddress from a dict
peering_address_from_dict = PeeringAddress.from_dict(peering_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


