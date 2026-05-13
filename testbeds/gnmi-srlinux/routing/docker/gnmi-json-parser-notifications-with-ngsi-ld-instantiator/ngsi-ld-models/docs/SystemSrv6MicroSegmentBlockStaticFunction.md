# SystemSrv6MicroSegmentBlockStaticFunction

Enter the static-function context  YANG module: srl_nokia-srv6.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SystemSrv6MicroSegmentBlockStaticFunction. | [default to 'SystemSrv6MicroSegmentBlockStaticFunction']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**max_entries** | [**SystemSrv6MicroSegmentBlockStaticFunctionMaxEntries**](SystemSrv6MicroSegmentBlockStaticFunctionMaxEntries.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.system_srv6_micro_segment_block_static_function import SystemSrv6MicroSegmentBlockStaticFunction

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSrv6MicroSegmentBlockStaticFunction from a JSON string
system_srv6_micro_segment_block_static_function_instance = SystemSrv6MicroSegmentBlockStaticFunction.from_json(json)
# print the JSON string representation of the object
print(SystemSrv6MicroSegmentBlockStaticFunction.to_json())

# convert the object into a dict
system_srv6_micro_segment_block_static_function_dict = system_srv6_micro_segment_block_static_function_instance.to_dict()
# create an instance of SystemSrv6MicroSegmentBlockStaticFunction from a dict
system_srv6_micro_segment_block_static_function_from_dict = SystemSrv6MicroSegmentBlockStaticFunction.from_dict(system_srv6_micro_segment_block_static_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


