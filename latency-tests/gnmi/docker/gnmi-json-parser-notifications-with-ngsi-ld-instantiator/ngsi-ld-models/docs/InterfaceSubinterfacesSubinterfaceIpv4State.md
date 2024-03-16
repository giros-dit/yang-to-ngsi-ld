# InterfaceSubinterfacesSubinterfaceIpv4State

Top level IPv4 operational state data  YANG module: openconfig-if-ip.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceSubinterfacesSubinterfaceIpv4State. | [default to 'InterfaceSubinterfacesSubinterfaceIpv4State']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**enabled** | [**InterfaceSubinterfacesSubinterfaceIpv4StateEnabled**](InterfaceSubinterfacesSubinterfaceIpv4StateEnabled.md) |  | [optional] 
**mtu** | [**InterfaceSubinterfacesSubinterfaceIpv4StateMtu**](InterfaceSubinterfacesSubinterfaceIpv4StateMtu.md) |  | [optional] 
**dhcp_client** | [**InterfaceSubinterfacesSubinterfaceIpv4StateDhcpClient**](InterfaceSubinterfacesSubinterfaceIpv4StateDhcpClient.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_subinterfaces_subinterface_ipv4_state import InterfaceSubinterfacesSubinterfaceIpv4State

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4State from a JSON string
interface_subinterfaces_subinterface_ipv4_state_instance = InterfaceSubinterfacesSubinterfaceIpv4State.from_json(json)
# print the JSON string representation of the object
print InterfaceSubinterfacesSubinterfaceIpv4State.to_json()

# convert the object into a dict
interface_subinterfaces_subinterface_ipv4_state_dict = interface_subinterfaces_subinterface_ipv4_state_instance.to_dict()
# create an instance of InterfaceSubinterfacesSubinterfaceIpv4State from a dict
interface_subinterfaces_subinterface_ipv4_state_form_dict = interface_subinterfaces_subinterface_ipv4_state.from_dict(interface_subinterfaces_subinterface_ipv4_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


