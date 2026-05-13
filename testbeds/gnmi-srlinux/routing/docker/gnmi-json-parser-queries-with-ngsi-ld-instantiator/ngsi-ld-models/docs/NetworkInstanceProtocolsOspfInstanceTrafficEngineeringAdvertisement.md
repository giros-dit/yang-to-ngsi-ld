# NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement

A setting of false means that no TE-related TLVs and subTLVs should be added to LSAs or LSPs originated by this IGP instance. A setting of true means that TE-related TLVs and subTLVs should be added to LSAs or LSPs originated by this IGP instance.  YANG module: srl_nokia-ospf.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **bool** |  | [default to False]
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
from ngsi_ld_models.models.network_instance_protocols_ospf_instance_traffic_engineering_advertisement import NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement from a JSON string
network_instance_protocols_ospf_instance_traffic_engineering_advertisement_instance = NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement.to_json())

# convert the object into a dict
network_instance_protocols_ospf_instance_traffic_engineering_advertisement_dict = network_instance_protocols_ospf_instance_traffic_engineering_advertisement_instance.to_dict()
# create an instance of NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement from a dict
network_instance_protocols_ospf_instance_traffic_engineering_advertisement_from_dict = NetworkInstanceProtocolsOspfInstanceTrafficEngineeringAdvertisement.from_dict(network_instance_protocols_ospf_instance_traffic_engineering_advertisement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


