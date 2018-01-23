'''
testing for sadpanda.server.server
'''
import unittest
import argparse

from sadpanda.server.server import AsyncServer

# import mocks
def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--encryption-method", default='aes', type=str)
    parser.add_argument("--data-store", default='redis', type=str)
    parser.add_argument("--keyfile", default='blockchain.evk', type=str)
    parser.add_argument("--datastore", default='data/blockchain.ev', type=str)
    parser.add_argument("--hostname", default='', type=str)
    parser.add_argument("--port", default=80, type=int)
    parser.add_argument("--server-threads", default=1, type=int)
    parser.add_argument("--config-file", default="conf/sadpanda.yml", type=str)
    parser.add_argument("--p2p-nodes", default=["localhost:9871"], type=list)
    parser.add_argument("--poppyfarm", default="/etc/sadpanda.d/poppyfarm.ve", type=str)
    # TODO: add the remaining default config variables. there are a lot...
    return parser.parse_args()

class AsyncServerTest(unittest.TestCase):
    def setUp(self):
        self.args = setup_args()

    def tearDown(self):
    	pass

    def test_server_has_started(self):
        async_server = AsyncServer(2828, self.args)
        async_server.start()
        self.assertEqual(1,1)
        async_server.stop()

    #def test_empty_datastore(self):
    #	self.assertEqual(self.datastore.datastore, [])