import argparse

parser = argparse.ArgumentParser()

parser.add_argument("x", type=int , help="the base")
parser.add_argument("y", type=int , help="power")
parser.add_argument("-v", "--verbose", type=int , help="modify the verbosity", choices=[0,1,2])

args = parser.parse_args()
answer = args.x ** args.y

if args.verbose == 2:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))

elif args.verbose == 1:
	print("{}^{} == {}".format(args.x, args.y, answer))
else:
	print(answer)


