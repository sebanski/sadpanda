'''
this is the data store implementation

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
|||   /  |  \   |||
  \+<|   |   |>+/
      \ /|\ /
       V===V
       |   |
   ___/     \___
				 
		 sadpanda

by: alex balzer
'''
import logging

logger = logging.getLogger(__name__)

class DataStore(object):
	'''
	the base data structure for the entire application data store. might want to look at a full library but for the time being a basic list and pickle will do just fine.
	'''
	def __init__(self):
		# NOTE: this is a super naive datastore, but I want something to start with thats why I am using a list
		self.datastore = []

	def add_item(self, item):
		# you should do validation and make sure it was passed throught the processor as an encrypted ledger.
		self.datastore.append(item)

	def get_previous_item(self):
		return self.datastore[len(self.datastore)-1]
		# return self.datastore[:-1]

	def check_item(self, item):
		'''
		validate that a item is correctly stored and encrypted.
		'''
		# TODO: implement this checker method. this actually might need to go in the Processor item.
		pass
