# swagger_client.MdsApi

All URIs are relative to *http://localhost:8182*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_doi_project**](MdsApi.md#cancel_doi_project) | **DELETE** /mds/metadata/{doi_name} | 
[**get_all_doi_metadata**](MdsApi.md#get_all_doi_metadata) | **GET** /mds/metadata/{doi_name} | 
[**get_all_dois**](MdsApi.md#get_all_dois) | **GET** /mds/dois | 
[**get_doi_media**](MdsApi.md#get_doi_media) | **GET** /mds/media/{doi_name} | 
[**get_landing_page_url**](MdsApi.md#get_landing_page_url) | **GET** /mds/dois/{doi_name} | 
[**post_doi**](MdsApi.md#post_doi) | **POST** /mds/dois | 
[**post_doi_metada**](MdsApi.md#post_doi_metada) | **POST** /mds/metadata | 
[**post_media**](MdsApi.md#post_media) | **POST** /mds/media/{doi_name} | 


# **cancel_doi_project**
> str cancel_doi_project(doi_name)



This request marks a dataset as 'inactive'

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
doi_name = 'doi_name_example' # str | doi project name

try:
    api_response = api_instance.cancel_doi_project(doi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->cancel_doi_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi_name** | **str**| doi project name | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_doi_metadata**
> str get_all_doi_metadata(doi_name)



Renvoie les metadata d'un doi

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
doi_name = 'doi_name_example' # str | 

try:
    api_response = api_instance.get_all_doi_metadata(doi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->get_all_doi_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi_name** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_dois**
> str get_all_dois()



Get all the dois

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_dois()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->get_all_dois: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/uri-list

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_doi_media**
> str get_doi_media(doi_name)



Retuen a list of pairs of media type and URLs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
doi_name = 'doi_name_example' # str | DOI project name

try:
    api_response = api_instance.get_doi_media(doi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->get_doi_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi_name** | **str**| DOI project name | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/uri-list

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_landing_page_url**
> str get_landing_page_url(doi_name)



Renvoie l'url de la landing page du doi

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
doi_name = 'doi_name_example' # str | doi project name

try:
    api_response = api_instance.get_landing_page_url(doi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->get_landing_page_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi_name** | **str**| doi project name | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doi**
> str post_doi(url, doi)



Create a **new** doi project or update the landing page url if it the project already exists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
url = 'url_example' # str | the URL of the landing page
doi = 'doi_example' # str | the project suffix, which is an unique identifier within the project

try:
    api_response = api_instance.post_doi(url, doi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->post_doi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| the URL of the landing page | 
 **doi** | **str**| the project suffix, which is an unique identifier within the project | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_doi_metada**
> str post_doi_metada(metada)



Create or update doi project metada

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
metada = 'metada_example' # str | metadata

try:
    api_response = api_instance.post_doi_metada(metada)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->post_doi_metada: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metada** | **str**| metadata | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_media**
> str post_media(doi_name, data)



add an association media/url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MdsApi(swagger_client.ApiClient(configuration))
doi_name = 'doi_name_example' # str | DOI project name
data = 'data_example' # str | an association types de media/url

try:
    api_response = api_instance.post_media(doi_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MdsApi->post_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi_name** | **str**| DOI project name | 
 **data** | **str**| an association types de media/url | 

### Return type

**str**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

