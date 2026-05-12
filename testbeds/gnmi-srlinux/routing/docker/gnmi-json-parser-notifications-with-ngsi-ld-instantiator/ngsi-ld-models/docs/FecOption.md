# FecOption

The forward error correction algorithm requested for the interface  The same FEC algorithm must be used at both ends of a link. This leaf should be only be configured for 25G and 100G interfaces; it can cause the port to remain operationally down for other interface speeds. 1G, 10G, and 40G interfaces do not use FEC 50G and interfaces with speeds higher than 100G have well defined FEC settings in IEEE 802.3 that must be used and so configuration is not needed.  For 100G interfaces, if the specific transceiver inserted uses PAM4 encoding, then the system shall always enable clause 91 RS(544,514) FEC and so this leaf should be left unconfigured. For 100G interfaces, if the specific transceiver inserted uses NRZ encoding, then it may require rs-528 to be enabled. This is dependent on the specific PMD and also whether the installed transceiver includes the FEC functionality inside the transceiver. Refer to Nokia support for the correct setting for the specific transceiver.  If this leaf is configured and the setting is incompatible with the installed transceiver, the interface shall be kept down with a reason of unsupported-fec.  25G interfaces support disabled, base-r, and rs-528. The FEC requirement for a 25G interface depends on the cable type. A CA-N DAC cable has a loss specification that requires no FEC. A CA-S DAC cable requires FEC, rs-528 recommended. A CA-L DAC cable requires the stronger rs-528 FEC.  YANG module: srl_nokia-interfaces.yang 

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
from ngsi_ld_models.models.fec_option import FecOption

# TODO update the JSON string below
json = "{}"
# create an instance of FecOption from a JSON string
fec_option_instance = FecOption.from_json(json)
# print the JSON string representation of the object
print(FecOption.to_json())

# convert the object into a dict
fec_option_dict = fec_option_instance.to_dict()
# create an instance of FecOption from a dict
fec_option_from_dict = FecOption.from_dict(fec_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


