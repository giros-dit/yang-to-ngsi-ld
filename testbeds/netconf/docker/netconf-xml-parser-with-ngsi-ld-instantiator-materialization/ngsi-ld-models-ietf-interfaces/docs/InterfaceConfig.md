# InterfaceConfig

The list of configured interfaces on the device.  The operational state of an interface is available in the /interfaces-state/interface list. If the configuration of a system-controlled interface cannot be used by the system (e.g., the interface hardware present does not match the interface type), then the configuration is not applied to the system-controlled interface shown in the /interfaces-state/interface list. If the configuration of a user-controlled interface cannot be used by the system, the configured interface is not instantiated in the /interfaces-state/interface list.  YANG module: ietf-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceConfig. | [default to 'InterfaceConfig']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**name** | [**InterfaceConfigName**](InterfaceConfigName.md) |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**interface_type** | [**InterfaceConfigType**](InterfaceConfigType.md) |  | 
**enabled** | [**InterfaceConfigEnabled**](InterfaceConfigEnabled.md) |  | [optional] 
**link_up_down_trap_enable** | [**LinkUpDownTrapEnable**](LinkUpDownTrapEnable.md) |  | [optional] 

## Example

```python
from ngsi_ld_models_ietf_interfaces.models.interface_config import InterfaceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceConfig from a JSON string
interface_config_instance = InterfaceConfig.from_json(json)
# print the JSON string representation of the object
print(InterfaceConfig.to_json())

# convert the object into a dict
interface_config_dict = interface_config_instance.to_dict()
# create an instance of InterfaceConfig from a dict
interface_config_from_dict = InterfaceConfig.from_dict(interface_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


