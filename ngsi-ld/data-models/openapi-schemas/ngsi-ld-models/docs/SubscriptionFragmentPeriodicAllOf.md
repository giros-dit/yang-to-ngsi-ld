# SubscriptionFragmentPeriodicAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_interval** | **float** | Indicates that a notification shall be delivered periodically regardless of attribute changes. Actually, when the time interval (in seconds) specified in this value field is reached.  | [optional] 

## Example

```python
from ngsi_ld_models.models.subscription_fragment_periodic_all_of import SubscriptionFragmentPeriodicAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionFragmentPeriodicAllOf from a JSON string
subscription_fragment_periodic_all_of_instance = SubscriptionFragmentPeriodicAllOf.from_json(json)
# print the JSON string representation of the object
print SubscriptionFragmentPeriodicAllOf.to_json()

# convert the object into a dict
subscription_fragment_periodic_all_of_dict = subscription_fragment_periodic_all_of_instance.to_dict()
# create an instance of SubscriptionFragmentPeriodicAllOf from a dict
subscription_fragment_periodic_all_of_form_dict = subscription_fragment_periodic_all_of.from_dict(subscription_fragment_periodic_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


