# LinecardForwardingComplexFibTableProgrammingProgressMplsLabels

Container for the FIB programming state of ILM entries  YANG module: srl_nokia-ip-route-tables.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be LinecardForwardingComplexFibTableProgrammingProgressMplsLabels. | [default to 'LinecardForwardingComplexFibTableProgrammingProgressMplsLabels']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**entries_remaining_to_add** | [**LinecardForwardingComplexFibTableProgrammingProgressMplsLabelsEntriesRemainingToAdd**](LinecardForwardingComplexFibTableProgrammingProgressMplsLabelsEntriesRemainingToAdd.md) |  | [optional] 
**entries_remaining_to_modify** | [**LinecardForwardingComplexFibTableProgrammingProgressMplsLabelsEntriesRemainingToModify**](LinecardForwardingComplexFibTableProgrammingProgressMplsLabelsEntriesRemainingToModify.md) |  | [optional] 
**last_sync_time** | [**LinecardForwardingComplexFibTableProgrammingProgressMplsLabelsLastSyncTime**](LinecardForwardingComplexFibTableProgrammingProgressMplsLabelsLastSyncTime.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.linecard_forwarding_complex_fib_table_programming_progress_mpls_labels import LinecardForwardingComplexFibTableProgrammingProgressMplsLabels

# TODO update the JSON string below
json = "{}"
# create an instance of LinecardForwardingComplexFibTableProgrammingProgressMplsLabels from a JSON string
linecard_forwarding_complex_fib_table_programming_progress_mpls_labels_instance = LinecardForwardingComplexFibTableProgrammingProgressMplsLabels.from_json(json)
# print the JSON string representation of the object
print(LinecardForwardingComplexFibTableProgrammingProgressMplsLabels.to_json())

# convert the object into a dict
linecard_forwarding_complex_fib_table_programming_progress_mpls_labels_dict = linecard_forwarding_complex_fib_table_programming_progress_mpls_labels_instance.to_dict()
# create an instance of LinecardForwardingComplexFibTableProgrammingProgressMplsLabels from a dict
linecard_forwarding_complex_fib_table_programming_progress_mpls_labels_from_dict = LinecardForwardingComplexFibTableProgrammingProgressMplsLabels.from_dict(linecard_forwarding_complex_fib_table_programming_progress_mpls_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


