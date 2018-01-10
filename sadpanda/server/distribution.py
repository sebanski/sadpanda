'''
base class for handling all distributed communications - p2p style

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
import os
from uuid import uuid1
import logging
import urllib3

# you can probably delete this iNode and just use the processors information. cut out the complexity
from sadpanda.structs.ifiles.inode import iNode

logger = logging.getLogger(__name__)

# TODO: implement this class.
class Manager(object):
	'''
	base manager that handles interaction with sub classes { DistributionManager, LogicManager }
	'''
	def __init__(self):
		pass

# TODO: what kind of math are you giong to use to distribute these bits across many nodes?????. this is a huge equation. it should be simple, but powerful
class DistributionManager(Manager):
	'''
	a single p2p connected node manager

	this guy handles all transports between agents. he will in the future utilize request/response teams(Objects). 
	that will help break down responsibilities into something the Distribution manager can handle.
	'''
	def __init__(self, server, args, p2p_nodes={}):
		if len(p2p_nodes.keys()) > 0:
			self.p2p_nodes = p2p_nodes
		else:
			self.p2p_nodes = args.p2p_nodes

	def reqeust_relationship(self, hostname, port):
		'''
		request a single relationship with a node believed to be in the graph.
		'''
		headers = {}
		data = {}
		# if relationship is accepted you can create the iNode object and add it to your reference dictionary
		# TODO: implement the below functionality.
		pass

	def request_breakup(self, hostname, port, node_id=None):
		'''
		request a disconnect from the given node.
		'''
		headers = {}
		data = {}
		if node_id == None:
			for k,v in self.p2p_nodes.items():
				if str("%s:%s" % (hostname, str(port))) == v:
					self.remove_node(k)
					logger.info("Removed relationship with node %s:%s" % (hostname, str(port)))
		elif node_id in self.p2p_nodes:
			self.remove_node(node_id)
			logger.info("Removed relationship with node %s:%s" % (hostname, str(port)))
		else:
			logger.warn("You have requested a terminated relationship with a node at %s:%s which does not exist." % (hostname, str(port)))
			logger.warn("  please check your configs and the status of your other node")

	def request_dataflow_downstream(self):
		'''
		request a downstream flow of data to another node. checks all nodes in keychain
		'''
		logger.warn("Initializing round-robin to find dataflow dump node.")
		for k,v in self.p2p_nodes.items():
			# TODO: add logic to find what node is statitcally the best breakdown for bits. This is a shelving algorithm by the way.
			self._request_dataflow_downstream(k,v)

	def _request_dataflow_downstream(self, node_id, node):
		'''
		request a downstream flow of data to another node.
		'''
		headers = {}
		data = {}
		# TODO: implement
		pass

	def check_nodes(self):
		for k,v in self.p2p_nodes.items():
			# TODO: ping the server for its health statistics. then take those into account to make further logically moves.
			pass

	def add_node(self, node):
		self.p2p_nodes.append(node)

	def remove_node(self, node_id):
		if node_id in self.p2p_nodes:
			del self.p2p_nodes[node_id]

# TODO: implement this as its the logic behind the network/io. which is currently handled by the super class. might need to research some design patterns.
class LogicManager(Manager):
	'''
	a child class of the distribution manager. it will house the system wise
	decision making i.e. gathering metadata{drive_space: x , ...} and summating all info. 
	This means that there needs to be an equal agreement between all nodes that the process of 
	sharding/ replicating/ whatever is good. Once it is agreed. data movement -> inode.write . 
	then a final conversation about stats on new instances.
	'''
	def __init__(self):
		self.local_metadata = Metadata()
		self.metadata_nodes = [self.local_metadata]
		self.ping_nodes() # update self.metadata_nodes with the other nodes.
		self.stats = self.gather_stats()

	def add_nodes(self, nodes):
		for node in nodes:
			self.add_node(node)

	def add_node(self, node):
		self.metadata_nodes.append(node)

	def gather_stats(self, metadata):
		#take metadata and create a statistics model for decision making
		self.stats = {}

	def update_metadata(self, args):
		self.metadata_nodes.remove(self.local_metadata)
		self.local_metadata = Metadata()
		self.add_node(self.local_metadata)
		for node in self.ping_nodes():
			self.add_node(node)

	def ping_nodes(self, args):
		# TODO: take args and rutrn responses of all computers
		# return a list of response metadata nodes.
		nodes_metadata = []
		for node in args.p2p_nodes:
		 	node = Metadata(urllib3.urlopen("http://%s/metadata"%(node)).read())
		 	# TOOD: create a route for this. that will just create a Metadata Object store it and send it.
		return []

# TODO: this object needs a correct vmstat parser. it does not work right now.
class Metadata(object):
	def __init__(self, request=None):
		if request == None:
			# TODO: implement these methods as they gather system specific attributes that are used by the logicmanager
			self.root_mount = None
			self.hard_drive_space = self.parse_hard_drive()
			self.vmstat = self.parse_vmstat() # os.popen('vmstat').read().split('\t')
		else:
			# self.cpu_percentage, self.cpu_usage, self.vmstate, self.these_are_incorrect_vars = self.parse_request(request)
			pass

	def parse_hard_drive(self):
		'''
		[~]$ df
		Filesystem                      1K-blocks    Used Available Use% Mounted on
		/dev/mapper/VolGroup00-LogVol00  38765936 1137512  35636132   4% /
		devtmpfs                           239452       0    239452   0% /dev
		tmpfs                              250388       0    250388   0% /dev/shm
		tmpfs                              250388    8484    241904   4% /run
		tmpfs                              250388       0    250388   0% /sys/fs/cgroup
		/dev/sda2                          487634  121406    336532  27% /boot
		tmpfs                               50080       0     50080   0% /run/user/1000
		'''
		data = os.popen('df').read().split('\n')
		# remove header pices
		if data[0].startswith("Filesystem"):
			data.pop(0)
		# TODO: implement some logic about what disk drive the library is formatted on.
		current_devices = []
		for device in data:
			devices = device.split('\t')
			n = 0
			for tdevice in devices:
				if tdevice == "":
					devices.pop(n)
				else:
					n += 1
			this_device = {
				"filesystem": devices[0], 
				"1k_blocks": devices[1], 
				"used": devices[2], 
				"availible": devices[3], 
				"use%":devices[4], 
				"mounted_on": devices[5]
			}
			if devices[5] == "/":
				self.root_mount = this_device
			current_devices.append(this_device)
		# TODO: now sort the devices and get your disk, or disks and only return those. thats all we care about.
		return current_devices

	def parse_vmstat(self):
		'''
    	[~]$ vmstat
    	procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
     	r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
     	2  0      0 278328  17720 137168    0    0     1     1    4    8  0  0 100  0  0
		'''
		data = os.popen("vmstat").read().split('\n')[2]
		data = data.split('\t')
		n = 0
		for i in data:
			if i == '':
				data.pop(n)
			else:
				n += 1
		logger.info("vmstat returned: { %s }" % str(data))
		return { "procs": {
					"r":data[0],
					"b":data[1]},
				 "memory": {
				 	"swpd", data[2],
				 	"free", data[3],
				 	"buff", data[4],
				 	"cache", data[5]
				 },
				 "swap": {
				 	"si", data[6],
				 	"so", data[7]
				 },
				 "io": {
				 	"bi", data[8],
				 	"bo", data[9]
				 },
				 "system": {
				 	"in", data[10],
				 	"cs", data[11]
				 },
				 "cpu": {
				 	"us", data[12],
				 	"sy", data[13],
				 	"id", data[14],
				 	"wa", data[15],
				 	"st", data[16]
				 }
		}

	def parse_request(self, request):
		# TODO: implement a similar system and finalize it
		new_request = request.split("~")
		return new_request[0], new_request[1], new_request[2], new_request[3]
