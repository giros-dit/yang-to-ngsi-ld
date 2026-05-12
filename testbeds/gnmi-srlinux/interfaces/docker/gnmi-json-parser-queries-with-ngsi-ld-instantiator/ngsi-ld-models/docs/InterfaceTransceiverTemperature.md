# InterfaceTransceiverTemperature

 YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceTransceiverTemperature. | [default to 'InterfaceTransceiverTemperature']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**latest_value** | [**InterfaceTransceiverTemperatureLatestValue**](InterfaceTransceiverTemperatureLatestValue.md) |  | [optional] 
**maximum** | [**InterfaceTransceiverTemperatureMaximum**](InterfaceTransceiverTemperatureMaximum.md) |  | [optional] 
**maximum_time** | [**InterfaceTransceiverTemperatureMaximumTime**](InterfaceTransceiverTemperatureMaximumTime.md) |  | [optional] 
**high_alarm_condition** | [**InterfaceTransceiverTemperatureHighAlarmCondition**](InterfaceTransceiverTemperatureHighAlarmCondition.md) |  | [optional] 
**high_alarm_threshold** | [**InterfaceTransceiverTemperatureHighAlarmThreshold**](InterfaceTransceiverTemperatureHighAlarmThreshold.md) |  | [optional] 
**low_alarm_condition** | [**InterfaceTransceiverTemperatureLowAlarmCondition**](InterfaceTransceiverTemperatureLowAlarmCondition.md) |  | [optional] 
**low_alarm_threshold** | [**InterfaceTransceiverTemperatureLowAlarmThreshold**](InterfaceTransceiverTemperatureLowAlarmThreshold.md) |  | [optional] 
**high_warning_condition** | [**InterfaceTransceiverTemperatureHighWarningCondition**](InterfaceTransceiverTemperatureHighWarningCondition.md) |  | [optional] 
**high_warning_threshold** | [**InterfaceTransceiverTemperatureHighWarningThreshold**](InterfaceTransceiverTemperatureHighWarningThreshold.md) |  | [optional] 
**low_warning_condition** | [**InterfaceTransceiverTemperatureLowWarningCondition**](InterfaceTransceiverTemperatureLowWarningCondition.md) |  | [optional] 
**low_warning_threshold** | [**InterfaceTransceiverTemperatureLowWarningThreshold**](InterfaceTransceiverTemperatureLowWarningThreshold.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_transceiver_temperature import InterfaceTransceiverTemperature

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceTransceiverTemperature from a JSON string
interface_transceiver_temperature_instance = InterfaceTransceiverTemperature.from_json(json)
# print the JSON string representation of the object
print InterfaceTransceiverTemperature.to_json()

# convert the object into a dict
interface_transceiver_temperature_dict = interface_transceiver_temperature_instance.to_dict()
# create an instance of InterfaceTransceiverTemperature from a dict
interface_transceiver_temperature_form_dict = interface_transceiver_temperature.from_dict(interface_transceiver_temperature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


