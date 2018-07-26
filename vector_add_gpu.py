#! /usr/bin/env python

'''
Example vectorize usage.
'''
from __future__ import print_function

import argparse
from timeit import default_timer as time

import numpy as np

from numba import vectorize


# Parallelise sum operations
@vectorize("float32(float32,float32)", target='cuda')
def sum(a, b):
    return a + b


def main(vector_length):
    # Initialise 2 vectors, each with length N with random numbers of float type
    A = np.random.random(vector_length).astype(np.float32)
    B = np.random.random(vector_length).astype(np.float32)

    # # Initialise the resulting vector that holds the sum of A and B
    # C = np.empty(A.shape, dtype=A.dtype)

    # Compute the sum of vectors A & B
    time_start = time()
    result = sum(A, B)
    time_end = time()

    # Compute total execution time
    total_time = (time_end - time_start)
    total_time_secs = total_time.seconds + total_time.microseconds / 1E6

    # Print results
    print("Result: a * b ** 100 * c * d ** 24 * (a + b) ** 9 ** (c + d) ** 100")
    print(result)
    print("-----Stats----")
    print('Vector Length is : ', vector_length)
    print('Execution time is : %.4f ' % total_time_secs)
    print('Throughput is :  %.4f ' % (vector_length / total_time_secs))
    print("---------------")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Enter the vector length", type=int)
    args = parser.parse_args()
    main(args.n)
