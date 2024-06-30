# InterfaceState

Operational state data at the global interface level  YANG module: openconfig-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceState. | [default to 'InterfaceState']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**InterfaceStateName**](InterfaceStateName.md) |  | [optional] 
**state_type** | [**InterfaceStateType**](InterfaceStateType.md) |  | 
**mtu** | [**InterfaceStateMtu**](InterfaceStateMtu.md) |  | [optional] 
**loopback_mode** | [**InterfaceStateLoopbackMode**](InterfaceStateLoopbackMode.md) |  | [optional] 
**description** | [**InterfaceStateDescription**](InterfaceStateDescription.md) |  | [optional] 
**enabled** | [**InterfaceStateEnabled**](InterfaceStateEnabled.md) |  | [optional] 
**ifindex** | [**InterfaceStateIfindex**](InterfaceStateIfindex.md) |  | [optional] 
**admin_status** | [**InterfaceStateAdminStatus**](InterfaceStateAdminStatus.md) |  | 
**oper_status** | [**InterfaceStateOperStatus**](InterfaceStateOperStatus.md) |  | 
**last_change** | [**InterfaceStateLastChange**](InterfaceStateLastChange.md) |  | [optional] 
**tpid** | [**InterfaceStateTpid**](InterfaceStateTpid.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_state import InterfaceState

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceState from a JSON string
interface_state_instance = InterfaceState.from_json(json)
# print the JSON string representation of the object
print InterfaceState.to_json()

# convert the object into a dict
interface_state_dict = interface_state_instance.to_dict()
# create an instance of InterfaceState from a dict
interface_state_form_dict = interface_state.from_dict(interface_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


