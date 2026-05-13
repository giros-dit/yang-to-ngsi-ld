# Control

Top-level container for control module configuration and state  YANG module: srl_nokia-platform-control.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be Control. | [default to 'Control']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**slot** | [**ControlSlot**](ControlSlot.md) |  | [optional] 
**control_type** | [**ControlType**](ControlType.md) |  | [optional] 
**role** | [**Role**](Role.md) |  | [optional] 
**disk_encrypted** | [**DiskEncrypted**](DiskEncrypted.md) |  | [optional] 
**oper_state** | [**ControlOperState**](ControlOperState.md) |  | [optional] 
**last_booted** | [**ControlLastBooted**](ControlLastBooted.md) |  | [optional] 
**last_booted_reason** | [**ControlLastBootedReason**](ControlLastBootedReason.md) |  | [optional] 
**last_change** | [**ControlLastChange**](ControlLastChange.md) |  | [optional] 
**part_number** | [**ControlPartNumber**](ControlPartNumber.md) |  | [optional] 
**removable** | [**ControlRemovable**](ControlRemovable.md) |  | [optional] 
**failure_reason** | [**ControlFailureReason**](ControlFailureReason.md) |  | [optional] 
**clei_code** | [**ControlCleiCode**](ControlCleiCode.md) |  | [optional] 
**serial_number** | [**ControlSerialNumber**](ControlSerialNumber.md) |  | [optional] 
**manufactured_date** | [**ControlManufacturedDate**](ControlManufacturedDate.md) |  | [optional] 
**rebooting_at** | [**ControlRebootingAt**](ControlRebootingAt.md) |  | [optional] 
**software_version** | [**ControlSoftwareVersion**](ControlSoftwareVersion.md) |  | [optional] 
**locator_state** | [**ControlLocatorState**](ControlLocatorState.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.control import Control

# TODO update the JSON string below
json = "{}"
# create an instance of Control from a JSON string
control_instance = Control.from_json(json)
# print the JSON string representation of the object
print(Control.to_json())

# convert the object into a dict
control_dict = control_instance.to_dict()
# create an instance of Control from a dict
control_from_dict = Control.from_dict(control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


