#! /usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo" , help="echo the string you use here")
parser.add_argument("shout", help="this option shouts the string you use here")
args = parser.parse_args()
print(args.echo)
print(args.shout.upper())
