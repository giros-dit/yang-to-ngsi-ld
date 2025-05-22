# ngsi_ld_client_1_8_1.ContextSourceDiscoveryApi

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_csr**](ContextSourceDiscoveryApi.md#query_csr) | **GET** /csourceRegistrations | Discover Csource registrations 
[**retrieve_csr**](ContextSourceDiscoveryApi.md#retrieve_csr) | **GET** /csourceRegistrations/{registrationId} | Csource registration retrieval by id 


# **query_csr**
> List[QueryCSR200ResponseInner] query_csr(id=id, type=type, id_pattern=id_pattern, attrs=attrs, q=q, csf=csf, geometry=geometry, georel=georel, coordinates=coordinates, geoproperty=geoproperty, timeproperty=timeproperty, timerel=timerel, time_at=time_at, end_time_at=end_time_at, geometry_property=geometry_property, lang=lang, scope_q=scope_q, options=options, limit=limit, count=count, link=link, ngsild_tenant=ngsild_tenant)

Discover Csource registrations 

5.10.2 Query Context Source Registrations.  This operation allows discovering context source registrations from an NGSI-LD system. The behaviour of the discovery of context source registrations differs significantly from the querying of entities as described in clause 5.7.2. The approach is that the client submits a query for entities as described in clause 5.7.2, but instead of receiving the Entity information, it receives a list of Context Source Registrations describing Context Sources that possibly have some of the requested Entity information. This means that the requested Entities and Attributes are matched against the 'information' property as described in clause 5.12.  If no temporal query is present, only Context Source Registrations for Context Sources providing latest information, i.e. without specified time intervals, are considered. If a temporal query is present only Context Source Registrations with matching time intervals, i.e. observationInterval or managementInterval, are considered. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client_1_8_1.models.query_csr200_response_inner import QueryCSR200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextSourceDiscoveryApi(api_client)
    id = ['id_example'] # List[str] | List of entity ids to be retrieved. (optional)
    type = 'type_example' # str | Selection of Entity Types as per clause 4.17. \"*\" is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  (optional)
    id_pattern = 'id_pattern_example' # str | Regular expression that shall be matched by entity ids. (optional)
    attrs = ['attrs_example'] # List[str] | List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  A synonym for a combination of the pick and q parameters. DEPRECATED. Each String is an Attribute (Property or Relationship) name.  (optional)
    q = 'q_example' # str | Query as per clause 4.9.  (optional)
    csf = 'csf_example' # str | Context Source filter as per clause 4.9. (optional)
    geometry = 'geometry_example' # str | Geometry as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    georel = ngsi_ld_client_1_8_1.QueryEntityGeorelParameter() # QueryEntityGeorelParameter | Geo relationship as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    coordinates = ngsi_ld_client_1_8_1.QueryEntityCoordinatesParameter() # QueryEntityCoordinatesParameter | Coordinates serialized as a string as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  (optional)
    geoproperty = location # str | The name of the Property that contains the geospatial data that will be used to resolve the geoquery. By default, will be location (see clause 4.7). It shall be ignored unless a geoquery is present.  (optional) (default to location)
    timeproperty = observedAt # str | Allowed values: \"observedAt\", \"createdAt\", \"modifiedAt\" and \"deletedAt\". If not specified, the default is \"observedAt\". (See clause 4.8)  (optional) (default to observedAt)
    timerel = 'timerel_example' # str | Allowed values: \"before\", \"after\", \"between\"  (optional)
    time_at = '2013-10-20T19:20:30+01:00' # datetime | It shall be a DateTime. Cardinality shall be 1 if timerel is present. String representing the timeAt parameter as defined by clause 4.11.  (optional)
    end_time_at = '2013-10-20T19:20:30+01:00' # datetime | It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \"between\". String representing the endTimeAt parameter as defined by clause 4.11.  (optional)
    geometry_property = 'geometry_property_example' # str | 4.5.16.1 Top-level \"geometry\" field selection algorithm.  A parameter of the request (named \"geometryProperty\") may be used to indicate the name of the GeoProperty to be selected.  If this parameter is not present, then the default name of \"location\" shall be used.  In the case of GeoJSON Entity representation, this parameter indicates which GeoProperty to use for the toplevel geometry field.  (optional)
    lang = 'lang_example' # str | It is used to reduce languageMaps to a string or string array property in a single preferred language.  (optional)
    scope_q = 'scope_q_example' # str | Scope query (see clause 4.19).  (optional)
    options = [ngsi_ld_client_1_8_1.OptionsSysAttrs()] # List[OptionsSysAttrs] |  (optional)
    limit = 56 # int | 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  (optional)
    count = True # bool | 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \"limit\" URI parameter), the total number of matching results (e.g. number of Entities) is returned.  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Discover Csource registrations 
        api_response = api_instance.query_csr(id=id, type=type, id_pattern=id_pattern, attrs=attrs, q=q, csf=csf, geometry=geometry, georel=georel, coordinates=coordinates, geoproperty=geoproperty, timeproperty=timeproperty, timerel=timerel, time_at=time_at, end_time_at=end_time_at, geometry_property=geometry_property, lang=lang, scope_q=scope_q, options=options, limit=limit, count=count, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of ContextSourceDiscoveryApi->query_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextSourceDiscoveryApi->query_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| List of entity ids to be retrieved. | [optional] 
 **type** | **str**| Selection of Entity Types as per clause 4.17. \&quot;*\&quot; is also allowed as a value and local is  implicitly set to true and shall not be explicitly set to false.  | [optional] 
 **id_pattern** | **str**| Regular expression that shall be matched by entity ids. | [optional] 
 **attrs** | [**List[str]**](str.md)| List of Attributes to be matched by the Entity and included in the response. If the Entity does not have any of the Attributes in attrs, then a 404 Not Found shall be retrieved. If attrs is not specified, no matching is performed and all Attributes related to the Entity shall be retrieved.  A synonym for a combination of the pick and q parameters. DEPRECATED. Each String is an Attribute (Property or Relationship) name.  | [optional] 
 **q** | **str**| Query as per clause 4.9.  | [optional] 
 **csf** | **str**| Context Source filter as per clause 4.9. | [optional] 
 **geometry** | **str**| Geometry as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **georel** | [**QueryEntityGeorelParameter**](.md)| Geo relationship as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **coordinates** | [**QueryEntityCoordinatesParameter**](.md)| Coordinates serialized as a string as per clause 4.10. It is part of geoquery. It shall be one if geometry or georel are present.  | [optional] 
 **geoproperty** | **str**| The name of the Property that contains the geospatial data that will be used to resolve the geoquery. By default, will be location (see clause 4.7). It shall be ignored unless a geoquery is present.  | [optional] [default to location]
 **timeproperty** | **str**| Allowed values: \&quot;observedAt\&quot;, \&quot;createdAt\&quot;, \&quot;modifiedAt\&quot; and \&quot;deletedAt\&quot;. If not specified, the default is \&quot;observedAt\&quot;. (See clause 4.8)  | [optional] [default to observedAt]
 **timerel** | **str**| Allowed values: \&quot;before\&quot;, \&quot;after\&quot;, \&quot;between\&quot;  | [optional] 
 **time_at** | **datetime**| It shall be a DateTime. Cardinality shall be 1 if timerel is present. String representing the timeAt parameter as defined by clause 4.11.  | [optional] 
 **end_time_at** | **datetime**| It shall be a DateTime. Cardinality shall be 1 if timerel is equal to \&quot;between\&quot;. String representing the endTimeAt parameter as defined by clause 4.11.  | [optional] 
 **geometry_property** | **str**| 4.5.16.1 Top-level \&quot;geometry\&quot; field selection algorithm.  A parameter of the request (named \&quot;geometryProperty\&quot;) may be used to indicate the name of the GeoProperty to be selected.  If this parameter is not present, then the default name of \&quot;location\&quot; shall be used.  In the case of GeoJSON Entity representation, this parameter indicates which GeoProperty to use for the toplevel geometry field.  | [optional] 
 **lang** | **str**| It is used to reduce languageMaps to a string or string array property in a single preferred language.  | [optional] 
 **scope_q** | **str**| Scope query (see clause 4.19).  | [optional] 
 **options** | [**List[OptionsSysAttrs]**](OptionsSysAttrs.md)|  | [optional] 
 **limit** | **int**| 6.3.10 Pagination behaviour. It defines the limit to the number of NGSI-LD Elements that shall be retrieved at a maximum as mandated by clause 5.5.9. The value 0 is only allowed in combination with the count URI parameter.  | [optional] 
 **count** | **bool**| 6.3.13 Counting number of results. If true, then a special HTTP header (NGSILD-Results-Count) is set in the response. Regardless of how many entities are actually returned (maybe due to the \&quot;limit\&quot; URI parameter), the total number of matching results (e.g. number of Entities) is returned.  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**List[QueryCSR200ResponseInner]**](QueryCSR200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the query result as an array of context source registrations.  |  * NGSILD-Results-Count -  <br>  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_csr**
> QueryCSR200ResponseInner retrieve_csr(registration_id, options=options, link=link, ngsild_tenant=ngsild_tenant)

Csource registration retrieval by id 

5.10.1 Retrieve Context Source Registration.  This operation allows retrieving a specific context source registration from an NGSI-LD system. 

### Example


```python
import ngsi_ld_client_1_8_1
from ngsi_ld_client_1_8_1.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client_1_8_1.models.query_csr200_response_inner import QueryCSR200ResponseInner
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
    api_instance = ngsi_ld_client_1_8_1.ContextSourceDiscoveryApi(api_client)
    registration_id = 'registration_id_example' # str | Id (URI) of the context source registration.
    options = [ngsi_ld_client_1_8_1.OptionsSysAttrs()] # List[OptionsSysAttrs] |  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Csource registration retrieval by id 
        api_response = api_instance.retrieve_csr(registration_id, options=options, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of ContextSourceDiscoveryApi->retrieve_csr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextSourceDiscoveryApi->retrieve_csr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| Id (URI) of the context source registration. | 
 **options** | [**List[OptionsSysAttrs]**](OptionsSysAttrs.md)|  | [optional] 
 **link** | **str**| 6.3.5 JSON-LD @context resolution  In summary, from a developer&#39;s perspective, for POST, PATCH and PUT operations, if MIME type is \&quot;application/ld+json\&quot;, then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \&quot;application/json\&quot;, then the associated @context shall be provided only by using the JSON-LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  | [optional] 
 **ngsild_tenant** | **str**| 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  | [optional] 

### Return type

[**QueryCSR200ResponseInner**](QueryCSR200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+ld

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response body containing the JSON-LD representation of the target subscription.  |  * NGSILD-Warning -  <br>  |
**400** | It is used to indicate that the request or its content is incorrect, see clause 6.3.2. In the returned ProblemDetails structure, the \&quot;detail\&quot; attribute should convey more information about the error.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |
**404** | It is used when a client provided an entity identifier (URI) not known to the system, see clause 6.3.2.  |  * NGSILD-Tenant -  <br>  * NGSILD-Warning -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

