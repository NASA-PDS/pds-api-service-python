# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.products import Products  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBundlesProductsController(BaseTestCase):
    """BundlesProductsController integration test stubs"""

    def test_products_of_a_bundle(self):
        """Test case for products_of_a_bundle

        get products belonging to a given bundle
        """
        query_string = [('start', 0),
                        ('limit', 100),
                        ('fields', 'fields_example'),
                        ('sort', 'sort_example'),
                        ('only_summary', false)]
        response = self.client.open(
            '/PDS_APIs/pds_federated_api/0.1.0/bundles/{lidvid}/products'.format(lidvid='lidvid_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
