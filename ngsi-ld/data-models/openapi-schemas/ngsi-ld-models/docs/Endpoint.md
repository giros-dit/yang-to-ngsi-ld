# Endpoint

5.2.15 represents the parameters that are required in order to define an endpoint for notifications. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | URI which conveys the endpoint which will receive the notification.  | 
**accept** | **str** | Intended to convey the MIME type of the notification payload body (JSON, or JSON-LD, or GeoJSON). If not present, default is \&quot;application/json\&quot;.  | [optional] 
**timeout** | **float** | Maximum period of time in milliseconds which may elapse before a notification is assumed to have failed. The NGSI-LD system can override this value. This only applies if the binding protocol always returns a response.  | [optional] 
**cooldown** | **float** | Once a failure has occurred, minimum period of time in milliseconds which shall elapse before attempting to make a subsequent notification to the same endpoint after failure. If requests are received before the cooldown period has expired, no notification is sent.  | [optional] 
**receiver_info** | [**List[KeyValuePair]**](KeyValuePair.md) | Generic {key, value} array to convey optional information to the receiver.  | [optional] 
**notifier_info** | [**List[KeyValuePair]**](KeyValuePair.md) | Generic {key, value} array to set up the communication channel.  | [optional] 

## Example

```python
from ngsi_ld_models.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print Endpoint.to_json()

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_form_dict = endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


