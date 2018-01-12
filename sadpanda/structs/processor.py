'''
the processor object that handles forward encryption and reverse decryption

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
\|.   /  |  \   .|/
  \+<|   |   |>+/
      \ /|\ /
       V===V
       |   |
   ___/     \___
				 
		 sadpanda

by: alex balzer
'''
import pickle
import os
import logging
import threading

from sadpanda.icrypt.aes import iAES # TODO: remove import
from sadpanda.structs.datastore import DataStore
from sadpanda.server.distribution import DistributionManager
from sadpanda.structs.queueing import QueueingSystem
from sadpanda.structs.ledger import Ledger

logger = logging.getLogger(__name__)

class Processor(object): # Blockchain
	'''
    base processor - handles processing ledgers

	for the time being this will be the base blockchain item
	'''
	def __init__(self, start_value, key, args):
		# TODO: this is a big one as it basically will invent the market. if you use this library for that kind of thing.
		self.args = args
		self.queueing_system = QueueingSystem(args)
		self.datastore = self.initialize_blockchain()
		if len(self.datastore) == 0:
			ledger = self.create_ledger(start_value, key, args)
			self.store_ledger(ledger)
		# TODO: the processor needs to be spawned into a pseudo infintite object that accepts requests and turns them into ledgers if they fit the bill
		self.save_datastore(args.datastore)
		# - now start the server
		#self._run_server(args)
		# - now start the infinite Processor item
		#self.daemonize(args)

	def initialize_blockchain(self):
		# TODO: start the blockchain datastore check the filesystem for the blocks
		return DataStore()

	def load_blockchain(self, args):
		# load the blockchain from disk.
		# TODO: implement the blockchain load feature
		self.queueing_system.load_blockchain(args)

	def create_ledger(self, current_value, key, args):
		if self.validate(current_value):
			current_ledger = Ledger(current_value, key, args)
			return current_ledger

	def validate(self, value):
		''' validate a value before doing anything further with it. '''
		# TODO: you need to implement this method as it is a very important security measure that maintains the integrity of the system
		return True

	def add_entry(self, item):
		'''
		add a single ledger into the blockchain.
		'''
		ledger = Ledger(item, self.datastore.get_previous_item().ledger.encrypted_item, self.args)
		self.datastore.add_item(ledger)

	def store_ledger(self, ledger):
		self.datastore.add_item(ledger)

	def save_datastore(self, filename):
		# TODO: this needs a lot of work.
		#if not os.path.isdir(filename):
		#	os.mkdir("data")
		try:
			pickle.dump(self, open(filename, 'ab'))
		except:
			directory_name = filename.split('/')
			directory_name.remove('')
			logger.error("Directory '%s' does not exist! Please create this directory before you can run this application." % directory_name[:-1])

	def run_server(self, args): #, hostname='', port=80):
		'''
		Should the processor control the http server? or maybe just launch it in the background.
		'''
		# TODO: you need to spawn the httpserver with the processor object as it handles everything else. use asyncio.
		self.hostname = args.hostname
		self.port = args.port
		self.server_threads = args.server_threads

	def _run_server(self, args):
		self.server_threads = []
		self.server_threads = args.server_threads
		for i in range(self.server_threads):
			t = threading.Thread(target=self.run_server(args))
			self.server_threads.append(t)
			t.start()

	def _initialize(self, args):
		pass

	def send_key(self, key):
		# TODO: send the key off into space. wherever your key ledger datastore is at.....
		pass

	def delete_key(self, filename):
		pass
		r, r1 = os.popen2("rm %s"%filename)
		logger.info("Doing some dd's....")

	def daemonize(self, key, args):
		# TODO: implement the functionality of the Processor object. how it handles requests received etc...
		logger.info("Starting the main sadpanda process.....")
		self.send_key(key)
		# NOTE: you should depreciate this method as it implies having a key on disk.
		self.delete_key(args.keyfile)
		logger.info("Initializing the main daemon......")
		self._initialize(args)
