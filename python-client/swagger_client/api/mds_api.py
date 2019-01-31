# coding: utf-8

"""
    Doi Server API

    Doi Server API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MdsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_doi_project(self, doi_name, **kwargs):  # noqa: E501
        """cancel_doi_project  # noqa: E501

        This request marks a dataset as 'inactive'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_doi_project(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: doi project name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cancel_doi_project_with_http_info(doi_name, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_doi_project_with_http_info(doi_name, **kwargs)  # noqa: E501
            return data

    def cancel_doi_project_with_http_info(self, doi_name, **kwargs):  # noqa: E501
        """cancel_doi_project  # noqa: E501

        This request marks a dataset as 'inactive'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_doi_project_with_http_info(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: doi project name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doi_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_doi_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doi_name' is set
        if ('doi_name' not in params or
                params['doi_name'] is None):
            raise ValueError("Missing the required parameter `doi_name` when calling `cancel_doi_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doi_name' in params:
            path_params['doi_name'] = params['doi_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/metadata/{doi_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_doi_metadata(self, doi_name, **kwargs):  # noqa: E501
        """get_all_doi_metadata  # noqa: E501

        Renvoie les metadata d'un doi  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_doi_metadata(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_doi_metadata_with_http_info(doi_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_doi_metadata_with_http_info(doi_name, **kwargs)  # noqa: E501
            return data

    def get_all_doi_metadata_with_http_info(self, doi_name, **kwargs):  # noqa: E501
        """get_all_doi_metadata  # noqa: E501

        Renvoie les metadata d'un doi  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_doi_metadata_with_http_info(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doi_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_doi_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doi_name' is set
        if ('doi_name' not in params or
                params['doi_name'] is None):
            raise ValueError("Missing the required parameter `doi_name` when calling `get_all_doi_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doi_name' in params:
            path_params['doi_name'] = params['doi_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/metadata/{doi_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_dois(self, **kwargs):  # noqa: E501
        """get_all_dois  # noqa: E501

        Get all the dois  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dois(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_dois_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_dois_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_dois_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_dois  # noqa: E501

        Get all the dois  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_dois_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_dois" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/uri-list'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/dois', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_doi_media(self, doi_name, **kwargs):  # noqa: E501
        """get_doi_media  # noqa: E501

        Retuen a list of pairs of media type and URLs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_doi_media(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: DOI project name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_doi_media_with_http_info(doi_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_doi_media_with_http_info(doi_name, **kwargs)  # noqa: E501
            return data

    def get_doi_media_with_http_info(self, doi_name, **kwargs):  # noqa: E501
        """get_doi_media  # noqa: E501

        Retuen a list of pairs of media type and URLs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_doi_media_with_http_info(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: DOI project name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doi_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_doi_media" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doi_name' is set
        if ('doi_name' not in params or
                params['doi_name'] is None):
            raise ValueError("Missing the required parameter `doi_name` when calling `get_doi_media`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doi_name' in params:
            path_params['doi_name'] = params['doi_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/uri-list'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/media/{doi_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_landing_page_url(self, doi_name, **kwargs):  # noqa: E501
        """get_landing_page_url  # noqa: E501

        Renvoie l'url de la landing page du doi  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_landing_page_url(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: doi project name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_landing_page_url_with_http_info(doi_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_landing_page_url_with_http_info(doi_name, **kwargs)  # noqa: E501
            return data

    def get_landing_page_url_with_http_info(self, doi_name, **kwargs):  # noqa: E501
        """get_landing_page_url  # noqa: E501

        Renvoie l'url de la landing page du doi  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_landing_page_url_with_http_info(doi_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: doi project name (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doi_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_landing_page_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doi_name' is set
        if ('doi_name' not in params or
                params['doi_name'] is None):
            raise ValueError("Missing the required parameter `doi_name` when calling `get_landing_page_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doi_name' in params:
            path_params['doi_name'] = params['doi_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/dois/{doi_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_doi(self, url, doi, **kwargs):  # noqa: E501
        """post_doi  # noqa: E501

        Create a **new** doi project or update the landing page url if it the project already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_doi(url, doi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str url: the URL of the landing page (required)
        :param str doi: the project suffix, which is an unique identifier within the project (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_doi_with_http_info(url, doi, **kwargs)  # noqa: E501
        else:
            (data) = self.post_doi_with_http_info(url, doi, **kwargs)  # noqa: E501
            return data

    def post_doi_with_http_info(self, url, doi, **kwargs):  # noqa: E501
        """post_doi  # noqa: E501

        Create a **new** doi project or update the landing page url if it the project already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_doi_with_http_info(url, doi, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str url: the URL of the landing page (required)
        :param str doi: the project suffix, which is an unique identifier within the project (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['url', 'doi']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_doi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'url' is set
        if ('url' not in params or
                params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `post_doi`")  # noqa: E501
        # verify the required parameter 'doi' is set
        if ('doi' not in params or
                params['doi'] is None):
            raise ValueError("Missing the required parameter `doi` when calling `post_doi`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'url' in params:
            form_params.append(('url', params['url']))  # noqa: E501
        if 'doi' in params:
            form_params.append(('doi', params['doi']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/dois', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_doi_metada(self, metada, **kwargs):  # noqa: E501
        """post_doi_metada  # noqa: E501

        Create or update doi project metada  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_doi_metada(metada, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metada: metadata (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_doi_metada_with_http_info(metada, **kwargs)  # noqa: E501
        else:
            (data) = self.post_doi_metada_with_http_info(metada, **kwargs)  # noqa: E501
            return data

    def post_doi_metada_with_http_info(self, metada, **kwargs):  # noqa: E501
        """post_doi_metada  # noqa: E501

        Create or update doi project metada  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_doi_metada_with_http_info(metada, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metada: metadata (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['metada']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_doi_metada" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'metada' is set
        if ('metada' not in params or
                params['metada'] is None):
            raise ValueError("Missing the required parameter `metada` when calling `post_doi_metada`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'metada' in params:
            body_params = params['metada']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/metadata', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_media(self, doi_name, data, **kwargs):  # noqa: E501
        """post_media  # noqa: E501

        add an association media/url  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_media(doi_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: DOI project name (required)
        :param str data: an association types de media/url (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_media_with_http_info(doi_name, data, **kwargs)  # noqa: E501
        else:
            (data) = self.post_media_with_http_info(doi_name, data, **kwargs)  # noqa: E501
            return data

    def post_media_with_http_info(self, doi_name, data, **kwargs):  # noqa: E501
        """post_media  # noqa: E501

        add an association media/url  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_media_with_http_info(doi_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str doi_name: DOI project name (required)
        :param str data: an association types de media/url (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['doi_name', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_media" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'doi_name' is set
        if ('doi_name' not in params or
                params['doi_name'] is None):
            raise ValueError("Missing the required parameter `doi_name` when calling `post_media`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `post_media`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'doi_name' in params:
            path_params['doi_name'] = params['doi_name']  # noqa: E501

        query_params = []

        header_params = {}

        # Workaround to send form data when the input is in thr request body
        form_params = []
        
        if 'data' in params:
            for mediaUrl in params['data'].split("&"):
                   media_url = mediaUrl.split("=")
                   form_params.append((media_url[0], media_url[1])) 
        
        
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/mds/media/{doi_name}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
