# -*- coding: utf-8 -*-
import logging
import time
import os

from testconfig import config
from unittest import TestCase
import requests
import json


default_headers = {'Content-Type': 'application/json; charset=utf-8', 'Connection': 'keep-alive'}

class BaseTest(TestCase):


    logger = logging.getLogger('api_testsuite')
    if not os.path.exists('logs/api_testsuite.log'):os.mkdir('logs')
    handler = logging.FileHandler('logs/api_testsuite.log')
    formatter = logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                                  '%d/%m/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)
        self.test_config = {}
        for section in config.keys():
            self.test_config[section]={}
            for key in config[section].keys():
                self.test_config[section][key]=config[section][key]
        

    def get_time_stamp(self):
        return time.time()
    

    def setUp(self):
        self._testID = self._testMethodName
        self._startTime = self.get_time_stamp()
        self._logger = logging.LoggerAdapter(logging.getLogger('api_testsuite'),
                                             {'testid': self.shortDescription().split(':')[0] or self._testID})
        self.lg('Testcase %s Started at %s' % (self._testID, self._startTime))
        self.lg('Config is %s STARTED' % self.test_config)
        self.session = requests.Session()


    def tearDown(self):
        """
        Environment cleanup and logs collection.
        """
        self.session.close()
        if hasattr(self, '_startTime'):
            executionTime = self.get_time_stamp() - self._startTime
        self.lg('Testcase %s Execution Time is %s sec.' % (self._testID, executionTime))


    def lg(self, msg):
        self._logger.info(msg)
   
        
    def get_request_response(self, url, timeout=30, headers=None):
        if not headers: headers = default_headers
        self.lg('GET %s' % url)
        return self.session.get(url, headers=headers, timeout=timeout, allow_redirects=True)     
    
    
    def create_file(self, file_name, file_path, content):
        self.lg('Create file [%s] in path [%s] with content [%s]' % (file_name, file_path, content))
        file_obj = open(file_path+file_name, "w")
        file_obj.write(content)
        file_obj.close()
    
    
    def check_file_exists(self, file_name, file_path):
        output = os.path.exists(file_path+file_name)
        self.lg('Check if file exists [%s] in path [%s]: [%s]' % (file_name, file_path, output))
        return output
    
    
    def time_sleep(self, interval):
        self.lg('Sleep [%s] seconds' % (interval))
        time.sleep(interval)
    
    


