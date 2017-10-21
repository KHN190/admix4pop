#!/usr/bin/python3

import sys, os, argparse
sys.path.append(os.path.dirname(__file__))
from admix_frac import estimate
from data_utils import *

def arguments():
    # argument parser
    parser = argparse.ArgumentParser()

    # raw genome data file
    parser.add_argument(
        '-t',
        '--tolerance',
        nargs='?',
        default='1e-3',
        help='tolerance for estimation stop criteria'
    )

    # specify models
    parser.add_argument(
        '-p',
        '--population',
        nargs='?',
        help='set reference populations allele frequencies'
    )

    # tolerance of optimization
    parser.add_argument(
        '-m',
        '--mixture',
        nargs='?',
        help='set mixture population to be analyzed')

    return parser.parse_args()

def main():
    # get arguments
    args = arguments()

    # load population & mixture
    mixture = load_mixture(args.mixture)
    pop_names, populations = load_populations(args.population)

    # start calculation
    fraction = estimate(mixture, populations, float(args.tolerance))

    print('Result:')
    for i in range(len(pop_names)):
    	print('\t%s: %.5f' % (pop_names[i] , fraction[i]))

if __name__ == '__main__':
    main()
