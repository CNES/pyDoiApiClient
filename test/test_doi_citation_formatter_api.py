# coding: utf-8

"""
    Doi Server API

    A Digital Object Identifier (DOI) is an alphanumeric string assigned to uniquely identify an object. It is tied to a metadata description of the object as well as to a digital location, such as a URL, where all the details about the object are accessible. This documentation provides an API to query the DOI-server.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: jean-christophe.malapert@cnes.fr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.doi_citation_formatter_api import DOICitationFormatterApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDOICitationFormatterApi(unittest.TestCase):
    """DOICitationFormatterApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.doi_citation_formatter_api.DOICitationFormatterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_citation(self):
        """Test case for get_citation

        """
        pass

    def test_get_citations_language(self):
        """Test case for get_citations_language

        """
        pass

    def test_get_citations_style(self):
        """Test case for get_citations_style

        """
        pass


if __name__ == '__main__':
    unittest.main()
