import time

from check_api import NGSILDHealthInfoAPI

class NGSILDHealthInfoClient(object):
    """
    Class encapsulating the main operations with NGSI-LD.
    """

    def __init__(self, url: str = "http://scorpio:9090",
                 headers: dict = {"Accept": "application/json"},
                 context: str = "http://context-catalog:8080/context.jsonld",
                 debug: bool = False):
        # Init NGSI-LD REST API Client
        self.api = NGSILDHealthInfoAPI(url, headers=headers,
                             context=context, debug=debug)

    def check_scorpio_status(self):
        """
        Infinite loop that checks every 1 second
        until Scorpio REST API becomes available.
        """
        print("Checking Scorpio REST API status ...")
        while True:
            if self.api.checkScorpioHealth().ok:
                print(
                    "Successfully connected to Scorpio REST API!")
                print(self.api.checkScorpioHealth().json())
                break
            else:
                print("Could not connect to Scorpio REST API. "
                               "Retrying in 1 second ...")
                time.sleep(1)
                continue

    def check_scorpio_info(self):
        """
        Infinite loop that checks every 1 second
        until Scorpio REST API becomes available.
        """
        print("Checking Scorpio build information ...")
        while True:
            if self.api.checkScorpioInfo().ok:
                print(
                    "Successfully connected to Scorpio REST API!")
                print(self.api.checkScorpioInfo().json())
                break
            else:
                print("Could not connect to Scorpio REST API. "
                               "Retrying in 1 second ...")
                time.sleep(1)
                continue