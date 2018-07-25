#! /usr/bin/env python

'''
Example vectorize usage.
'''
from __future__ import print_function

import argparse
from timeit import default_timer as time

import numpy as np







def sum(a, b):
    return a + b


def main(vector_length):


    # Initialise 2 vectors, each with length N with random numbers of float type
    A = np.random.random(vector_length).astype(np.float32)
    B = np.random.random(vector_length).astype(np.float32)

    # Vectorise the sum function so that your dont have to loop through
    #   For in in range(0, vector_length):
    #       ith_sum = A[i] + A[B]
    vectorized_sum = np.vectorize(sum)

    # Compute the sum of A & B
    time_start = time()
    C = vectorized_sum(A, B)
    time_end = time()

    # Compute total execution time
    total_time = (time_end - time_start)

    # Print results
    print("Vector A:")
    print(A)
    print("Vector B:")
    print(B)
    print("Result: A + B")
    print(C)
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