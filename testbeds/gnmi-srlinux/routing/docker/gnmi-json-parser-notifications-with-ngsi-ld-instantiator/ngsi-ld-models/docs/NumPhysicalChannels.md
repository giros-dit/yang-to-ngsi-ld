# NumPhysicalChannels

Sets the number of lanes or physical channels assigned to this interface or to the set of interfaces within this breakout group  This leaf can be used to distinguish between transceivers that provide the same port-speed or breakout-configuration but using different PMAs. For example, if a port supports two transceivers providing 100G optical signal but one uses CAUI4 and the other uses 100GAUI-2, then this leaf can be set to 4 for the CAUI4 transceiver and 2 for the 100GAUI-2 transceiver. Similarly, a transceiver that provides a breakout of 4 ports of 100G using 4 x 100GAUI2 would set this leaf to 8 but a transceiver using 4 x 100GAUI-1 would have this leaf set to 4.  If not set, then the default shall be as follows:   1 is used for 10G, 25G   2 is used for 50G   4 is used for 40G, 100G, 2x50G, 1x100G, 4x10G, 4x25G   6 is used for 3x100G (digital coherent optics)   8 is used for 200G, 400G, 800G, 2x100G, 4x100G, 8x50G   YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **int** |  | 
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
from ngsi_ld_models.models.num_physical_channels import NumPhysicalChannels

# TODO update the JSON string below
json = "{}"
# create an instance of NumPhysicalChannels from a JSON string
num_physical_channels_instance = NumPhysicalChannels.from_json(json)
# print the JSON string representation of the object
print(NumPhysicalChannels.to_json())

# convert the object into a dict
num_physical_channels_dict = num_physical_channels_instance.to_dict()
# create an instance of NumPhysicalChannels from a dict
num_physical_channels_from_dict = NumPhysicalChannels.from_dict(num_physical_channels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


