#! /usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo" ,nargs='?', help="echo the string you use here")
args = parser.parse_args()
print(args.echo)
