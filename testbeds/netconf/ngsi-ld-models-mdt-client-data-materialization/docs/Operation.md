# Operation

NGSI-LD Property Type. The NETCONF RPC operation (i.e., GET, SET, or SUBSCRIBE). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Node type.  | [optional] [default to 'Property']
**value** | **str** |  | 
**observed_at** | **datetime** | It is defined as the temporal Property at which a certain Property or Relationship became valid or was observed. For example, a temperature Value was measured by the sensor at this point in time.  | [optional] 
**unit_code** | **str** | Property Value&#39;s unit code.  | [optional] 
**dataset_id** | **str** | It allows identifying a set or group of property values.  | [optional] 
**created_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  Entity creation timestamp. See clause 4.8.  | [optional] 
**modified_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  Entity last modification timestamp. See clause 4.8.  | [optional] 
**deleted_at** | **datetime** | It is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8. It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] 
**instance_id** | **str** | A URI uniquely identifying a Property instance as  mandated by clause 4.5.7. System generated. Only used in temporal representation of Properties.  | [optional] [readonly] 
**previous_value** | [**PropertyPreviousValue**](PropertyPreviousValue.md) |  | [optional] 
**get_option** | [**GetOption**](GetOption.md) |  | [optional] 
**subscription_mode** | [**SubscriptionMode**](SubscriptionMode.md) |  | [optional] 
**subscription_state** | [**SubscriptionState**](SubscriptionState.md) |  | [optional] 
**entity_type** | [**NGSILDEntityType**](NGSILDEntityType.md) |  | [optional] 
**entity_id** | [**NGSILDEntityId**](NGSILDEntityId.md) |  | [optional] 

## Example

```python
from ngsi_ld_models_mdt_client_data_materialization.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


