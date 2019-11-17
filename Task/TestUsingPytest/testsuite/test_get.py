import time
import os

import pytest
import requests
import json
import types
from testconfig import config

  
test_config = {}

def read_config():
    for section in config.keys():
        test_config[section]={}
        for key in config[section].keys():
            test_config[section][key]=config[section][key]
        


def get_request_response(url, timeout=1, headers=None):
    if not headers: headers = {'Content-Type': 'application/json; charset=utf-8', 'Connection': 'keep-alive'}
    session = requests.Session()
    response = session.get(url, headers=headers, timeout=timeout, allow_redirects=True)     
    session.close()
    return response


def create_file(file_name, file_path, content):
    file_obj = open(file_path+file_name, "w")
    file_obj.write(content)
    file_obj.close()


def check_file_exists(file_name, file_path):
    return os.path.exists(file_path+file_name)


def test_qts():
    # Setup Test
    read_config() 	
    
    # Create XML file in the QTS folder
	assert os.path.isdir(self.test_config['QTS']['folder']) is True, 'No such directory [%s]' %self.test_config['QTS']['folder']
    file_name = test_config['Program']['name'] + '.xml'
    create_file(file_name=file_name, file_path=test_config['QTS']['folder'], content=test_config['XML']['format'].replace('program_name', test_config['Program']['name']))
    
    # File should be processed within timeout
    exists = True
    time_stamp = time.time()
    while int(time.time()-time_stamp)<int(test_config['QTS']['timeout']):
        if not check_file_exists(file_name=file_name, file_path=test_config['QTS']['folder']): 
            exists = False
            break
        time.sleep(1)
        
    assert exists is False, 'QTS system file reader is timeout after [%s] seconds' % test_config['QTS']['timeout']
        
    # File should be consumed within timeout
    completed = False
    time_stamp = time.time()
    while int(time.time()-time_stamp)<int(test_config['Consumer']['timeout']):
        response = get_request_response(url=test_config['Consumer']['url'])
        assertTrue(response.ok, 'Failed to get response from QTS Consumer')
        assertEqual(type(response.json()), types.ListType, 'Failed to get expected response format from QTS Consumer')
        for item in response.json():
            if item['name'] ==  test_config['Program']['name'] and item['status'] == "completed" :
                completed = True
                break
                
        time.sleep(1)
        
    assert completed is True, 'Consumer in QTS system is timeout after [%s] seconds' % test_config['Consumer']['timeout']
    
    # The result of the process is published to Media Manager component
    response = get_request_response(url=test_config['MediaManager']['url'].replace('program_name', test_config['Program']['name']))
    assert response.status_code==200, 'Entity with name [%s] is not exists in Media Manager' % test_config['Program']['name']