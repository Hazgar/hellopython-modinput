import os
import unittest
from splunklib.modularinput import *

THIS_PATH = os.path.dirname(os.path.realpath(__file__))

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.setup = 1

    def test_sample(self):
        found = ValidationDefinition.parse("%s/data/validation.xml" % THIS_PATH);
        expected = {
            'metadata': {'server_host': 'tiny', 'checkpoint_dir': '/opt/splunk/var/lib/splunk/modinputs', 'name': 'aaa', 'session_key': '123102983109283019283', 'server_uri': 'https://127.0.0.1:8089'},
            'parameters': {'magic': '42', 'whoareyou': 'someone', 'whatisyourfavoritecolor': 'green', 'index': 'default', 'whereareyou': 'somewhere', 'howareyou': 'good', 'disabled': '0'}
        }
        self.assertEqual(expected["metadata"]["server_host"], found.metadata["server_host"])
        self.assertEqual(expected["metadata"]["server_uri"], found.metadata["server_uri"])
        self.assertEqual(expected["metadata"]["checkpoint_dir"], found.metadata["checkpoint_dir"])
        self.assertEqual(expected["metadata"]["session_key"], found.metadata["session_key"])
        self.assertEqual(expected["metadata"]["name"], found.metadata["name"])

        self.assertEqual(found.parameters["whoareyou"], expected["parameters"]["whoareyou"]);
        self.assertEqual(found.parameters["whereareyou"], expected["parameters"]["whereareyou"]);
        self.assertEqual(found.parameters["howareyou"], expected["parameters"]["howareyou"]);
        self.assertEqual(found.parameters["whatisyourfavoritecolor"], expected["parameters"]["whatisyourfavoritecolor"]);
        self.assertEqual(found.parameters["magic"], expected["parameters"]["magic"]);
        self.assertEqual(found.parameters["disabled"], expected["parameters"]["disabled"]);
        self.assertEqual(found.parameters["index"], expected["parameters"]["index"]);

if __name__ == '__main__':
    unittest.main()
