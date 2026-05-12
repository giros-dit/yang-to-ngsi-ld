# InterfaceTransceiverVoltage

 YANG module: srl_nokia-interfaces.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be InterfaceTransceiverVoltage. | [default to 'InterfaceTransceiverVoltage']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**latest_value** | [**InterfaceTransceiverVoltageLatestValue**](InterfaceTransceiverVoltageLatestValue.md) |  | [optional] 
**high_alarm_condition** | [**InterfaceTransceiverVoltageHighAlarmCondition**](InterfaceTransceiverVoltageHighAlarmCondition.md) |  | [optional] 
**high_alarm_threshold** | [**InterfaceTransceiverVoltageHighAlarmThreshold**](InterfaceTransceiverVoltageHighAlarmThreshold.md) |  | [optional] 
**low_alarm_condition** | [**InterfaceTransceiverVoltageLowAlarmCondition**](InterfaceTransceiverVoltageLowAlarmCondition.md) |  | [optional] 
**low_alarm_threshold** | [**InterfaceTransceiverVoltageLowAlarmThreshold**](InterfaceTransceiverVoltageLowAlarmThreshold.md) |  | [optional] 
**high_warning_condition** | [**InterfaceTransceiverVoltageHighWarningCondition**](InterfaceTransceiverVoltageHighWarningCondition.md) |  | [optional] 
**high_warning_threshold** | [**InterfaceTransceiverVoltageHighWarningThreshold**](InterfaceTransceiverVoltageHighWarningThreshold.md) |  | [optional] 
**low_warning_condition** | [**InterfaceTransceiverVoltageLowWarningCondition**](InterfaceTransceiverVoltageLowWarningCondition.md) |  | [optional] 
**low_warning_threshold** | [**InterfaceTransceiverVoltageLowWarningThreshold**](InterfaceTransceiverVoltageLowWarningThreshold.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.interface_transceiver_voltage import InterfaceTransceiverVoltage

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceTransceiverVoltage from a JSON string
interface_transceiver_voltage_instance = InterfaceTransceiverVoltage.from_json(json)
# print the JSON string representation of the object
print InterfaceTransceiverVoltage.to_json()

# convert the object into a dict
interface_transceiver_voltage_dict = interface_transceiver_voltage_instance.to_dict()
# create an instance of InterfaceTransceiverVoltage from a dict
interface_transceiver_voltage_form_dict = interface_transceiver_voltage.from_dict(interface_transceiver_voltage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


