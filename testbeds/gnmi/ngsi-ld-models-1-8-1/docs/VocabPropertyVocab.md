# VocabPropertyVocab

String Values which shall be type coerced to URIs based on the supplied @context. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ngsi_ld_models_1_8_1.models.vocab_property_vocab import VocabPropertyVocab

# TODO update the JSON string below
json = "{}"
# create an instance of VocabPropertyVocab from a JSON string
vocab_property_vocab_instance = VocabPropertyVocab.from_json(json)
# print the JSON string representation of the object
print(VocabPropertyVocab.to_json())

# convert the object into a dict
vocab_property_vocab_dict = vocab_property_vocab_instance.to_dict()
# create an instance of VocabPropertyVocab from a dict
vocab_property_vocab_from_dict = VocabPropertyVocab.from_dict(vocab_property_vocab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


