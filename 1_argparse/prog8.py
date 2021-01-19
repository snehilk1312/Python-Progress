import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int, help="prints the square of the number")
parser.add_argument("-v", "--verbose", help="gives verbose output", action="store_true")
args = parser.parse_args()

answer = args.square**2

if args.verbose:
	print(f"the square of {args.square} is {answer}")
else:
	print(answer)
