# Interface

NGSI-LD Entity Type that represents an interface of a YANG model-based network device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be Interface. | [default to 'Interface']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**Name**](Name.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**enabled** | [**InterfaceEnabled**](InterfaceEnabled.md) |  | [optional] 
**link_up_down_trap_enable** | [**LinkUpDownTrapEnable**](LinkUpDownTrapEnable.md) |  | [optional] 
**admin_status** | [**AdminStatus**](AdminStatus.md) |  | 
**oper_status** | [**OperStatus**](OperStatus.md) |  | 
**last_change** | [**LastChange**](LastChange.md) |  | [optional] 
**if_index** | [**IfIndex**](IfIndex.md) |  | 
**phys_address** | [**PhysAddress**](PhysAddress.md) |  | [optional] 
**speed** | [**Speed**](Speed.md) |  | [optional] 
**higher_layer_if** | [**HigherLayerIf**](HigherLayerIf.md) |  | [optional] 
**lower_layer_if** | [**LowerLayerIf**](LowerLayerIf.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print Interface.to_json()

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_form_dict = interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


