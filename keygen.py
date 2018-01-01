'''
keygen - dont tread on me.
'''
from random import randint
import argparse

def setup_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--num-chars', default=256, type=int)
	return parser.parse_args()

def generate_number():
	return randint(65, 144) # int( randint(0,7435673) / 345.2346 * 456254.54 / 345.456 / 7333333 )

def main():
	args = setup_args()
	return ''.join([ chr( generate_number() ) for i in range(args.num_chars) ])

if __name__ == "__main__":
	print(main())

