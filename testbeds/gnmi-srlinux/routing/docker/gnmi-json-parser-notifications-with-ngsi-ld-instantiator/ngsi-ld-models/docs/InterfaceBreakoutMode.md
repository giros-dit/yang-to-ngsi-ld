# InterfaceBreakoutMode

Configuration of breakout options.  7220 D2L ports 49-55: 4x10G 7220 D3 ports 3-33: 4x10G and 4x25G 7220 D3L ports 1-31: 2x50G, 4x10G and 4x25G 7220 H3 ports 3-34: 4x10G, 2x100G/4x100G, and 2x200G 7220 H4 ports 1-64: 4x100G and 2x200G 7220 H4-32D ports 1-32: 2x100G/4x100G and 2x200G 7220 H5-32D Odd Ports 1-31: 2x100G/4x100G/8x100G and 2x400G 7220 H5-32D Even Ports 2-32: 2x100G, 2x400G 7220 H5-64D ports 1-32: 2x100G/4x100G/8x100G and 2x400G 7220 H5-64D ports 33-64: 2x100G and 2x400G 7220 H5-64O ports 1-32: 8x100G and 2x400G 7220 H5-64O ports 33-64: 2x400G 7220 D4 ports 29-32: 4x100G, 4x25G, and 4x10G 7220 D4 ports 9, 23-27: 4x25G and 4x10G 7220 D5 ports 1-32: 4x10G, 4x25G, 2x100G/4x100G, and 2x200G 7730 SXR-1d-32D QSFP28 ports 1-16, 21-32: 4x10G and 4x25G (Note 3) 7730 SXR-1d-32D QSFPDD ports 17-20: 4x100G, 3x100G (Note 1), 4x25G, and 4x10G 7730 SXR-1x-44S SFPDD ports 1-20, 23-42: No breakouts 7730 SXR-1x-44S QSFPDD ports 21,22,43,44: 4x100G, 3x100G (Note 1), 4x25G, and 4x10G 7250 IXR-6e/10e 60p QSFP28 IMM ports: 9,12,15,18,21,24,26,27,29,30,32,33,35,36,38,39,41,42,45,48: 4x25G and 4x10G (Note 2) 7250 IXR-6e/10e 36p QSFPDD IMM all ports: 4x100G, 2x100G, 4x25G, and 4x10G 7250 IXR-6e/10e/18e 36p QSFP112-DD IMM all ports: 2x400G, 8x100G, 4x100G, 3x100G (Note 1), 2x100G, 1x100G (Note 1), 4x25G 7250 IXR-6e/10e/18e 36p OSFP IMM all ports: 2x400G, 8x100G 7250 IXR-X1b QSFP28 ports 1-24: 4x25G, and 4x10G (Note 4) 7250 IXR-X1b QSFPDD ports 25-36: 4x100G, 3x100G (Note 1), 2x100G (Note 1), 1x100G (Note 1), 4x25G, and 4x10G 7250 IXR-X3b QSFPDD all ports: 4x100G, 3x100G (Note 1), 2x100G (Note 1), 1x100G (Note 1), 4x25G, and 4x10G SSE-T8164 Odd Ports 1-63: 2x400G, 4x200G, 8x100G SSE-T8164 Even Ports 2-64: 2x400G  Note 1: 3x100G, 2x100G, 1x100G is only supported for Digital Coherent Optic transceivers  Note 2: For the following port groupings only the higher numbered port supports breakout-mode.     If the higher numbered port is to be configured for breakout-mode, then the lower numbered port should not be configured.     If both ports are configured, then the lower numbered port takes precedence and the higher numbered port shall be operationally down with reason unsupported-breakout-port.     Groupings are (8,9), (11,12), (14,15), (17,18), (20,21), (23,24), (44, 45), (47,48).  Note 3: Breakout and 40G is only supported on odd numbered ports.     For the QSFP28 four port groupings [1-4], [5-8], [9-12], [13-16], [21-24], [25-28], and [29-32] if either of the odd numbered ports within a group is configured for 40G, 4x10G, or 4x25G,     then the other odd numbered port in the same group may only be configured if it is configured for one of 40G, 4x10G, or 4x25G (can differ between the odd ports) and neither of     the two even numbered ports within the same group can be configured.  Note 4: For the QSFP28 ports, the following port groups exist [n, n+1, n+2, n+3] for n = 1, 5, 9, 13, 17, 21. Breakout for 4x25G or 4x10G is only supported on ports n+1 and n+3.     When initially configuring a port with a breakout configuration or port speed that does not already exist on another configured port within the same group, then a link flap and traffic hit may occur on other ports within the same group.     When the breakout configuration or port speed is changed for a port in a group, then a link flap and traffic hit may occur on other ports within the same group.     If port n+1 within the group is configured for breakout, then port n cannot be configured.     In addition if port n+1 is configured for breakout and port n+3 is configured without breakout, then port n+2 may only be configured with the same speed as port n+3.     If port n+3 within the group is configured for breakout, then port n+2 cannot be configured.     In addition if port n+3 is configured for breakout and port n+1 is configured without breakout, then port n may only be configured with the same speed as port n+1.  Port Groups and auto-configuration of port speed:  Manually configured breakout-mode takes precedence over the auto-configured port-speed. This means that configuring a port within a port-group can have a side effect to take down an operational port that had its speed set based on the auto configuration feature. If there is risk of mixing transceiver types within a port group, then it is recommended to always manually configure the ports  YANG module: srl_nokia-interfaces.yang 

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
print(InterfaceBreakoutMode.to_json())

# convert the object into a dict
interface_breakout_mode_dict = interface_breakout_mode_instance.to_dict()
# create an instance of InterfaceBreakoutMode from a dict
interface_breakout_mode_from_dict = InterfaceBreakoutMode.from_dict(interface_breakout_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


