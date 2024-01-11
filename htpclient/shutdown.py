import logging

from htpclient.config import Config
from htpclient.jsonRequest import JsonRequest
from htpclient.dicts import *

from htpclient.initialize import Initialize

import subprocess


class Shutdown:
    def __init__(self):
        self.config = Config()

    def get_shutdown(self):
        query = copy_and_set_token(dict_shutdown, self.config.get_value('token'))
        req = JsonRequest(query)
        ans = req.execute()
        if ans['response'] == "shutdown":
            logging.info("shutdown command recieved")
            self.shutdown_agent()

    def shutdown_agent(self):
        os_type = Initialize().get_os()
        logging.info("starting studown process")
        # Execute a shutdown command on Windows
        if os_type == 1:
            logging.info("Detected Windows OS")
            #subprocess.call(["shutdown", "/f", "/s", "/t", "0"])
        elif os_type == 0 or os_type == 2:
            # Execute a shutdown command on Linux or macOS
            logging.info("Detected Linux or MacOS")
            #subprocess.run(["shutdown", "-h", "now"])
        else:
            logging.error("Operating System is not supported") 
