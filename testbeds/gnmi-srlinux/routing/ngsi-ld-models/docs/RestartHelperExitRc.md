# RestartHelperExitRc

the value of restart-helper-exit-rc indicates the outcome of the last attempt at acting as a graceful restart helper for the neighbor. none no restart has yet been attempted. in-progress A restart attempt is currently underway. completed the last restart completed successfully. timed-out the last restart timed out. topology-changed the last restart was aborted due to a topology change.  YANG module: srl_nokia-ospf.yang 

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
from ngsi_ld_models.models.restart_helper_exit_rc import RestartHelperExitRc

# TODO update the JSON string below
json = "{}"
# create an instance of RestartHelperExitRc from a JSON string
restart_helper_exit_rc_instance = RestartHelperExitRc.from_json(json)
# print the JSON string representation of the object
print(RestartHelperExitRc.to_json())

# convert the object into a dict
restart_helper_exit_rc_dict = restart_helper_exit_rc_instance.to_dict()
# create an instance of RestartHelperExitRc from a dict
restart_helper_exit_rc_from_dict = RestartHelperExitRc.from_dict(restart_helper_exit_rc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


