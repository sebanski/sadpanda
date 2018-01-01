'''
the sadpanda config parser.

     __     __
    /  \ ^ /  \
    \ /  |  \ /
     | . | . |
      \__A__/
.|.   /  |  \   ||.
  \+<|   |   |>+/
      \ /|\ /
       V===V
       |   |
   ___/     \___
				 
		 sadpanda

this object should meld with your command line arguments
'''
import json
import yaml
# NOTE: might be a circular dependency
import argparse
import logging

logger = logging.getLogger(__name__)

class ConfigParser(object):
	def __init__(self, filename):
		self.filename = filename
		self.data = self.iopen(self.filename)
		if self.data == None:
			from sys import exit
			# NOTE: just fail the process from a bad input config file.
			print("You entered in a malformed config-file, please specify a good file, or restore your config to the default setting...")
			exit(1)
		# TODO: now take your argument parser and converge the data into it. the class works very well so take full advantage of it.
		# return self.merge_args(self.data, parser)

	def iopen(self, filename):
		# TODO: impelement a multi statement file parser that can handle all differnt types
		data = open(filename, 'r').read()
		if filename.endswith('.json'):
			try:
				# print(data)
				return json.loads(data)
			except Exception as e:
				logger.error(e)
				return None
		elif filename.endswith('.yaml') or filename.endswith('.yml'):
			try:
				# print(data)
				return yaml.load(data)
			except Exception as e:
				logger.error(e)
				return None

	def merge_args(self, args):
		# TODO: this method needs to take your current object and use the argparse library to update the configs.
		parser = argparse.ArgumentParser()
		for k,v in args.__dict__.items():
			# TODO: add metatdata object checkers that skip that k,v pair.
			# if k not in self.data.keys():
			parser.add_argument("--%s"%k.replace('_','-'), default=v, type=type(v))
		for k,v in self.data.items():
			# NOTE: this might be extremely dangerous..
			if k.replace('-','_') not in args.__dict__.keys():
				parser.add_argument("--%s"%k.replace('_','-'), default=v, type=type(v))
		return parser

