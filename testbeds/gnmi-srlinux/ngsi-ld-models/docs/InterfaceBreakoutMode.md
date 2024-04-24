# InterfaceBreakoutMode

Configuration of breakout options.  The 7220 D3 supports 4x10G and 4x25G breakout on ports 3-33. The 7220 D3L supports 4x10G and 4x25G breakout on ports 1-31. The 7220 H3 supports 4x10G, 2x100G/4x100G, and 2x200G breakout on ports 3-34. The 7220 H4 supports 4x100G breakout on ports 1-64. The 7220 D4 supports 4x100G breakout on ports 29-32. The 7220 D4 supports 4x25G breakout on ports 9, 23-27, 29-32. The 7220 D4 supports 4x10G breakout on ports 9, 23-27, 29-32. The 7220 D5 supports 4x10G, 4x25G, and 2x100G/4x100G breakout on ports 1-32. 7250 IXR-6e/10e 36p QSFPDD IMM all port: 4x100G, 2x100G, 4x25G, and 4x10G  YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceBreakoutMode. | [default to 'InterfaceBreakoutMode']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**num_breakout_ports** | [**NumBreakoutPorts**](NumBreakoutPorts.md) |  | 
**breakout_port_speed** | [**BreakoutPortSpeed**](BreakoutPortSpeed.md) |  | 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_breakout_mode import InterfaceBreakoutMode

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceBreakoutMode from a JSON string
interface_breakout_mode_instance = InterfaceBreakoutMode.from_json(json)
# print the JSON string representation of the object
print InterfaceBreakoutMode.to_json()

# convert the object into a dict
interface_breakout_mode_dict = interface_breakout_mode_instance.to_dict()
# create an instance of InterfaceBreakoutMode from a dict
interface_breakout_mode_form_dict = interface_breakout_mode.from_dict(interface_breakout_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


