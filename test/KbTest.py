from unittest import TestCase
import imp
import os
import HttpServer
import json
from TestQueryResponses import *

os.environ['KB_READONLY_USER'] = 'myuser'
os.environ['KB_READONLY_PASSWORD'] = 'mypassword'
os.environ['KB_LAB_URL'] = 'http://localhost:8889'
os.environ['KB_PRODUCTION_URL'] = 'http://productionurl'

kb_class = imp.load_source('kb', '../src/kb')


class TestKB(TestCase):
    server = None

    def setUp(self):
        self.kb = kb_class.KB()

        self.kb.set_domain("lab")
        self.set_test_environment("foo")

    @classmethod
    def setUpClass(cls):
        cls.server = HttpServer.HttpServer(8889)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test_getHost(self):
        self.assertEquals(self.kb.get_host(), 'http://localhost:8889')

    def test_getHostProduction(self):
        self.kb.set_domain("production")

        self.assertEquals(self.kb.get_host(), 'http://productionurl')

    def test_getDomain(self):
        self.assertEquals(self.kb.get_domain(), "lab")

    def test_setDomain(self):
        self.kb.set_domain("production")

        self.assertEquals(self.kb.get_domain(), "production")

    def test_list_environments(self):
        self.server.set_data(json.dumps(environments))

        response = list(self.kb.list_environments("", ""))

        self.assertListEqual(response, ['foo', 'bar', 'fi'])

    def test_list_environment_server_errors(self):
        self.server.set_error(500)

        response = self.kb.list_environments("", "")

        self.assertListEqual(response, [])

    def test_list_services(self):
        self.server.set_data(json.dumps(services))

        response = list(self.kb.list_services('', ''))

        # 2 of the 3 services are in the current environment, the other is excluded
        self.assertListEqual(response, ['Foo2', 'fee'])

    def test_list_services_server_errors(self):
        self.server.set_error(500)

        response = self.kb.list_services('', '')

        self.assertListEqual(response, [])

    def test_list_properties(self):
        self.server.set_data(json.dumps(properties))

        response = list(self.kb.list_properties('', Namespace(service='foo')))

        self.assertListEqual(sorted(response), sorted(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

    def test_list_properties_server_errors(self):
        self.server.set_error(500)

        response = self.kb.list_properties('', Namespace(service='foo'))

        self.assertListEqual(response, [])

    def test_list_domains(self):

        response = list(self.kb.list_domains('', ''))

        self.assertListEqual(response, ['lab', 'production'])

    def test_list_clouds(self):
        self.server.set_data(json.dumps(clouds))

        response = list(self.kb.list_clouds('', ''))

        self.assertListEqual(response, ['cloud1', 'cloud2', 'cloud3'])

    def test_list_clouds_server_errors(self):
        self.server.set_error(500)

        response = self.kb.list_clouds('', '')

        self.assertListEqual(response, [])

    def test_list_sizes(self):
        self.server.set_data(json.dumps(sizes))

        response = list(self.kb.list_sizes('', Namespace(location='aws')))

        self.assertListEqual(response, ['m1.small', 'm1.medium', 'm1.large', 'c1.xlarge'])

    def test_list_sizes_server_errors(self):
        self.server.set_error(500)

        response = self.kb.list_sizes('', Namespace(location='aws'))

        self.assertListEqual(response, [])

    def test_list_images(self):
        self.server.set_data(json.dumps(images))

        response = list(self.kb.list_images('', Namespace(location='aws')))

        self.assertListEqual(response, ['centos6.6', 'centos6.6HVM', 'centos6.5L'])

    def test_list_images_server_errors(self):
        self.server.set_error(500)

        response = self.kb.list_images('', Namespace(location='aws'))

        self.assertListEqual(response, [])

    # todo list_filters
    # todo list_variables

    # ------------------------------------------------------------------------
    # Test utility methods
    # ------------------------------------------------------------------------
    def set_test_environment(self, environment):
        environment = [{
            "environment_name": "lab",
            "name": environment,
            "type": "environment",
            "svc_id": "52",
            "note": "rcollette ops bootcamp"
        }]
        self.server.set_data(json.dumps(environment))
        self.kb.set_environment("foo")

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
