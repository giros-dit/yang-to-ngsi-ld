# SystemSrv6

Enter the srv6 context to configure locators and other SRv6 functionalities  YANG module: srl_nokia-srv6.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be SystemSrv6. | [default to 'SystemSrv6']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**default_source_address** | [**DefaultSourceAddress**](DefaultSourceAddress.md) |  | 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.system_srv6 import SystemSrv6

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSrv6 from a JSON string
system_srv6_instance = SystemSrv6.from_json(json)
# print the JSON string representation of the object
print(SystemSrv6.to_json())

# convert the object into a dict
system_srv6_dict = system_srv6_instance.to_dict()
# create an instance of SystemSrv6 from a dict
system_srv6_from_dict = SystemSrv6.from_dict(system_srv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


