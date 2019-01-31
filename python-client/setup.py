# coding: utf-8

"""
    Doi Server API

    Doi Server API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Doi Server API",
    author_email="",
    url="",
    keywords=["Swagger", "Doi Server API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    data_files=['swagger_client/clientApi.cfg'],
    long_description="""\
    Doi Server API  # noqa: E501
    """
)
