import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int, help="display the square of a number")
parser.add_argument("-v", "--verbose", type=int, help="increase output verbosity", choices=[0,1,2])

args = parser.parse_args()

if args.verbose == 2 :
        print(f"the square of {args.square} is {args.square**2}")

elif args.verbose == 1:
        print(f"{args.square}^2={args.square**2}")

else:
        print(args.square**2)
