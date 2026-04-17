# InterfaceAdapter

State for adapters  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceAdapter. | [default to 'InterfaceAdapter']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**model_number** | [**ModelNumber**](ModelNumber.md) |  | [optional] 
**adapter_type** | [**InterfaceAdapterType**](InterfaceAdapterType.md) |  | [optional] 
**vendor_manufacture_date** | [**VendorManufactureDate**](VendorManufactureDate.md) |  | [optional] 
**vendor_oui** | [**VendorOui**](VendorOui.md) |  | [optional] 
**vendor_part_number** | [**InterfaceAdapterVendorPartNumber**](InterfaceAdapterVendorPartNumber.md) |  | [optional] 
**vendor_serial_number** | [**VendorSerialNumber**](VendorSerialNumber.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_adapter import InterfaceAdapter

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceAdapter from a JSON string
interface_adapter_instance = InterfaceAdapter.from_json(json)
# print the JSON string representation of the object
print InterfaceAdapter.to_json()

# convert the object into a dict
interface_adapter_dict = interface_adapter_instance.to_dict()
# create an instance of InterfaceAdapter from a dict
interface_adapter_form_dict = interface_adapter.from_dict(interface_adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


