# InterfaceAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | NGSI-LD Entity identifier. It has to be Interface. | [optional] [default to 'Interface']
**name** | [**Name**](Name.md) |  | [optional] 
**description** | [**Description**](Description.md) |  | [optional] 
**enabled** | [**Enabled**](Enabled.md) |  | [optional] 
**link_up_down_trap_enable** | [**LinkUpDownTrapEnable**](LinkUpDownTrapEnable.md) |  | [optional] 
**admin_status** | [**AdminStatus**](AdminStatus.md) |  | [optional] 
**oper_status** | [**OperStatus**](OperStatus.md) |  | [optional] 
**last_change** | [**LastChange**](LastChange.md) |  | [optional] 
**if_index** | [**IfIndex**](IfIndex.md) |  | [optional] 
**phys_address** | [**PhysAddress**](PhysAddress.md) |  | [optional] 
**speed** | [**Speed**](Speed.md) |  | [optional] 
**higher_layer_if** | [**HigherLayerIf**](HigherLayerIf.md) |  | [optional] 
**lower_layer_if** | [**LowerLayerIf**](LowerLayerIf.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.interface_all_of import InterfaceAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceAllOf from a JSON string
interface_all_of_instance = InterfaceAllOf.from_json(json)
# print the JSON string representation of the object
print InterfaceAllOf.to_json()

# convert the object into a dict
interface_all_of_dict = interface_all_of_instance.to_dict()
# create an instance of InterfaceAllOf from a dict
interface_all_of_form_dict = interface_all_of.from_dict(interface_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


