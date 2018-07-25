# GPU Demo
Code samples for GPU (NVIDIA GPU)demo. 
This is a simple vector add example to compare the execution times for CPU Sequential, CPU parallel and GPU parallel 

## Prerequisites
1. Require NVIDIA CUDA drivers installed to run the GPU example

##How to run
1. This runs on CPU only
    ```shell
    python vector_add.py 10000000
    ```

2. This also runs on the CPU only, but parallelises the operations
    ```shell
    python vector_add_parallel.py 10000000
    ```

3. This runs on the GPU (NVDIA)
    ```shell
    python vector_add_gpu.py 10000000
    ```



