import responses
import json

from .helpers import mock_file, ClientTestCase


class TestCancelRequestOrder(ClientTestCase):

    def setUp(self):
        super(TestCancelRequestOrder, self).setUp()

    @responses.activate
    def test_TestCancelRequestOrder(self):
        result = mock_file('cancel_request_order_response')
        url = "https://stg-api.sandbox.paypay.ne.jp/v1/requestOrder/fakeMerchantId"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True, )
        self.assertEqual(
            self.client.Pending.refund_details('fakeMerchantId'), result)