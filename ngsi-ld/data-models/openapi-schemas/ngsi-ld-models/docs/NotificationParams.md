# NotificationParams

5.2.14 represents the parameters that allow to convey the details of a notification. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | Entity Attribute Names (Properties or Relationships) to be included in the notification payload body. If undefined it will mean all Attributes.  | [optional] 
**sys_attrs** | **bool** | If true, the system generated attributes createdAt and modifiedAt are included in the response payload body, in the case of a deletion also deletedAt.  | [optional] 
**format** | **str** | Conveys the representation format of the entities delivered at notification time. By default, it will be in the normalized format.  | [optional] 
**show_changes** | **bool** | If true the previous value (previousValue) of Properties or languageMap (previousLanguageMap) of Language Properties or object (previousObject) of Relationships is provided in addition to the current one. This requires that it exists, i.e. in case of modifications and deletions,  but not in the case of creations. showChanges cannot be true in case format is \&quot;keyValues\&quot;.  | [optional] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | 
**status** | **str** | Status of the Notification. It shall be \&quot;ok\&quot; if the last attempt to notify the subscriber succeeded. It shall be \&quot;failed\&quot; if the last attempt to notify the subscriber failed.  | [optional] 
**times_sent** | **float** | Number of times that the notification has been sent. Provided by the system when querying the details of a subscription.  | [optional] 
**times_failed** | **float** | Number of times an unsuccessful response (or timeout) has been received when deliverying the notification. Provided by the system when querying the details of a subscription.  | [optional] 
**last_notification** | **datetime** | Timestamp corresponding to the instant when the last notification has been sent. Provided by the system when querying the details of a subscription.  | [optional] 
**last_failure** | **datetime** | Timestamp corresponding to the instant when the last notification resulting in failure (for instance, in the HTTP binding, an HTTP response code different than 200) has been sent. Provided by the system when querying the details of a subscription.  | [optional] 
**last_success** | **datetime** | Timestamp corresponding to the instant when the last successful (200 OK response) notification has been sent. Provided by the system when querying the details of a subscription.  | [optional] 

## Example

```python
from ngsi_ld_models.models.notification_params import NotificationParams

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationParams from a JSON string
notification_params_instance = NotificationParams.from_json(json)
# print the JSON string representation of the object
print NotificationParams.to_json()

# convert the object into a dict
notification_params_dict = notification_params_instance.to_dict()
# create an instance of NotificationParams from a dict
notification_params_form_dict = notification_params.from_dict(notification_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


