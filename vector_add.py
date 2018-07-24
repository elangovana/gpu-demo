#! /usr/bin/env python

'''
Example vectorize usage.
'''
from __future__ import print_function

from timeit import default_timer as time

import numpy as np

N = 1000000





def sum(a, b):
    return a + b


def main():


    A = np.random.random(N).astype(np.float32)
    B = np.random.random(N).astype(np.float32)

    vsum = np.vectorize(sum)

    assert A.shape == B.shape
    assert A.dtype ==  B.dtype
    assert len(A.shape) == 1

    D = np.empty(A.shape, dtype=A.dtype)

    print('Data size', N)

    ts = time()
    D = vsum(A, B)
    te = time()

    total_time = (te - ts)

    print('Execution time %.4f' % total_time)
    print('Throughput %.4f' % (N / total_time))

    print(D)




if __name__ == '__main__':
    main()