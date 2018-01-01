'''
the queuing system for disk writes and atomicity.

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
'''
import logging

from structs.datastore import DataStore
from structs.ledger import Ledger
from structs.ifiles.inode import iNode

logger = logging.getLogger(__name__)

# TODO: implement this class.
class QueueingSystem(object):
	'''
	handles queueing writes between the world to guareentee atomicity.....
	'''
	inode = iNode('')
	# TODO: add inode initiation here, you only need 1 iNode per system.
	def __init__(self, args, queue_data=[]):
		self.args = args
		self.lock = False
		self.queue_data = []
		if len(queue_data) > 0:
			for data in queue_data:
				self.queue_data.append(data)

	def lock_writes(self):
		# all iNode writes need permission from QueueingSystem before they can write
		self.lock = True

	def unlock_writes(self):
		self.lock = False
		# NOTE: basically drain the queues contents, until lock takes place again...
		self.drain_queue()

	def drain_queue(self):
		for data in self.queue_data:
			if not self.lock:
				# TODO: handle a inode write here
				inode.data = data
				inode.data_write(self.args)
				pass
			elif self.lock:
				# NOTE: break since you know there is a lock. when the lock is unlocked it will start the drain again.
				break

	def add_queue_data(self, data):
		if isinstance(data, list):
			for i in data:
				if isinstance(i, Ledger):
					self.queue_data.append(i)
				else:
					# TODO: raise a big red alarm as there is some corrupt data in transit.
					logger.error("Incorrect data type in ledger type=<%s>. this is a huge problem. the system needs to rebalance itself and run security tests now." % str(i))
		# TODO: make sure that the ledger is the exact item you want to place within the queue.
		elif isinstance(data, Ledger):
			self.queue_data.append(data)

	def load_blockchain(self, args):
		# TODO: initiate the from disk to memory read.
		datastore = DataStore()
		inodes = inode.load_files()
		pass 
