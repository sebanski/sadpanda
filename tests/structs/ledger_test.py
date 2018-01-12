'''
testing for sadpanda.structs.datastore.py
'''
import unittest
import argparse

from sadpanda.structs.ledger import Ledger, LedgerCounter
from sadpanda.icrypt.aes import iAES

# TODO: you need to create a factory for the config values.
# XXX: this is a hack that should be avoided, but for the time being I want to see if the testing works. BAD
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

class LedgerTest(unittest.TestCase):
	def setUp(self):
		self.key = "ABCDEFGHIJKLMNOPABCDEFGHIJKLMNOP"
		self.salt = "AAAAAAAAAAAAAAAA"
		# TODO: the below args need to come from a factory class.
		self.args = setup_args()
		self.value = "A testable value for the validation method."
		self.ledger = Ledger(self.value, self.key, self.args)
		self.salted_ledger = Ledger(self.value, self.key, self.args, self.salt)

	def tearDown(self):
		pass

	def test_ledger_create(self):
		test_ledger = Ledger(self.value, self.key, self.args) 
		# TODO: you need to do a test for the `item` by taking the encrypted item and decrypting it.
		#self.assertEqual(self.ledger.ledger.item , test_ledger.ledger.item)
		#self.assertEqual(unencrypt(self.ledger.ledger.encrypted_item, self.key) , self.value)
		self.assertEqual(self.ledger.ledger.key, test_ledger.ledger.key)
		self.assertEqual(self.ledger.ledger.salt, test_ledger.ledger.salt)

	def test_salted_ledger_create(self):
		test_ledger = Ledger(self.value, self.key, self.args, salt=self.salt)
		#self.assertEqual(self.ledger.ledger.item , test_ledger.ledger.item)
		self.assertEqual(self.ledger.ledger.key , test_ledger.ledger.key)
		self.assertEqual(self.ledger.ledger.salt , test_ledger.ledger.salt)

	def test_validate_value(self):
		self.assertEqual(self.ledger.validate_value(self.value), True)
