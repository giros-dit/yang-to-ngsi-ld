# NetworkInstanceTcpConnection

List of TCP connections that are established or that are in the process of being established – i.e. excluding those in the LISTEN state. An entry in this list is transient in that it ceases to exist when (or soon after) the connection makes the transition to the CLOSED state.  YANG module: srl_nokia-tcp-udp.yang 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity id.  | [optional] 
**type** | **str** | NGSI-LD Entity identifier. It has to be NetworkInstanceTcpConnection. | [default to 'NetworkInstanceTcpConnection']
**scope** | [**EntityScope**](EntityScope.md) |  | [optional] 
**location** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**observation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**operation_space** | [**GeoProperty**](GeoProperty.md) |  | [optional] 
**created_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system.  | [optional] [readonly] 
**modified_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value.  | [optional] [readonly] 
**deleted_at** | **datetime** | Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32).  | [optional] [readonly] 
**local_address** | [**NetworkInstanceTcpConnectionLocalAddress**](NetworkInstanceTcpConnectionLocalAddress.md) |  | [optional] 
**local_port** | [**NetworkInstanceTcpConnectionLocalPort**](NetworkInstanceTcpConnectionLocalPort.md) |  | [optional] 
**remote_address** | [**RemoteAddress**](RemoteAddress.md) |  | [optional] 
**remote_port** | [**RemotePort**](RemotePort.md) |  | [optional] 
**session_state** | [**SessionState**](SessionState.md) |  | [optional] 
**process_id** | [**NetworkInstanceTcpConnectionProcessId**](NetworkInstanceTcpConnectionProcessId.md) |  | [optional] 
**is_part_of** | [**IsPartOf**](IsPartOf.md) |  | 

## Example

```python
from ngsi_ld_models.models.network_instance_tcp_connection import NetworkInstanceTcpConnection

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInstanceTcpConnection from a JSON string
network_instance_tcp_connection_instance = NetworkInstanceTcpConnection.from_json(json)
# print the JSON string representation of the object
print(NetworkInstanceTcpConnection.to_json())

# convert the object into a dict
network_instance_tcp_connection_dict = network_instance_tcp_connection_instance.to_dict()
# create an instance of NetworkInstanceTcpConnection from a dict
network_instance_tcp_connection_from_dict = NetworkInstanceTcpConnection.from_dict(network_instance_tcp_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


