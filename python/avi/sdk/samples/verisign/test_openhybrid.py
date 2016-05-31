'''
Created on May 31, 2016

@author: grastogi
'''
import unittest
from avi.sdk.samples.verisign.openhybrid import OpenHybrid


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def testGetOpenHybridData(self):
        verisign_settings = {'url': 'http://versign.com',
                             'source_id': 'avi_controller'}
        ohs = OpenHybrid(verisign_settings)
        dos_event = {'src_ips': ['10.42.42.1', '10.42.42.2'],
                     'type': 'SYN_FLOOD'}
        obj_id = 'vs-1'
        obj_name = 'test-vs'
        vs_info = {
            'app_profile_type': 'APPLICATION_PROFILE_TYPE_HTTP',
            'config': {'services': [{'port': 80}],
                       'address': '10.10.10.42'},
        }
        data = ohs.getOpenHybridData(
            ts='xxxx', obj_id=obj_id, obj_name=obj_name,
            dos_event=dos_event, vs_info=vs_info)
        print data
        assert data['alert_type'] == 'SYN_FLOOD'
        assert data['destination'] == '10.10.10.42'
        assert data['destination_port'] == 80
        assert len(data['source_ips'].split(',')) == len(dos_event['src_ips'])



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
