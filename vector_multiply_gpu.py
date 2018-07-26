#! /usr/bin/env python

'''
Example vectorize usage.
'''
from __future__ import print_function

import argparse
from timeit import default_timer as time

import numpy as np

from numba import vectorize


# Parallelise multiply operations
@vectorize("float32(float32,float32,float32,float32,float32,float32)", target='cuda')
def mutiply(a, b, c, d, e, f):
    return a * b ** 100 * c * d ** 24 * e ** 21 * f ** 2


def main(vector_length):
    # Initialise vectors, each with length N with random numbers of float type
    A = np.random.random(vector_length).astype(np.float32)
    B = np.random.random(vector_length).astype(np.float32)
    C = np.random.random(vector_length).astype(np.float32)
    D = np.random.random(vector_length).astype(np.float32)
    E = np.random.random(vector_length).astype(np.float32)
    F = np.random.random(vector_length).astype(np.float32)

    # Compute the sum of vectors A & B
    time_start = time()
    result = mutiply(A, B, C, D, E, F)
    time_end = time()

    # Compute total execution time
    total_time = (time_end - time_start)

    # Print results

    print("Result: a * b ** 100 * c * d ** 24 * e ** 21 * f ** 2")
    print(result)
    print("-----Stats----")
    print('Vector Length is : ', vector_length)
    print('Execution time is : %.4f ' % total_time)
    print('Throughput is :  %.4f ' % (vector_length / total_time))
    print("---------------")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Enter the vector length", type=int)
    args = parser.parse_args()
    main(args.n)
