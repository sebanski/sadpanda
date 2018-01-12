'''
basic block chain database/algorithm.

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
.|/   /  |  \   \|.
  \+<|   |   |>+/
      \ /|\ /
       V===V
       |   |
   ___/     \___
				 
		 sadpanda

by: alex balzer
'''
# TODO: extend this from flask blueprints. so that all objects hold the power to server content on top of there functionality.
import crypt
import random
import pprint as pp
import pickle
import logging
import datetime
import argparse
from sys import path
import os

from sadpanda.icrypt.aes import iAES
from sadpanda.structs.processor import Processor
from sadpanda.parser.config import ConfigParser

# NOTE: super naive. but just getting shit going.
# TODO: create a better encryption method. make it a class so it works < forward -> encrypt , backwards <- decrypt >

def setup_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--encryption-method", default='aes', type=str)
	parser.add_argument("--data-store", default='redis', type=str)
	parser.add_argument("--keyfile", default='blockchain.evk', type=str)
	parser.add_argument("--datastore", default='data/blockchain.ev', type=str)
	parser.add_argument("--hostname", default='', type=str)
	parser.add_argument("--port", default=80, type=int)
	parser.add_argument("--server-threads", default=1, type=int)
	parser.add_argument("--config-file", default="conf/sadpanda.yml", type=str)
	parser.add_argument("--p2p-nodes", default=["localhost:9871"], type=list)
	parser.add_argument("--poppyfarm", default="/etc/sadpanda.d/poppyfarm.ve", type=str)
	# TODO: add the remaining default config variables. there are a lot...
	return parser.parse_args()

def setup_logger(log_name):
	if not os.path.exists(log_name):
		os.mkdir("log")
	logging.basicConfig(filename=log_name, level=logging.DEBUG, datefmt="%y-%m-%d-%h-%mm-%s")

def setup_config(config_filename, args):
	config = ConfigParser(config_filename)
	print("Config data: %s" % str(config.__dict__))
	parser = config.merge_args(args)
	return parser.parse_args()

def get_next_token(size):
	token = ''.join( [ chr(random.randint(65, 90)) for i in range(size) ] )
	logging.info("Created token %s" % token)
	return token

def main(args):
	# TODO: implement a method that will open the data/*.ev file and place it into memory
	# NOTE: in the future items will become to large so you have to handle what parts should be in memory
	# NOTE: you are also going to need to add a distributed system to this. but for the time being focus on running this on one machine.
	# TODO: you need to replace this method with a generate_key() method that will keep one part in memory. 
	key = open(args.keyfile, "r").read()
	blockchain = Processor("this is an important ledger that is valid in some sort of application....", key, args)
	# NOTE: the below methods emulate a ping from an external client that represents data to be placed within the block
	# TODO: wrap the processor or have it work with an external https server that handles all requests, and the processor handles all the underlying compute.
	blockchain.add_entry("here is another very important ledger to be housed within the blockchain....")
	blockchain.add_entry("hsghikbaeflvihafsovilhadfoivhadfv....")
	blockchain.add_entry("here is auegaviuvkber8qEYR895QRG89Y58948blockchain....")
	blockchain.add_entry("h8V0H3	089	G59RGUEUGHQER98GHQ38RBVR F FE89 9F8 GHQE88AOVG08ERHV8AOEHBVA8in....")
	blockchain.add_entry("lkafdhg08yeetGATHRAYHYarbuhfaouiagereg8u89reg8ea8gvaiudvakvdvkjgdfvg")
	blockchain.save_datastore(args.datastore)
	logging.info("Created a base test blockchain")
	#blockchain.run_server(args)
	#blockchain.daemonize(key, args)

if __name__ == "__main__":
	setup_logger("log/blockchain.log")
	args = setup_args()
	logging.info("Args before: %s" % str(args.__dict__))
	args = setup_config(args.config_file, args)
	logging.info("Args after: %s" % str(args.__dict__))
	main(args)

