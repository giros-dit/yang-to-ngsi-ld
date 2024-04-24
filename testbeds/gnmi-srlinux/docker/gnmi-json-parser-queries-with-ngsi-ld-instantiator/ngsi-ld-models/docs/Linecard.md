# Linecard

Top-level container for linecard configuration and state  YANG module: srl_nokia-platform-lc.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be Linecard. | [default to 'Linecard']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**slot** | [**Slot**](Slot.md) |  | [optional] 
**admin_state** | [**LinecardAdminState**](LinecardAdminState.md) |  | [optional] 
**oper_state** | [**LinecardOperState**](LinecardOperState.md) |  | [optional] 
**last_booted** | [**LinecardLastBooted**](LinecardLastBooted.md) |  | [optional] 
**last_booted_reason** | [**LinecardLastBootedReason**](LinecardLastBootedReason.md) |  | [optional] 
**last_change** | [**LinecardLastChange**](LinecardLastChange.md) |  | [optional] 
**part_number** | [**LinecardPartNumber**](LinecardPartNumber.md) |  | [optional] 
**removable** | [**LinecardRemovable**](LinecardRemovable.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 
**clei_code** | [**CleiCode**](CleiCode.md) |  | [optional] 
**serial_number** | [**LinecardSerialNumber**](LinecardSerialNumber.md) |  | [optional] 
**manufactured_date** | [**ManufacturedDate**](ManufacturedDate.md) |  | [optional] 
**rebooting_at** | [**RebootingAt**](RebootingAt.md) |  | [optional] 
**linecard_type** | [**LinecardType**](LinecardType.md) |  | [optional] 
**software_version** | [**LinecardSoftwareVersion**](LinecardSoftwareVersion.md) |  | [optional] 
**locator_state** | [**LocatorState**](LocatorState.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.linecard import Linecard

# TODO update the JSON string below
json = "{}"
# create an instance of Linecard from a JSON string
linecard_instance = Linecard.from_json(json)
# print the JSON string representation of the object
print Linecard.to_json()

# convert the object into a dict
linecard_dict = linecard_instance.to_dict()
# create an instance of Linecard from a dict
linecard_form_dict = linecard.from_dict(linecard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


