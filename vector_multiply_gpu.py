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
    return (a * (b ** 10) * c * (d ** 240) * ((a + b) ** 9) * ((c + d) ** 100) * ((a + d) ** 10))**100


def main(vector_length):
    start_time = datetime.now()

    # Initialise vectors, each with length N with ones of float type
    A = np.ones(vector_length).astype(np.float32)
    B = np.ones(vector_length).astype(np.float32)
    C = np.ones(vector_length).astype(np.float32)
    D = np.ones(vector_length).astype(np.float32)

    # Compute vector multiply
    exec_start_time = datetime.now()
    result = mutiply(A, B, C, D)
    exec_end_time = datetime.now()

    # Compute total execution time
    exec_time = (exec_end_time - exec_start_time)
    total_exec_time = exec_end_time - start_time

    # Print results
    print("Result: (a * (b ** 10) * c * (d ** 240) * ((a + b) ** 9) * ((c + d) ** 100) * ((a + d) ** 10))**100")
    print(result)
    print("-----Stats----")
    print('Vector Length is : ', vector_length)
    print('Execution time is : %.4f ' % exec_time.total_seconds())
    print('Total Execution time is : %.4f ' % total_exec_time.total_seconds())
    print('Throughput is :  %.4f ' % (vector_length / exec_time.total_seconds()))
    print("---------------")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Enter the vector length", type=int)
    args = parser.parse_args()
    main(args.n)
