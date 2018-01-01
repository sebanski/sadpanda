'''
base inode file compressor

by: alex balzer
'''
import logging

import snappy
# from snappy-python import SnappyCompressor

logger = logging.getLogger(__name__)

# TODO: move all data writes into inode objects that will create sequential seperated files. both locally and across a network of inodes.
# TODO: implement a fast compression algorithm. use it within here. snappy is not a bad choice. i believe there are sdks for it to bind with PyObjects i believe.

def install_snappy():
	import os
	os.mkdir("/opt/snappy")
	r = os.popen("git http://github.com/google/snappy.git -O /opt/snappy").read()
	# TODO: handle output from command
	r = os.popen("yum -y install libsnappy ...").read()
	# TODO: handle output from command

class Compressor(object):
	def __init__(self, filedata, args):
		self.info = "base idea of what the compressor object should look like"
		pass

class Decompressor(object):
	def __init__(self, filedata, args):
		pass

class SnappyDecompressor(Decompressor):
	'''
	snappy-decompressor
	'''
	def __init__(self, filedata, decompress=True):
		if decompress == True:
			self.decompress = decompress
			self.decompressed_data = self.decompress(filedata)

	def open_filedata(self, filedata):
		'''
		all data should be returned as a string object.
		'''
		# TODO: handle whatever bizarre file opening mechanism you are going to do here...
		if isisntance(filedata, str):
			return filedata
		elif isinstance(filedata, list):
			new_data = ""
			for i in filedata:
				if isinstance(i, str):
					new_data += i
				elif isinstance(i, unicode):
					new_data + str(i)
				else:
					logging.error("Encountered corrupt data at point %s in data structure %s." % (str(i), str(filedata)))
					# TODO: do some advanced functionality here. make sure you handle corrupt shit well.
			return new_data
		else:
			logging.error("There is a corrupt filedata object being passed into the compression lib. !!!!!!!")
			# TODO: handle this type of event gracefully.

	def decompress(self, filedata):
		return snappy.decompress(filedata)

	def get_decompressed_data(self, filedata=None):
		if filedata == None:
			return self.decompressed_data
		else:
			return self.decompress(self.open_filedata(filedata))

class SnappyCompressor(Compressor):
	'''
	this should be implemented using some snappy-python lib
	'''
	def __init__(self, filedata, compress=True):
		if compress == True:
			self.compress = compress
			self.compressed_data = self.compress(filedata)

	def open_filedata(self, filedata):
		'''
		all data should be returned as a string object.
		'''
		# TODO: handle whatever bizarre file opening mechanism you are going to do here...
		if isisntance(filedata, str):
			return filedata
		elif isinstance(filedata, list):
			new_data = ""
			for i in filedata:
				if isinstance(i, str):
					new_data += i
				elif isinstance(i, unicode):
					new_data + str(i)
				else:
					logging.error("Encountered corrupt data at point %s in data structure %s." % (str(i), str(filedata)))
					# TODO: do some advanced functionality here. make sure you handle corrupt shit well.
			return new_data
		else:
			logging.error("There is a corrupt filedata object being passed into the compression lib. !!!!!!!")
			# TODO: handle this type of event gracefully.

	def compress(self, filedata):
		return snappy.compress(filedata)

	def get_compressed_data(self, filedata=None):
		if self.compress == True:
			return self.compressed_data
		else:
			return self.compress(self.open_filedata(self.filedata))
