'''
a basic http server for handling transactions

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
\|.   /  |  \   .|.
  \+<|   |   |>+/
      \ /|\ /
       V===V
       |   |
   ___/     \___

     sadpanda

by: alex balzer
'''
import socket
import logging

import asyncio

logger = logging.getLogger(__name__)

# TODO: implement a model class that will adhere to the nosql like document abilities, especially when you wrap this in a ipython shell.

class AsyncServer(object):
	def __init__(self, port, args):
		self.port = port
		#self.start()

	async def process(self, reader, writer):
		while True:
			data = await reader.readline()
			writer.write(data) 

	def start(self):
		self.loop = asyncio.get_event_loop()
		self.listener = asyncio.start_server(self.process, host=None, port=self.port)
		self.loop.run_until_complete(self.listener)
		self.loop.run_forever()

	def stop(self):
		self.loop.stop()
		self.loop.close()

################################################################################################################
################################################################################################################
################################################################################################################

# TODO: implement this class, dont go crazy and reinvent the wheel use a well written library to abstract out a lot of these complexities.
class iBaseServer(object):
	'''
    the base http server which handles all internet transactions.

    this is a different version as it uses raw sockets.

	sadpanda default port = 9871
	'''
	def __init__(self, hostname='localhost', port=9871):
		self.hostname = hostname
		self.port = port

	def setup_server(self):
		'''
		take all the objects items and create a base socket server for your distributed software. 
		'''
		serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serversock.bind((self.hostname, self.port))
		serversock.listen(5)
		while(1):
			(clientsock, address) = serversock.accept()
			# TODO: you need to wrap this logic in intelligent engineering that can successfully server:response back the good good.
			clientsock.send("kgeriuvberoivbeairbipdfnbljdfshboiethblknbldfhbosdfhbrtbsflhbgblh!!!")

	def handle_request(self, request):
		'''
		validate the request, and use a case like structure to solve clients expectations, but also solve hackers conundrum.
		'''
		pass

