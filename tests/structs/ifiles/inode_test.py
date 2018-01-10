'''
test sute for sadpanda/structs/ifiles/inode.py
'''
import pytest

from structs.ifiles.inode import iNode

def before_test():
	# setup mock args, mock objects if needed
	pass

def test__init__(data, sibling_nodes=[], key=None):
	# CASE 1
	inode = iNode("here is some random data")
	assert inode.files == {}
	assert inode.data == "here is some random data"
	assert inode.sibling_nodes == []
	assert inode.key == None
	# TODO: add all transaction methods in here.

# =====================================
# =====================================
# TODO: finish the rest of these tests.
# =====================================
# =====================================

def test_write(data, filename, args):
	# TODO: add a write method that handles encryption and compression based on user configs.
	w = open('data/%s'%filename, 'wb')
	# NOTE: all below arguments add hugh disk/io latency.
	if args.compression == True:
		if args.compression_type.lower() == "snappy":
			data = SnappyCompressor(data, args, encrypt=True).compressed_data
		else:
			# TODO: handle default compression type
			# data = Gzip(data, args, ...)
			pass
	if args.encrypt_on_dick == True:
		if args.encrypt_on_disk_type.lower() == "aes":
			data = iAES(data, open(args.keyfile , 'rb').read()).encrypted_value
		else:
			# TODO: handle default encryption type
			# data = Blowfish(data, args, ...)
			pass
	w.write(data)
	w.close()
	logger.info("Just wrote file <%s> to %s" % (filename, args.datastore) )

def test_read(self):
	# TODO: add a read method
	pass

def test_generate_files(self, args):
	'''
	take the data stored in the inode and distribute it against multiple files in the data/ directory
	'''
	# TODO: you need to rigourously test this method.
	# TODO: you need to implement the file naming logic based on the given criteria.
	if len(self.data) > args.max_file_length:
		# TODO: go through the string and chop until you hit max_file_length. write that data to file. close file. move on to next piece doing the same thing
		iterations = ceil( args.max_file_length / len(self.data) )
		file_begin = 0
		file_end = args.max_file_length
		for i in range(iterations):
			new_data = "V" * file_end - file_begin # [file_begin:file_end]
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
	else:
		# TODO: implemtn filenaming machine
		filename = "something"
		self.write(self.data, filename, args)

