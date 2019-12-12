# Public Domain (-) 2010-2011 The Tavutil Authors.
# See the Tavutil UNLICENSE file for details.

from __future__ import absolute_import
from tavutil.paypalx import AdaptivePayment, PayRequest
from config import (
    PPX_API_USERNAME, PPX_API_PASSWORD, 
    PPX_API_SIGNATURE, PPX_APP_ID
)

api_credentials = {'api_username': PPX_API_USERNAME,
                    'api_password': PPX_API_PASSWORD,
                    'api_signature': PPX_API_SIGNATURE,
                    'app_id': PPX_APP_ID}
adaptpay = AdaptivePayment(**api_credentials)
pay_request_kwargs = {
            'receiver_email': 'mamadi_1262634965_per@gmail.com',
            'receiver_amount': 20.00, 'currency_code': 'GBP',
            'cancel_url': 'http://www.ebay.com',
            'return_url': 'http://www.sandbox.paypal.com'
}
payreq = PayRequest(**pay_request_kwargs)
payreqmsg = payreq.get_message()
#pp_response = adaptpay.call("PAY", payreqmsg)

