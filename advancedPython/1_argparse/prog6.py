import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("square", help = "squares a number", type=int)
parser.add_argument("--verbosity", help = "increase output verbosity", action="store_true")
args = parser.parse_args()

print(args.square**2)

if args.verbosity:
        print(f"Program ran on {datetime.datetime.now()}")
