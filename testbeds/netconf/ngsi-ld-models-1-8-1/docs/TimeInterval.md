# TimeInterval

5.2.11 NGSI-LD TimeInterval. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **datetime** | Describes the start of the time interval.  | 
**end_at** | **datetime** | Describes the end of the time interval. If not present the interval is open.  | [optional] 

## Example

```python
from ngsi_ld_models_1_8_1.models.time_interval import TimeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of TimeInterval from a JSON string
time_interval_instance = TimeInterval.from_json(json)
# print the JSON string representation of the object
print(TimeInterval.to_json())

# convert the object into a dict
time_interval_dict = time_interval_instance.to_dict()
# create an instance of TimeInterval from a dict
time_interval_from_dict = TimeInterval.from_dict(time_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


