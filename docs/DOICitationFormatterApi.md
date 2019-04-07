# swagger_client.DOICitationFormatterApi

All URIs are relative to *https://localhost:8183*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_citation**](DOICitationFormatterApi.md#get_citation) | **GET** /citation/format | 
[**get_citations_language**](DOICitationFormatterApi.md#get_citations_language) | **GET** /citation/language | 
[**get_citations_style**](DOICitationFormatterApi.md#get_citations_style) | **GET** /citation/style | 


# **get_citation**
> str get_citation(doi, style, lang)



Returns the formatted citation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DOICitationFormatterApi()
doi = 'doi_example' # str | DOI project name
style = 'style_example' # str | style
lang = 'lang_example' # str | langage

try:
    api_response = api_instance.get_citation(doi, style, lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DOICitationFormatterApi->get_citation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doi** | **str**| DOI project name | 
 **style** | **str**| style | 
 **lang** | **str**| langage | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_citations_language**
> list[str] get_citations_language()



Renvoie la liste des langages disponibles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DOICitationFormatterApi()

try:
    api_response = api_instance.get_citations_language()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DOICitationFormatterApi->get_citations_language: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_citations_style**
> list[str] get_citations_style()



Renvoie la liste des styles disponibles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DOICitationFormatterApi()

try:
    api_response = api_instance.get_citations_style()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DOICitationFormatterApi->get_citations_style: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

