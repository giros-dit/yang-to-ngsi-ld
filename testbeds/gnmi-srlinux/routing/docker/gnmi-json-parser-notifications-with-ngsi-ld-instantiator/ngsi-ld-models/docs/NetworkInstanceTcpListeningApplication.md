# NetworkInstanceTcpListeningApplication

List of applications that are listening on a particular TCP port bound to the network-instance.  YANG module: srl_nokia-tcp-udp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceTcpListeningApplication. | [default to 'NetworkInstanceTcpListeningApplication']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**local_address** | [**NetworkInstanceTcpListeningApplicationLocalAddress**](NetworkInstanceTcpListeningApplicationLocalAddress.md) |  | [optional] 
**local_port** | [**NetworkInstanceTcpListeningApplicationLocalPort**](NetworkInstanceTcpListeningApplicationLocalPort.md) |  | [optional] 
**process_id** | [**NetworkInstanceTcpListeningApplicationProcessId**](NetworkInstanceTcpListeningApplicationProcessId.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_tcp_listening_application import NetworkInstanceTcpListeningApplication

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceTcpListeningApplication from a JSON string
network_instance_tcp_listening_application_instance = NetworkInstanceTcpListeningApplication.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceTcpListeningApplication.to_json())

# convert the object into a dict
network_instance_tcp_listening_application_dict = network_instance_tcp_listening_application_instance.to_dict()
# create an instance of NetworkInstanceTcpListeningApplication from a dict
network_instance_tcp_listening_application_from_dict = NetworkInstanceTcpListeningApplication.from_dict(network_instance_tcp_listening_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


