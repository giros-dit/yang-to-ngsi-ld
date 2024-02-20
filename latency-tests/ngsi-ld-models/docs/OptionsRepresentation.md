# OptionsRepresentation

6.3.7 Representation of Entities. When its value includes the keyword \"normalized\", a normalized representation of Entities shall be provided as defined by clause 4.5.1, with Attributes returned in the normalized representation as defined in clauses 4.5.2.2, 4.5.3.2 and 4.5.18.2.  When its value includes the keyword \"concise\", a concise lossless representation of Entities shall be provided as defined by clause 4.5.1. with Attributes returned in the concise representation as defined in clauses 4.5.2.3, 4.5.3.3 and 4.5.18.3. In this case the broker will return data in the most concise lossless representation possible, for example removing all Attribute \"type\" members.  When its value includes the keyword \"keyValues\" (or \"simplified\" as a synonym), a simplified representation of Entities shall be provided as defined by clause 4.5.4.  If the Accept Header is set to \"application/geo+json\" the response will be in simplified GeoJSON format as defined by clause 4.5.17. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


