from requests.adapters import HTTPAdapter
from urllib3.util import Retry

import logging
import requests

logger = logging.getLogger(__name__)

CORE_CONTEXT = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"


# Class built based on reference docs for the
# Scorpio Broker FIWARE NGSI-LD API Walktrough.
# See https://scorpio.readthedocs.io/en/latest/API_walkthrough.html

class NGSILDHealthInfoAPI():
    def __init__(
            self, url: str = "http://scorpio:9090",
            headers: dict = {},
            disable_ssl: bool = False,
            debug: bool = False,
            context: str = CORE_CONTEXT):

        self.headers = headers
        self.url = url
        self.ssl_verification = not disable_ssl
        # Retry strategy
        retry_strategy = Retry(
            total=5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "PUT", "POST", "OPTIONS"],
            backoff_factor=5
        )
        self._session = requests.Session()
        self._session.mount(self.url, HTTPAdapter(max_retries=retry_strategy))
        self.context = context
        self.headers['Link'] = ('<{0}>;'
                                ' rel="http://www.w3.org/ns/json-ld#context";'
                                ' type="application/ld+json'
                                ).format(self.context)
        self.debug = debug
        if self.debug:
            import logging
            # These two lines enable debugging at httplib level
            # (requests->urllib3->http.client)
            # You will see the REQUEST, including HEADERS and DATA,
            # and RESPONSE with HEADERS but without DATA.
            # The only thing missing will be
            # the response.body which is not logged.
            try:
                import http.client as http_client
            except ImportError:
                # Python 2
                import httplib as http_client
            http_client.HTTPConnection.debuglevel = 1

            # You must initialize logging,
            # otherwise you'll not see debug output.
            logging.basicConfig()
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.propagate = True


    def checkScorpioHealth(self):
        """
        Checks NGSI-LD Scorpio broker status is up.
        """
        response = self._session.get(
            "{0}/q/health/".format(self.url),
            verify=self.ssl_verification,
            headers=self.headers
        )
        return response
    
    def checkScorpioInfo(self):
        """
        Checks NGSI-LD Scorpio broker build info.
        """
        response = self._session.get(
            "{0}/q/info/".format(self.url),
            verify=self.ssl_verification,
            headers=self.headers
        )
        return response