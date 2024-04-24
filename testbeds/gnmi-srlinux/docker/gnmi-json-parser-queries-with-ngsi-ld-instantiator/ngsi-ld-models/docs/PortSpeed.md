# PortSpeed

The speed of the port or channel  The default speed of a port (when there is no configured value and auto-negotiation is disabled or unsupported) depends on the platform and port/connector number as follows:  mgmt0 and mgmt0-standby ports: 1G J2 IMM ports 1-32: 100G J2 IMM ports 33-36: 100G 7220-D1 ports 1-48: 1G 7220-D1 ports 49-52: 10G 7220-D2/D2L ports 1-48: 25G 7220-D2/D2L ports 49-56: 100G 7220-D2L ports 57-58: 10G 7220-D3 ports 1-2: 10G 7220-D3 ethernet-1/[3-34]: 100G 7220-D3 ethernet-1/[3-33]/n: 25G 7220-D3L ethernet-1/[1-32]: 100G 7220-D3L ethernet-1/[1-31]/n: 25G 7220-D3L ports 33-34: 10G 7220-D4 ports 1-28: 100G 7220-D4 ports 29-36: 400G 7220-D5 ports 1-32: 400G 7220-D5 ports 33-38: 10G 7220-H2 ports 1-128: 100G 7220-H3 ports 1-2: 10G 7220-H3 ports 3-34: 400G 7220-H4 ports 1-64: 400G 7220-H4 ports 65-66: 10G 7250 IXR-6e/10e 60p QSFP28 IMM all port: 100G 7250 IXR-6e/10e 36p QSFPDD-400 IMM all port: 400G  Supported speeds: mgmt0 and mgmt0-standby ports: 1G J2 IMM ports 1-32: 40G, 100G [note1] J2 IMM ports 33-36: 40G, 100G, 400G 7220-D1 ports 1-48: 10M, 100M, 1G 7220-D1 ports 49-52: 10G 7220-D2/D2L ports 1-48: 1G, 10G, 25G [note2] 7220-D2 ports 49-56: 10G, 25G, 40G, 100G 7220-D2L ports 49-56: 10G, 25G, 40G, 100G 7220-D2L ports 57-58: 10G 7220-D3 ports 1-2: 10G 7220-D3 ethernet-1/[3-34]: 10G, 25G, 40G, 50G, 100G 7220-D3 ethernet-1/[3-33]/n: 10G, 25G 7220-D3L ethernet-1/[1-32]: 10G, 25G, 40G, 50G, 100G 7220-D3L ethernet-1/[1-31]/n: 10G, 25G 7220-D3L ports 33-34: 10G 7220-D4 ports 1-8: 40G, 100G 7220-D4 ports 9-28: 10G, 25G, 40G, 100G 7220-D4 ports 29-36: 10G, 25G, 40G, 100G, 400G 7220-D5 ports 1-32: 40G, 100G, 400G 7220-D5 ports 33-38: 10G 7220-H2 ports 1-128: 100G 7220-H3 ports 1-2: 10G 7220-H3 ports 3-34: 40G, 100G, 200G, 400G 7220-H4 ports 1-64: 40G, 100G, 400G 7220-H4 ports 65-66: 10G 7250 IXR-6e/10e 60p QSFP28 IMM all port: 100G 7250 IXR-6e/10e 36p QSFPDD-400 IMM all port: 40G, 100G, 400G  [note1] Ports 9-12 cannot operate at different port speeds (some at 40G and others at 100G). The required speed of ports 9-12 is based on the port-speed of the lowest-numbered configured port in this block; if any higher-numbered port in the block is configured with a different port speed that port will not come up.  [note2]  On 7220-D2: if one port in each consecutive group of 4 ports (1-4, 5-8, .. , 45-48) is configured and has a speed of 25G then the other 3 ports may only be configured if they also have a speed of 25G; if one port in each consecutive group of 4 ports (1-4, 5-8, .. , 45-48) is configured and has a speed of 1G or 10G the other 3 ports may only be configured if they also have a speed of 1G or 10G.  On 7220-D2L: if one port in each port group of 4 ports ({1, 2, 3, 6}, {4, 5, 7, 9}, {8, 10, 11, 12}, {13, 14, 15, 18}, {16, 17, 19, 21}, {20, 22, 23, 24}, {25, 26, 27, 30}, {28, 29, 31, 33}, {32, 34, 35, 36}, {37, 38, 39, 42}, {40, 41, 43, 45}, {44, 46, 47, 48}) is configured and has a speed of 25G the other 3 ports may only be configured if they also have a speed of 25G; if one port in each port group of 4 ports is configured and has a speed of 1G or 10G the other 3 ports may only be configured if they also have a speed of 1G or 10G.  7250 IXR details: If the interface corresponds to a connector that has no installed transceiver then the value is accepted without any checking or restriction, and info from state will display the configured value. Otherwise if the configured port-speed is NOT supported by the installed transceiver the port is forced operationally down.  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.port_speed import PortSpeed

# TODO update the JSON string below
json = "{}"
# create an instance of PortSpeed from a JSON string
port_speed_instance = PortSpeed.from_json(json)
# print the JSON string representation of the object
print PortSpeed.to_json()

# convert the object into a dict
port_speed_dict = port_speed_instance.to_dict()
# create an instance of PortSpeed from a dict
port_speed_form_dict = port_speed.from_dict(port_speed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


