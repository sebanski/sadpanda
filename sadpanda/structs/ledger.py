'''
base ledger object

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

from icrypt.aes import iAES

logger = logging.getLogger(__name__)

# TODO: you need to add a ledger counter to handle keeping track of all ledgers that enter the system.
class LedgerCounter(object):
	'''
	keeps track of all ledgers that enter the system.
	'''
	def __init__(self, start_value=0):
		self.current_value = start_value

	def add_ledger(self):
		self.current_value += 1

	def remove_ledger(self):
		self.current_value -= 1

class Ledger(object):
	'''
	a ledger is a single item in the datastore
	'''
	counter = LedgerCounter() # TODO: there needs to be a metadatavalue passed in for the start value.
	def __init__(self, value, key, args, salt=None):
		if not self.validate_value(value):
			logger.error("Invorrect value type for ledger check the value again...")
		else:
			if salt == None:
				if args.encryption_method.lower() == "aes":
					self.ledger = iAES(value, key)
					# TODO: this might break...
					del value
				# TODO: implement the other encryption methods...
				else:
					self.ledger = iAES(value, key)
					del value
			elif salt != None:
				if args.encryption_method.lower() == "aes":
					self.ledger = iAES(value, key, salt)
					del value

	def validate_value(self, value):
		# TODO: implement this feature.....
		return True


