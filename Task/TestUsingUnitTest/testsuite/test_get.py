# -*- coding: utf-8 -*-
from testframework.base import *
import types


class TestQTS(BaseTest):
     

    def test_qts(self):
        """ TestCase-A: Test case for QTS.*
        **Test Scenario:**
        #. Create XML file in the QTS folder, should succeed
        #. File should be processed within timeout, should succeed
        #. File should be consumed within timeout, should succeed
        #. The result of the process is published to Media Manager component, should succeed
        """     
        self.lg('%s STARTED' % self._testID)
        
        #. Create XML file in the QTS folder, should succeed
        self.lg('Create XML file in the QTS folder, should succeed')
		self.assertTrue(os.path.isdir(self.test_config['QTS']['folder']), 'No such directory [%s]' %self.test_config['QTS']['folder'])
        file_name = self.test_config['Program']['name'] + '.xml'
        self.create_file(file_name=file_name, file_path=self.test_config['QTS']['folder'], content=self.test_config['XML']['format'].replace('program_name', self.test_config['Program']['name']))
        
        #. File should be processed within timeout, should succeed
        self.lg('File should be processed within timeout, should succeed')
        exists = True
        time_stamp = self.get_time_stamp()
        while int(self.get_time_stamp()-time_stamp)<int(self.test_config['QTS']['timeout']):
            if not self.check_file_exists(file_name=file_name, file_path=self.test_config['QTS']['folder']): 
                exists = False
                break
            self.time_sleep(1)
            
        self.assertFalse(exists, 'QTS system file reader is timeout after [%s] seconds' % self.test_config['QTS']['timeout'])
            
        #. File should be consumed within timeout, should succeed
        self.lg('File should be consumed within timeout, should succeed')
        self.lg('#. Test using GET %s, should succeed' %self.test_config['Consumer']['url'])
        completed = False
        time_stamp = self.get_time_stamp()
        while int(self.get_time_stamp()-time_stamp)<int(self.test_config['Consumer']['timeout']):
            response = self.get_request_response(url=self.test_config['Consumer']['url'])
            self.assertTrue(response.ok, 'Failed to get response from QTS Consumer')
            self.lg('#. Check response body, should succeed')
            self.assertEqual(type(response.json()), types.ListType, 'Failed to get expected response format from QTS Consumer')
            for item in response.json():
                if item['name'] ==  self.test_config['Program']['name'] and item['status'] == "completed" :
                    completed = True
                    break
                    
            self.time_sleep(1)
            
        self.assertTrue(completed, 'Consumer in QTS system is timeout after [%s] seconds' % self.test_config['Consumer']['timeout'])
        
        # The result of the process is published to Media Manager component, should succeed
        self.lg('The result of the process is published to Media Manager component, should succeed')
        self.lg('#. Test using GET %s, should succeed' %self.test_config['MediaManager']['url'])
        response = self.get_request_response(url=self.test_config['MediaManager']['url'].replace('program_name', self.test_config['Program']['name']))
        self.assertEqual(response.status_code, 200, 'Entity with name [%s] is not exists in Media Manager' % self.test_config['Program']['name'])
        
        self.lg('%s ENDED' % self._testID) 
