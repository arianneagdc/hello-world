import argparse
parser = argparse.ArgumentParser()
parser.add_argument("triangle", help="display a square of a given number")
args = parser.parse_args()
print(args.triangle)