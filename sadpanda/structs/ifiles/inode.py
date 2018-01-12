'''
base object for a single instance. handles all file/io for a single instance. logic reported to it is through the LogicManager and the DistributionManager. which are handled wy the Manager

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
from math import ceil
import logging

# from boto import s3

from sadpanda.icrypt.aes import iAES
from sadpanda.structs.ifiles.compressor import SnappyCompressor, SnappyDecompressor
from sadpanda.structs.datastore import DataStore

logger = logging.getLogger(__name__)


class iNodeMetadata(object):
	'''
	breakpoints = [ (begin: 45, end: 2, num_files_spanned: 1) ] - these are logical representations of where an object starts and ends on disk.
	'''
	def __init__(self, files, breakpoints):
		self.files = files
		self.breakpoints = breakpoints

	def close(self, args):
		# TODO: implement a close method for this as you need to save state on disk.
		import pickle
		# TODO: make all files absolute....
		w = open('data/blockchain.evm', 'wb')
		item = {"files": self.files, "breakpoints": self.breakpoints }
		item = str( pickle.dump(item) )
		item = SnappyCompressor(item, args, encrypt=True).compressed_data
		item = iAES(item, open(args.keyfile , 'rb').read()).encrypted_value
		w.write(item)
		w.close()
		logger.info("Wrote the inodes metadata to disk...")

	def open(self, args):
		import pickle
		# TODO: implement a close method for this as you need to save state on disk.
		# TODO: make all files absolute....
		metadata = open('data/blockchain.evm', 'rb').read()
		metadata = iAES(metadata, open(args.keyfile , 'rb').read())
		metadata = data.decrypt(metadata, open(args.keyfile , 'rb').read(), args)
		metadata = SnappyDecompressor(metadata, args, decrypt=True).decompressed_data
		data = pickle.load(metadata)
		self.files = data["files"]
		self.breakpoints = data["breakpoints"]
		# TODO: just set your variables from the metadata

	def load_metadata(self):
		# TODO: load the metadata from disk into this object
		pass 

# TODO: implement this object as it serves as the coordinator for a instances file-writes
# TODO: add s3 support so you can just do s3 writes for the project.
class iNode(object):
	'''
	file data handler in a nutshell
	'''
	# TODO: implement a metadata attribute that saves the inodes state. for on restart.
	inode_metadata = None
	def __init__(self, data, sibling_nodes=[], key=None):
		self.inode_metadata = iNodeMetadata(self.load_files(), self.load_breakpoints()).load_metadata()
		self.files = {}
		self.data = data
		self.sibling_nodes = sibling_nodes
		if key == None:
			# no key specified. generate a random_key...
			self.key = ""
		else:
			self.key = key

	def write(self, data, filename, args):
		# TODO: add a write method that handles encryption and compression based on user configs.
		w = open('data/%s'%filename, 'ab')
		if args.compression == True:
			if args.compression_type.lower() == "snappy":
				data = SnappyCompressor(data, args, encrypt=True).compressed_data
		if args.encrypt_on_disk == True:
			if args.encrypt_on_disk_type.lower() == "aes":
				data = iAES(data, open(args.keyfile , 'rb').read()).encrypted_value
		w.write(data)
		w.close()
		logger.info("Just wrote file <%s> to %s" % (filename, args.datastore) )

	def read(self, filename, args):
		# TODO: add a read method
		data = open(filename,'rb').read()
		if args.encrypt_on_disk == True:
			if args.encrypt_on_disk_type.lower() == "aes":
				data = iAES(data, open(args.keyfile , 'rb').read())
				data = data.decrypt(data, open(args.keyfile , 'rb').read(), args)
		if args.compression == True:
			if args.compression_type.lower() == "snappy":
				data = SnappyDecompressor(data, args, decrypt=True).decompressed_data

	def data_write(self, args):
		'''
		write the data from self.data
		'''
		w = open('data/%s'%filename, 'ab')
		if args.compression == True:
			if args.compression_type.lower() == "snappy":
				self.data = SnappyCompressor(self.data, args, encrypt=True).compressed_data
		if args.encrypt_on_dick == True:
			if args.encrypt_on_disk_type.lower() == "aes":
				self.data = iAES(self.data, open(args.keyfile , 'rb').read()).encrypted_value
		w.write(self.data)
		w.close()
		logger.info("Just wrote file <%s> to %s" % (filename, args.datastore) )

	def generate_files(self, args):
		'''
		take the data stored in the inode and distribute it against multiple files in the data/ directory
		'''
		# TODO: you need to rigourously test this method.
		# TODO: you need to implement the file naming logic based on the given criteria.
		# TODO: TODO: this is a big one. this method will contain the molding of the inode_metadata.breakpoints.
		if len(self.data) > args.max_file_length:
			# TODO: go through the string and chop until you hit max_file_length. write that data to file. close file. move on to next piece doing the same thing
			iterations = ceil( args.max_file_length / len(self.data) )
			file_begin = 0
			file_end = args.max_file_length
			inode_metadata.breakpoints.append((file_begin, file_end))
			for i in range(iterations):
				new_data = self.data[file_begin:file_end:]
				# TODO: implement a filename_generator for this library to use
				filename = "something-%s" % str(i)
				self.write(new_data, filename, args)
				file_begin = file_end + 1
				new_file_end = file_begin + args.max_file_length
				# TODO: fix the below expression as it will fail on the last node.
				if file_begin + new_file_end > len(self.data):
					# handle giving the correct amount
					new_file_end = len(self.data) - file_begin
				file_end = file_end + new_file_end
				inode_metadata.breakpoints.append((file_begin, file_end))
		else:
			# TODO: implemtn filenaming machine
			filename = "something"
			self.write(self.data, filename, args)

	def regenerate_datastore(self, args):
		'''
		this method witl regenerate the DataStore item. you have to use the
		indoe_metadata.breakpoints to reconstruct objects.
		'''
		# TODO: implement this method as it is a big part of this.
		pass

	def load_files(self):
		# TODO: implement a batch file load that will convert the files back into ledgers for the datastore.
		import os
		if os.path.isdir('data/'):
			dirs = os.listdir('data/')
			nodes = [ self.read(i, args) for i in dirs if os.path.isdir(i) ]
			return nodes
		else:
			logger.warn("There does not seem to be a directory dedicated to the datastores files.")
			return []

	def load_breakpoints(self):
		import pickle
		import os
		if os.path.isfile('data/blockchain.ev.bp'):
			r = open('data/blockchain.ev.bp','rb').read()
			return pickle.loads(r)
		else:
			return []

# NOTE: any time the system is restarted this node needs to be started.
	def load_metadata(self, args):
		inode_metadata = iNodeMetadata([],[])
		inode_metadata.open(args)
		self.inode_metadata = inode_metadata

	def save_metadata(self, args):
		#inode_metadata = iNodeMetadata([],[])
		self.inode_metadata.close(args)
		# self.inode_metadata
