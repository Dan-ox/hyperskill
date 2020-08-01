import argparse
import sys


parser = argparse.ArgumentParser()


parser.add_argument('--num1', help="Number 1", type=float)
parser.add_argument('--num2', help="Number 2", type=int)
parser.add_argument('--operation', help="provide operator", default='+')

args = parser.parse_args()
args_list = sys.argc

print(args_list)

result = None
if args.operation == '+':
    result = args.num1 + args.num2
if args.operation == '*':
    result = args.num1 + args.num2
if args.operation == '-':
    result = args.num1 + args.num2
if args.operation == 'pow':
    result = pow(args.num1, args.num2)
print(result)



