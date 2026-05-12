# InterfaceEthernetForwardErrorCorrection

 YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceEthernetForwardErrorCorrection. | [default to 'InterfaceEthernetForwardErrorCorrection']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**fec_option** | [**FecOption**](FecOption.md) |  | [optional] 
**operational_host_if_fec** | [**OperationalHostIfFec**](OperationalHostIfFec.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_ethernet_forward_error_correction import InterfaceEthernetForwardErrorCorrection

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceEthernetForwardErrorCorrection from a JSON string
interface_ethernet_forward_error_correction_instance = InterfaceEthernetForwardErrorCorrection.from_json(json)
# print the JSON string representation of the object
print(InterfaceEthernetForwardErrorCorrection.to_json())

# convert the object into a dict
interface_ethernet_forward_error_correction_dict = interface_ethernet_forward_error_correction_instance.to_dict()
# create an instance of InterfaceEthernetForwardErrorCorrection from a dict
interface_ethernet_forward_error_correction_from_dict = InterfaceEthernetForwardErrorCorrection.from_dict(interface_ethernet_forward_error_correction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


