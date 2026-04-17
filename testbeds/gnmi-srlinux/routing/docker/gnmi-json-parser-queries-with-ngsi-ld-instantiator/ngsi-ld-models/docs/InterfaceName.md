# InterfaceName

The name of the interface  Valid options are: irb<N>, N=0..255 lif-<lif_name> enp<bus>s<dev>f<fn>, bus=0..255, dev=0..31, fn=0..7 vhn-<vhn_name> lag<N>, N=1..1000 [note1] lo<N>, N=0..255 mgmt0 mgmt0-standby mgmtA mgmtB ethernet-<slot>/<port> ethernet-<slot>/<connector>/<port> ethernet-<slot>/m<mda>/<port> ethernet-<slot>/m<mda>/<connector>/<port> system0 sync0  <lif_name>=Linux interface name <vhn_name>=vhost interface name <slot>=slot number {1,2,3,..} <mda>=mda id {1,2,3,..} <connector>=connector id {1,2,3,..} <port>=port id {1,2,3,..}  [note1] The maximum number of LAGs per platform is as follows:  D1: 32 (N must be 1..32)  D2-D3: 128 (N must be 1..1000)  D4-D5: 64 (N must be 1..64)  H2-H3: 127 (N must be 1..127)  H4-32D: 127 (N must be 1..127)  H4: 255 (N must be 1..255)  H5-32D: 127 (N must be 1..127)  H5-64D: 127 (N must be 1..127)  H5-64O: 127 (N must be 1..127)  IXR: 512 (N must be 1..512)  SXR-1d-32D: 128 (N must be 1..128)  SXR-1x-44S: 128 (N must be 1..128)  vSRL: 8 (N must be 1..8)  A1: 10 (N must be 1..10)  IXR-X1b: 512 (N must be 1..512)  IXR-X3b: 512 (N must be 1..512)  SSE-T8164: 127 (N must be 1..127)  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.interface_name import InterfaceName

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceName from a JSON string
interface_name_instance = InterfaceName.from_json(json)
# print the JSON string representation of the object
print(InterfaceName.to_json())

# convert the object into a dict
interface_name_dict = interface_name_instance.to_dict()
# create an instance of InterfaceName from a dict
interface_name_from_dict = InterfaceName.from_dict(interface_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


