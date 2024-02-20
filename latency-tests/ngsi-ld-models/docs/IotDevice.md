# IotDevice

NGSI-LD Entity Type that represents an IoT device. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be IotDevice. | [default to 'IotDevice']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**name** | [**Name**](Name.md) |  | 
**description** | [**Description**](Description.md) |  | [optional] 
**has_sensor** | [**HasSensor**](HasSensor.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.iot_device import IotDevice

# TODO update the JSON string below
json = "{}"
# create an instance of IotDevice from a JSON string
iot_device_instance = IotDevice.from_json(json)
# print the JSON string representation of the object
print IotDevice.to_json()

# convert the object into a dict
iot_device_dict = iot_device_instance.to_dict()
# create an instance of IotDevice from a dict
iot_device_form_dict = iot_device.from_dict(iot_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


