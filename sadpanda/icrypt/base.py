'''
base encryption class for all encryption methods.

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
.||   /  |  \   |||
  \+<|   |   |>+/
      \ /|\ /
       V===V
       |   |
   ___/     \___
				 
		 sadpanda

by: alex balzer
'''
import crypt
import logging

logger = logging.getLogger(__name__)

class Base(object):
	def __init__(self, item, salt):
		self.encrypted_item = self.encrypt(item, salt)

	def encrypt(self, item, salt):
		return crypt.crypt(item, salt) # honestly this is a bad method as you cant decrypt i dont believe.
