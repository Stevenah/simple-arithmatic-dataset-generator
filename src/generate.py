import operator as op
import argparse
import random
import math

OPERATORS = [
    ("+", op.add),
    ("-", op.sub),
    ("*", op.mul),
    ("/", op.truediv)
]

def generate(args):
    with open(args.filename, 'w') as f:
        for i in range(args.size):
            operator = OPERATORS[random.randrange(0, len(OPERATORS))]
            
            op1 = random.randrange(0, args.range)
            op2 = random.randrange(0, args.range)

            try: 
                result = math.floor(operator[1](op1, op2))
            except ZeroDivisionError:
                result = 'undefined'

            f.write(f"{op1} {operator[0]} {op2} {result}\n")

if __name__ == '__main__':

    ap = argparse.ArgumentParser(description='Generate a dataset of simple arithmatic operations.')

    ap.add_argument('-f', '--filename',
        default='../data/dataset.txt', help='Filename of generated dataset.')

    ap.add_argument('-s', '--size', type=int, 
        default=100, help='Size of the dataset (default: 100).')

    ap.add_argument('-range', '--range', type=int, 
        default=100, help='range of the integers used (default: 100).')

    args = ap.parse_args()
    
    generate(args)