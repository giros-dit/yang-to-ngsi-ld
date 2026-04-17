# LinecardTemperatureAlarmStatus

Indicates if a temperature sensor of this component is currently in an alarm state  An alarm state is triggered if the margin is <=2 degrees, indicating that a thermal protection shut down is imminent unless adequate system cooling is provided to bring the temperature sensor back into safe operating ranges.  YANG module: srl_nokia-platform-lc.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **bool** |  | 
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
from ngsi_ld_models.models.linecard_temperature_alarm_status import LinecardTemperatureAlarmStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LinecardTemperatureAlarmStatus from a JSON string
linecard_temperature_alarm_status_instance = LinecardTemperatureAlarmStatus.from_json(json)
# print the JSON string representation of the object
print(LinecardTemperatureAlarmStatus.to_json())

# convert the object into a dict
linecard_temperature_alarm_status_dict = linecard_temperature_alarm_status_instance.to_dict()
# create an instance of LinecardTemperatureAlarmStatus from a dict
linecard_temperature_alarm_status_from_dict = LinecardTemperatureAlarmStatus.from_dict(linecard_temperature_alarm_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


