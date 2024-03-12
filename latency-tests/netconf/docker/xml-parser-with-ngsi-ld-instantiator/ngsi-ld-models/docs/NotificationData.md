# NotificationData

The content of the notification as NGSI-LD Entities. See clause 5.2.4.  If the notification has been triggered from a Subscription that has the notification. endpoint.accept field set to application/geo+json then data is returned as a FeatureCollection. In this case, if the notification.endpoint.rece iverInfo contains the key \"Prefer\" and it is set to the value \"body=json\", then the FeatureCollection will not contain an @context field.  If endpoint.accept is not set or holds another value then Entity[] is returned. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | GeoJSON Type.  | 
**features** | [**List[Feature]**](Feature.md) | In the case that no matches are found, \&quot;features\&quot; will be an empty array.  | [optional] 
**context** | [**LdContext**](LdContext.md) |  | [optional] 

## Example

```python
from ngsi_ld_models.models.notification_data import NotificationData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationData from a JSON string
notification_data_instance = NotificationData.from_json(json)
# print the JSON string representation of the object
print NotificationData.to_json()

# convert the object into a dict
notification_data_dict = notification_data_instance.to_dict()
# create an instance of NotificationData from a dict
notification_data_form_dict = notification_data.from_dict(notification_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


