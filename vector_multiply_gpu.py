#! /usr/bin/env python

'''
Example vectorize usage.
'''
from __future__ import print_function

import argparse
from timeit import default_timer as time

import numpy as np
from datetime import datetime

from numba import vectorize


# Parallelise multiply operations
@vectorize("float32(float32,float32,float32,float32)", target='cuda')
def mutiply(a, b, c, d):
    return a * b ** 100 * c * d ** 24 * (a + b) ** 9 ** (c + d) ** 100


def main(vector_length):
    # Initialise vectors, each with length N with random numbers of float type
    A = np.random.random(vector_length).astype(np.float32)
    B = np.random.random(vector_length).astype(np.float32)
    C = np.random.random(vector_length).astype(np.float32)
    D = np.random.random(vector_length).astype(np.float32)

    # Compute vector multiply
    time_start = datetime.now()
    result = mutiply(A, B, C, D)
    time_end = datetime.now()

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
