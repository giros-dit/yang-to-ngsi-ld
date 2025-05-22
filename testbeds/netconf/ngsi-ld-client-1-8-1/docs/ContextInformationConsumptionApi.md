# ngsi_ld_client_1_8_1.ContextInformationConsumptionApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_batch**](ContextInformationConsumptionApi.md#query_batch) | **POST** /entityOperations/query | Query entities based on POST 
[**query_entity**](ContextInformationConsumptionApi.md#query_entity) | **GET** /entities | Query entities 
[**retrieve_attr_type_info**](ContextInformationConsumptionApi.md#retrieve_attr_type_info) | **GET** /attributes/{attrId} | Details about available attribute 
[**retrieve_attr_types**](ContextInformationConsumptionApi.md#retrieve_attr_types) | **GET** /attributes | Available attributes 
[**retrieve_entity**](ContextInformationConsumptionApi.md#retrieve_entity) | **GET** /entities/{entityId} | Entity retrieval by id 
[**retrieve_entity_type_info**](ContextInformationConsumptionApi.md#retrieve_entity_type_info) | **GET** /types/{type} | Details about available entity type 
[**retrieve_entity_types**](ContextInformationConsumptionApi.md#retrieve_entity_types) | **GET** /types | Retrieve available entity types  


# **query_batch**
> List[QueryEntity200ResponseInner] query_batch(count=count, limit=limit, local=local, options=options, link=link, ngsild_tenant=ngsild_tenant, via=via, query=query)

Query entities based on POST 

5.7.2 Query Entity (batch entity queries only).  This operation allows querying an NGSI-LD system. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.query import Query
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    count = True # bool | 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \"limit\" URI parameter), the total number of matching results (e.g. number of Entities) is returned.  (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    options = [ngsi_ld_client_1_8_1.OptionsRepresentation()] # List[OptionsRepresentation] |  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)
    query = ngsi_ld_client_1_8_1.Query() # Query | Payload body in the request contains a JSON-LD object which represents the query to be performed. (optional)

    try:
        # Query entities based on POST 
        api_response = api_instance.query_batch(count=count, limit=limit, local=local, options=options, link=link, ngsild_tenant=ngsild_tenant, via=via, query=query)
        print("The response of ContextInformationConsumptionApi->query_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->query_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **bool**| 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \&quot;limit\&quot; URI parameter), the total number of matching results (e.g. number of Entities) is returned.  | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **options** | [**List[OptionsRepresentation]**](OptionsRepresentation.md)|  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 
 **query** | [**Query**](Query.md)| Payload body in the request contains a JSON-LD object which represents the query to be performed. | [optional] 

### Return type

[**List[QueryEntity200ResponseInner]**](QueryEntity200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/json+ld
 - **Accept**: application/json, application/json+ld, application/geo+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the query result as a list of Entities.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_entity**
> List[QueryEntity200ResponseInner] query_entity(id=id, type=type, id_pattern=id_pattern, attrs=attrs, pick=pick, omit=omit, q=q, csf=csf, geometry=geometry, georel=georel, coordinates=coordinates, geoproperty=geoproperty, geometry_property=geometry_property, lang=lang, scope_q=scope_q, contained_by=contained_by, join=join, join_level=join_level, dataset_id=dataset_id, details=details, limit=limit, count=count, options=options, format=format, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Query entities 

5.7.2 Query Entities (excluding batch entity queries).  This operation allows querying an NGSI-LD system. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.format_representation import FormatRepresentation
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
from ngsi_ld_client_1_8_1.models.query_entity_options_parameter_inner import QueryEntityOptionsParameterInner
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    id = ['id_example'] # List[str] | List of entity ids to be retrieved. (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    id_pattern = 'id_pattern_example' # str | Regular expression that shall be matched by entity ids. (optional)
    attrs = ['attrs_example'] # List[str] | List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  A synonym for a combination of the pick and q parameters. DEPRECATED. Each String is an Attribute (Property or Relationship) name.  (optional)
    pick = ['pick_example'] # List[str] | Each String is an Entity member (\"id\", \"type\", \"scope\" or a projected Attribute name). When defined, every Entity within the payload body is reduced down to only contain  the listed Entity members.  (optional)
    omit = ['omit_example'] # List[str] | Each String is an Entity member (\"id\", \"type\", \"scope\" or a projected Attribute name).  When defined, the listed Entity members are removed from each Entity within the payload.  (optional)
    q = 'q_example' # str | Query as per clause 4.9.  (optional)
    csf = 'csf_example' # str | Context Source filter as per clause 4.9. (optional)
    geometry = 'geometry_example' # str | Geometry as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    georel = ngsi_ld_client_1_8_1.QueryEntityGeorelParameter() # QueryEntityGeorelParameter | Geo relationship as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    coordinates = ngsi_ld_client_1_8_1.QueryEntityCoordinatesParameter() # QueryEntityCoordinatesParameter | Coordinates serialized as a string as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    geoproperty = location # str | The name of the Property that contains the geospatial data that will be used to resolve the geoquery. By default, will be location (see clause 4.7). It shall be ignored unless a geoquery is present.  (optional) (default to location)
    geometry_property = 'geometry_property_example' # str | 4.5.16.1 Top-level \"geometry\" field selection algorithm.  A parameter of the request (named \"geometryProperty\") may be used to indicate the name of the GeoProperty to be selected.  If this parameter is not present, then the default name of \"location\" shall be used.  In the case of GeoJSON Entity representation, this parameter indicates which GeoProperty to use for the toplevel geometry field.  (optional)
    lang = 'lang_example' # str | It is used to reduce languageMaps to a string or string array property in a single preferred language.  (optional)
    scope_q = 'scope_q_example' # str | Scope query (see clause 4.19).  (optional)
    contained_by = ['contained_by_example'] # List[str] | List of entity ids which have previously been encountered whilst retrieving the  Entity Graph. Only applicable if joinLevel is present.  (optional)
    join = 'join_example' # str | The type of Linked Entity retrieval to apply (see clause 4.5.23). Allowed values: \"flat\", \"inline\", \"@none\".  (optional)
    join_level = 56 # int | Depth of Linked Entity retrieval to apply. Only applicable if join parameter is present.  (optional)
    dataset_id = ngsi_ld_client_1_8_1.QueryEntityDatasetIdParameter() # QueryEntityDatasetIdParameter | Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  (optional)
    details = True # bool | If true, the location of the EntityMap used in the operation is returned in the response. (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    count = True # bool | 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \"limit\" URI parameter), the total number of matching results (e.g. number of Entities) is returned.  (optional)
    options = [ngsi_ld_client_1_8_1.QueryEntityOptionsParameterInner()] # List[QueryEntityOptionsParameterInner] |  (optional)
    format = ngsi_ld_client_1_8_1.FormatRepresentation() # FormatRepresentation |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Query entities 
        api_response = api_instance.query_entity(id=id, type=type, id_pattern=id_pattern, attrs=attrs, pick=pick, omit=omit, q=q, csf=csf, geometry=geometry, georel=georel, coordinates=coordinates, geoproperty=geoproperty, geometry_property=geometry_property, lang=lang, scope_q=scope_q, contained_by=contained_by, join=join, join_level=join_level, dataset_id=dataset_id, details=details, limit=limit, count=count, options=options, format=format, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationConsumptionApi->query_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->query_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| List of entity ids to be retrieved. | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **id_pattern** | **str**| Regular expression that shall be matched by entity ids. | [optional] 
 **attrs** | [**List[str]**](str.md)| List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  A synonym for a combination of the pick and q parameters. DEPRECATED. Each String is an Attribute (Property or Relationship) name.  | [optional] 
 **pick** | [**List[str]**](str.md)| Each String is an Entity member (\&quot;id\&quot;, \&quot;type\&quot;, \&quot;scope\&quot; or a projected Attribute name). When defined, every Entity within the payload body is reduced down to only contain  the listed Entity members.  | [optional] 
 **omit** | [**List[str]**](str.md)| Each String is an Entity member (\&quot;id\&quot;, \&quot;type\&quot;, \&quot;scope\&quot; or a projected Attribute name).  When defined, the listed Entity members are removed from each Entity within the payload.  | [optional] 
 **q** | **str**| Query as per clause 4.9.  | [optional] 
 **csf** | **str**| Context Source filter as per clause 4.9. | [optional] 
 **geometry** | **str**| Geometry as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **georel** | [**QueryEntityGeorelParameter**](.md)| Geo relationship as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **coordinates** | [**QueryEntityCoordinatesParameter**](.md)| Coordinates serialized as a string as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **geoproperty** | **str**| The name of the Property that contains the geospatial data that will be used to resolve the geoquery. By default, will be location (see clause 4.7). It shall be ignored unless a geoquery is present.  | [optional] [default to location]
 **geometry_property** | **str**| 4.5.16.1 Top-level \&quot;geometry\&quot; field selection algorithm.  A parameter of the request (named \&quot;geometryProperty\&quot;) may be used to indicate the name of the GeoProperty to be selected.  If this parameter is not present, then the default name of \&quot;location\&quot; shall be used.  In the case of GeoJSON Entity representation, this parameter indicates which GeoProperty to use for the toplevel geometry field.  | [optional] 
 **lang** | **str**| It is used to reduce languageMaps to a string or string array property in a single preferred language.  | [optional] 
 **scope_q** | **str**| Scope query (see clause 4.19).  | [optional] 
 **contained_by** | [**List[str]**](str.md)| List of entity ids which have previously been encountered whilst retrieving the  Entity Graph. Only applicable if joinLevel is present.  | [optional] 
 **join** | **str**| The type of Linked Entity retrieval to apply (see clause 4.5.23). Allowed values: \&quot;flat\&quot;, \&quot;inline\&quot;, \&quot;@none\&quot;.  | [optional] 
 **join_level** | **int**| Depth of Linked Entity retrieval to apply. Only applicable if join parameter is present.  | [optional] 
 **dataset_id** | [**QueryEntityDatasetIdParameter**](.md)| Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  | [optional] 
 **details** | **bool**| If true, the location of the EntityMap used in the operation is returned in the response. | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **count** | **bool**| 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \&quot;limit\&quot; URI parameter), the total number of matching results (e.g. number of Entities) is returned.  | [optional] 
 **options** | [**List[QueryEntityOptionsParameterInner]**](QueryEntityOptionsParameterInner.md)|  | [optional] 
 **format** | [**FormatRepresentation**](.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**List[QueryEntity200ResponseInner]**](QueryEntity200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the query result as a list of entities, unless the Accept Header indicates that the Entities are to be rendered as GeoJSON.  If the Accept Header indicates that the Entities are to be rendered as GeoJSON, a response body containing the query result as GeoJSON FeatureCollection is returned.  If an EntityMap has been requested, the HTTP response shall include an \&quot;NGSILDEntityMap\&quot; HTTP  header that contains the resource URI of the EntityMap resource used in the operation.  |  * NGSILD-Results-Count -  <br>  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**501** | It is used by Registered Context Sources to indicate that the data format  of the request is unsupported see clause 6.3.7.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_attr_type_info**
> Attribute retrieve_attr_type_info(attr_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Details about available attribute 

5.7.10 Retrieve Available Attribute Information.  This operation allows retrieving detailed attribute information about a specified NGSI-LD attribute that belongs to entity instances existing within the NGSI-LD system. The detailed representation includes the attribute name (as short name if available in the provided @context) and the type names for which entity instances exist that have the respective attribute, a count of available attribute instances and a list of types the attribute can have (e.g. Property, Relationship or GeoProperty). 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.attribute import Attribute
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    attr_id = 'attr_id_example' # str | Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Details about available attribute 
        api_response = api_instance.retrieve_attr_type_info(attr_id, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationConsumptionApi->retrieve_attr_type_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->retrieve_attr_type_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attr_id** | **str**| Name of the attribute for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the detailed information about the available attribute.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_attr_types**
> RetrieveAttrTypes200Response retrieve_attr_types(details=details, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Available attributes 

5.7.8 Retrieve Available Attributes.  This operation allows retrieving a list of NGSI-LD attributes that belong to entity instances existing within the NGSI- LD system.  5.7.9 Retrieve Details of Available Attributes.  This operation allows retrieving a list with a detailed representation of NGSI-LD  attributes that belong to entity instances existing within the NGSI-LD system. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.retrieve_attr_types200_response import RetrieveAttrTypes200Response
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    details = True # bool | If true, then detailed attribute information represented as an array with elements of the Attribute data structure (clause 5.2.28) is to be returned.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Available attributes 
        api_response = api_instance.retrieve_attr_types(details=details, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationConsumptionApi->retrieve_attr_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->retrieve_attr_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **bool**| If true, then detailed attribute information represented as an array with elements of the Attribute data structure (clause 5.2.28) is to be returned.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**RetrieveAttrTypes200Response**](RetrieveAttrTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the AttributeList (clause 5.2.27) is to be returned, unless details&#x3D;true is specified.  If details&#x3D;true is specified, a response body containing a JSON-LD array with elements of the Attribute data structure (clause 5.2.28) is to be returned.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity**
> QueryEntity200ResponseInner retrieve_entity(entity_id, type=type, attrs=attrs, pick=pick, omit=omit, geometry_property=geometry_property, lang=lang, contained_by=contained_by, join=join, join_level=join_level, dataset_id=dataset_id, details=details, options=options, format=format, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Entity retrieval by id 

5.7.1 Retrieve Entity.  This operation allows retrieving an NGSI-LD Entity. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.format_representation import FormatRepresentation
from ngsi_ld_client_1_8_1.models.query_entity200_response_inner import QueryEntity200ResponseInner
from ngsi_ld_client_1_8_1.models.query_entity_options_parameter_inner import QueryEntityOptionsParameterInner
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    entity_id = 'entity_id_example' # str | Id (URI) of the Entity to be retrieved, updated or deleted.
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    attrs = ['attrs_example'] # List[str] | List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  A synonym for a combination of the pick and q parameters. DEPRECATED. Each String is an Attribute (Property or Relationship) name.  (optional)
    pick = ['pick_example'] # List[str] | Each String is an Entity member (\"id\", \"type\", \"scope\" or a projected Attribute name). When defined, every Entity within the payload body is reduced down to only contain  the listed Entity members.  (optional)
    omit = ['omit_example'] # List[str] | Each String is an Entity member (\"id\", \"type\", \"scope\" or a projected Attribute name).  When defined, the listed Entity members are removed from each Entity within the payload.  (optional)
    geometry_property = 'geometry_property_example' # str | 4.5.16.1 Top-level \"geometry\" field selection algorithm.  A parameter of the request (named \"geometryProperty\") may be used to indicate the name of the GeoProperty to be selected.  If this parameter is not present, then the default name of \"location\" shall be used.  In the case of GeoJSON Entity representation, this parameter indicates which GeoProperty to use for the toplevel geometry field.  (optional)
    lang = 'lang_example' # str | It is used to reduce languageMaps to a string or string array property in a single preferred language.  (optional)
    contained_by = ['contained_by_example'] # List[str] | List of entity ids which have previously been encountered whilst retrieving the  Entity Graph. Only applicable if joinLevel is present.  (optional)
    join = 'join_example' # str | The type of Linked Entity retrieval to apply (see clause 4.5.23). Allowed values: \"flat\", \"inline\", \"@none\".  (optional)
    join_level = 56 # int | Depth of Linked Entity retrieval to apply. Only applicable if join parameter is present.  (optional)
    dataset_id = ngsi_ld_client_1_8_1.QueryEntityDatasetIdParameter() # QueryEntityDatasetIdParameter | Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  (optional)
    details = True # bool | If true, the location of the EntityMap used in the operation is returned in the response. (optional)
    options = [ngsi_ld_client_1_8_1.QueryEntityOptionsParameterInner()] # List[QueryEntityOptionsParameterInner] |  (optional)
    format = ngsi_ld_client_1_8_1.FormatRepresentation() # FormatRepresentation |  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Entity retrieval by id 
        api_response = api_instance.retrieve_entity(entity_id, type=type, attrs=attrs, pick=pick, omit=omit, geometry_property=geometry_property, lang=lang, contained_by=contained_by, join=join, join_level=join_level, dataset_id=dataset_id, details=details, options=options, format=format, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationConsumptionApi->retrieve_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->retrieve_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id (URI) of the Entity to be retrieved, updated or deleted. | 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **attrs** | [**List[str]**](str.md)| List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  A synonym for a combination of the pick and q parameters. DEPRECATED. Each String is an Attribute (Property or Relationship) name.  | [optional] 
 **pick** | [**List[str]**](str.md)| Each String is an Entity member (\&quot;id\&quot;, \&quot;type\&quot;, \&quot;scope\&quot; or a projected Attribute name). When defined, every Entity within the payload body is reduced down to only contain  the listed Entity members.  | [optional] 
 **omit** | [**List[str]**](str.md)| Each String is an Entity member (\&quot;id\&quot;, \&quot;type\&quot;, \&quot;scope\&quot; or a projected Attribute name).  When defined, the listed Entity members are removed from each Entity within the payload.  | [optional] 
 **geometry_property** | **str**| 4.5.16.1 Top-level \&quot;geometry\&quot; field selection algorithm.  A parameter of the request (named \&quot;geometryProperty\&quot;) may be used to indicate the name of the GeoProperty to be selected.  If this parameter is not present, then the default name of \&quot;location\&quot; shall be used.  In the case of GeoJSON Entity representation, this parameter indicates which GeoProperty to use for the toplevel geometry field.  | [optional] 
 **lang** | **str**| It is used to reduce languageMaps to a string or string array property in a single preferred language.  | [optional] 
 **contained_by** | [**List[str]**](str.md)| List of entity ids which have previously been encountered whilst retrieving the  Entity Graph. Only applicable if joinLevel is present.  | [optional] 
 **join** | **str**| The type of Linked Entity retrieval to apply (see clause 4.5.23). Allowed values: \&quot;flat\&quot;, \&quot;inline\&quot;, \&quot;@none\&quot;.  | [optional] 
 **join_level** | **int**| Depth of Linked Entity retrieval to apply. Only applicable if join parameter is present.  | [optional] 
 **dataset_id** | [**QueryEntityDatasetIdParameter**](.md)| Specifies the datasetIds of the Attribute instances to be selected for each matched Attribute as per clause 4.5.5,  or the datasetId of the dataset to be deleted.  | [optional] 
 **details** | **bool**| If true, the location of the EntityMap used in the operation is returned in the response. | [optional] 
 **options** | [**List[QueryEntityOptionsParameterInner]**](QueryEntityOptionsParameterInner.md)|  | [optional] 
 **format** | [**FormatRepresentation**](.md)|  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**QueryEntity200ResponseInner**](QueryEntity200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld, application/geo+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the target entity containing the selected Attributes, unless the Accept Header indicates that the Entity is to be rendered as GeoJSON.  If the Accept Header indicates that the Entity is to be rendered as GeoJSON, a GeoJSON Feature is returned.  If an EntityMap has been requested, the HTTP response shall include an \&quot;NGSILDEntityMap\&quot; HTTP header that  contains the resource URI of the EntityMap resource used in the operation.  |  * NGSILD-EntityMap -  <br>  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**501** | It is used by Registered Context Sources to indicate that the data format  of the request is unsupported see clause 6.3.7.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity_type_info**
> EntityTypeInfo retrieve_entity_type_info(type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Details about available entity type 

5.7.7 Retrieve Available Entity Type information.  This operation allows retrieving detailed entity type information about a specified NGSI-LD entity type for which entity instances exist within the NGSI-LD system. The detailed representation includes the type name (as short name if available in the provided @context), the count of available entity instances and details about attributes that existing instances of this entity type have, including their name (as short name if available in the provided @context) and a list of types the attribute can have (e.g. Property, Relationship or GeoProperty). 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.entity_type_info import EntityTypeInfo
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    type = 'type_example' # str | Name of the entity type for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided. 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Details about available entity type 
        api_response = api_instance.retrieve_entity_type_info(type, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationConsumptionApi->retrieve_entity_type_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->retrieve_entity_type_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Name of the entity type for which detailed information is to be retrieved. The Fully Qualified Name (FQN) as well as the short name can be used, given that the latter is part of the JSON-LD @context provided.  | 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**EntityTypeInfo**](EntityTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the detailed information about the available entity type.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity_types**
> RetrieveEntityTypes200Response retrieve_entity_types(details=details, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)

Retrieve available entity types  

5.7.5 Retrieve Available Entity Types.  This operation allows retrieving a list of NGSI-LD entity types for which entity instances exist within the NGSI-LD system.  5.7.6  Retrieve Details of Available Entity Types.  This operation allows retrieving a list with a detailed representation of NGSI-LD entity types for which entity instances exist within the NGSI-LD system. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.retrieve_entity_types200_response import RetrieveEntityTypes200Response
from ngsi_ld_client_1_8_1.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client_1_8_1.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)


# Enter a context with an instance of the API client
with ngsi_ld_client_1_8_1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client_1_8_1.ContextInformationConsumptionApi(api_client)
    details = True # bool | If true, then detailed entity type information represented as an array with elements of the Entity Type data structure (clause 5.2.25) is to be returned.  (optional)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    via = 'via_example' # str | 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \"hostAlias\"  (see clause 5.2.40) as the pseudonym.  (optional)

    try:
        # Retrieve available entity types  
        api_response = api_instance.retrieve_entity_types(details=details, local=local, link=link, ngsild_tenant=ngsild_tenant, via=via)
        print("The response of ContextInformationConsumptionApi->retrieve_entity_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextInformationConsumptionApi->retrieve_entity_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **details** | **bool**| If true, then detailed entity type information represented as an array with elements of the Entity Type data structure (clause 5.2.25) is to be returned.  | [optional] 
 **local** | **bool**| 6.3.18 Limiting Distributed Operations. If local&#x3D;true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  The parameter described in this clause limits the execution of an operation to a local Context Source  or Context Broker (clause 5.5.13).  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 
 **via** | **str**| 6.3.18 Limiting Distributed Operations  If present, the listing of previously encountered Context Sources supplied is used when determining  matching registrations. HTTP Via Header (IETF RFC 7230).  Any Context Broker implementation passing a distributed operation request onward to another Context Source  shall send an additional field value on the Via header field using its own unique Context Source \&quot;hostAlias\&quot;  (see clause 5.2.40) as the pseudonym.  | [optional] 

### Return type

[**RetrieveEntityTypes200Response**](RetrieveEntityTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the EntityTypeList (clause 5.2.24) is to be returned, unless details&#x3D;true is specified.  If details&#x3D;true is specified, a response body containing a JSON-LD array with elements of the EntityType data structure (clause 5.2.25) is to be returned.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

