'''
testing for sadpanda.structs.processor.py
'''
import unittest

from sadpanda.structs.processor import Processor

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

class ProcessorTest(unittest.TestCase):
    def setUp(self):
        self.args = setup_args()
        self.processor = Processor()

    def tearDown(self):
    	pass

    #def test_empty_datastore(self):
    #	self.assertEqual(self.datastore.datastore, [])
