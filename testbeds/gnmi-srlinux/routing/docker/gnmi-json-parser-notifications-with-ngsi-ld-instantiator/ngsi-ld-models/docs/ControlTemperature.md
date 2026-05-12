# ControlTemperature

State related to temperature for this component  YANG module: srl_nokia-platform-control.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be ControlTemperature. | [default to 'ControlTemperature']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**instant** | [**ControlTemperatureInstant**](ControlTemperatureInstant.md) |  | [optional] 
**maximum** | [**ControlTemperatureMaximum**](ControlTemperatureMaximum.md) |  | [optional] 
**maximum_time** | [**ControlTemperatureMaximumTime**](ControlTemperatureMaximumTime.md) |  | [optional] 
**alarm_status** | [**ControlTemperatureAlarmStatus**](ControlTemperatureAlarmStatus.md) |  | [optional] 
**margin** | [**ControlTemperatureMargin**](ControlTemperatureMargin.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.control_temperature import ControlTemperature

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTemperature from a JSON string
control_temperature_instance = ControlTemperature.from_json(json)
# print the JSON string representation of the object
print(ControlTemperature.to_json())

# convert the object into a dict
control_temperature_dict = control_temperature_instance.to_dict()
# create an instance of ControlTemperature from a dict
control_temperature_from_dict = ControlTemperature.from_dict(control_temperature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


