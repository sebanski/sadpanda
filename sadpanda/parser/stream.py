 '''
handles all the nodes for the low-level socket implementation packets.
'''
import logging

logger = logging.getLogger(__name__)

class Stream(object):
	'''
	a stream is a stream object that will have the below syntax.
	'''
	def __init__(self):
		self.info = "peace on earth this class is a template right now."

	def create_zenith(self, headers, data):
		# TODO: take the headers and data pieces from the DistributionManager() object...
		pass

class Node(object):
	def __init__(self, value):
		self.value = value

class Zenith(Node):
	'''
	base Message node. houses all metadata about message...
	'''
	def __init__(self, value, expressions):
		self.value = value
		self.expressions = expressions

class Bronze(Node):
	'''
	sub - node of the zentith(Message) class. Contains the headers
	'''
	def __init__(self, args):
		for k,v in args.items():
			self.k = v

	def validate_headers(self, d):
		# NOTE: all the good metadata you can use throughout the process.
		good_headers = [
				"NodeId",
				"iHostname",
				"iPort",
		]
		for i in d.keys():
			if i not in good_headers:
				self.report_spam(i)
				del d[i]
				logger.warn("Header-Value -> %s is not a correct header type." % str(i))
		

	def report_spam(self, header_tuple):
		# TODO: send a signal to a spam collection server for any malicious headers
		pass

class Silver(Node):
	'''
	sub - node of the zentith(Message) class. Contains the body
	'''
	def __init__(self, data):
		if self.validate_data(data):
			self.data = data

	def validate_data(self, d):
		# TODO: implement a data checker for any unwanted data that might be trying to get slipped in.
		return True

	def report_spam(self, header_tuple):
		# TODO: send a signal to a spam collection server for any malicious headers
		pass



