# NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs

When present, topology and TE information related to this protocol instance is installed into the TE database in a format that supports export as BGP-LS routes  YANG module: srl_nokia-traffic-engineering.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs. | [default to 'NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**igp_identifier** | [**NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLsIgpIdentifier**](NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLsIgpIdentifier.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_protocols_directly_connected_te_database_install_bgp_ls import NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs from a JSON string
network_instance_protocols_directly_connected_te_database_install_bgp_ls_instance = NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs.to_json())

# convert the object into a dict
network_instance_protocols_directly_connected_te_database_install_bgp_ls_dict = network_instance_protocols_directly_connected_te_database_install_bgp_ls_instance.to_dict()
# create an instance of NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs from a dict
network_instance_protocols_directly_connected_te_database_install_bgp_ls_from_dict = NetworkInstanceProtocolsDirectlyConnectedTeDatabaseInstallBgpLs.from_dict(network_instance_protocols_directly_connected_te_database_install_bgp_ls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


