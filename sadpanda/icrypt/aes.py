'''
aes encryption

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
.|.   /  |  \   .|.
  \+<|   |   |>+/
      \ /|\ /
       V===V
      ||   ||
   __//     \\__
   ===		 ===

		 sadpanda

by: alex balzer
'''
from uuid import uuid1
from random import randint
import logging

from Crypto.Cipher import AES

from sadpanda.icrypt.base import Base

# NOTE: this is my first crack at the encryption item for a processor. 
# 1.) I am sure it is littered with bugs and vulnerabilities, especially with saving salt in memory and storing the keys in an external application

logger = logging.getLogger(__name__)

class iAES(Base):
	'''
	basic encryption object for the aes suite of encryption types
	'''
	# TODO: implement the different methods below... so you have encrypt256(), encrypt128(), decrypt64(), decrypt256(),
	def __init__(self, item, key, salt=None):
		self.item_id = str(uuid1())
		self.salt = salt
		if salt == None or not isinstance(salt, str):
			self.salt = self.generate_salt()
		# TODO: delete the below variable as it is unneccassary only the processor should handle the logic for this objects methods.
		self.encrypted_item = self.encrypt(item, key, self.salt)
		#self.salt = salt
		self.key = key
		# TODO: dont save these values but instead save a new value based on these 2 items.

	def encrypt(self, item, key, salt):
		item = self.multiple_16(item)
		icrypt_model = AES.new(self.check_key(key), AES.MODE_CBC, salt)
		encrypted_item = icrypt_model.encrypt(item)
		logger.info("Successfully encrypted item %s" % self.item_id)
		return encrypted_item

	def decrypt(self, encrypted_item, key, salt):
		icrypt_model = AES.new(self.check_key(key), AES.MODE_CBC, salt)
		decrypted_item = icrypt_model.decrypt(encrypted_item)
		logger.info("Successfully decrypted item %s" % self.item_id)
		return decrypted_item

	def multiple_16(self, item):
		if len(item) % 16 == 0:
			return item
		else:
			for i in range(10000):
				item += " " # shoule be a bit \x00
				if len(item) % 16 == 0:
					return item
			# recursive call for instances thats 16 factor are larger than 10000000000. though I might be confusing factors with multiples.
			# self.factor_16(item)
			# TODO: implement never reached a 16 factor algoritm that does this recursively.

	def check_salt(self, salt):
		if len(salt) > 16:
			return salt[:16]
		elif len(salt) < 0:
			return self.generate_salt()
		elif len(salt) < 16:
			return salt + self.generate_salt()[:16 - len(salt)]

	def check_key(self, key):
		# TODO: how will the datastore handle an object that creates a key that is less then 32? If you add the same charact
		# ERROR: how do you handle keys that are less then 32 in length. 
		if len(key) > 32:
			return key[:32]
		elif len(key) == 32:
			return key
		else:
			logger.error("You have placed a key into the system that is less then the required length.")
			import sys
			sys.exit()

	def generate_salt(self):
		# TODO: you need to make sure you know the rules of this method and salt size.
		return ''.join( [ chr( randint(65,90) ) for i in range(16) ] )
 
