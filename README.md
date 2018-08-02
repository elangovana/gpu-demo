# GPU Demo
Code samples for GPU (NVIDIA GPU)demo. 
This is a simple vector add example to compare the execution times for CPU Sequential, CPU parallel and GPU parallel 

## Prerequisites
1. Require NVIDIA CUDA drivers installed to run the GPU example

##How to run
### Vector Add
1. This runs on Vector Add CPU only
    ```shell
    python vector_add.py 10000000
    ```

2. This also runs on the CPU only, but parallelises the operations
    ```shell
    python vector_add_parallel.py 100000000
    ```
    ```shell
    nvprof --print-summary  --cpu-profiling on  vector_add_parallel.py 100000000
    ```
    
3. This runs on the GPU (NVDIA)
    ```shell
    python vector_add_gpu.py 100000000
    ```
    ```shell
    nvprof --print-summary  --cpu-profiling on  vector_add_gpu.py 100000000
    ```


### Vector Mutiply

2. This multiply runs on the CPU only, but parallelises the operations
    ```shell
    python vector_multiply_parallel.py 100000000
    ```
    ```shell
    nvprof --print-summary  --cpu-profiling on  vector_multiply_parallel.py 100000000
    ```

3. This runs on the GPU (NVDIA)
    ```shell
    python vector_multiply_gpu.py 100000000
    
    ```
    
    In order to check the utilisation on the GPU vs CPU.
    ```shell
    nvprof --print-summary  --cpu-profiling on vector_multiply_gpu.py 100000000
    ```

### Run All
1. Run All
    ```shell
    python vector_add.py 10000000
    python vector_add_parallel.py 100000000
    python vector_add_gpu.py 100000000
    python vector_multiply_parallel.py 100000000
    python vector_multiply_gpu.py 100000000
    ```
    
## Large Score image

```shell
python train_imagenet.py --network resnet --num-layers 152 --data-train ~/data/train --data-val ~/data/val/ --gpus 0,1,2,3  --batch-size 10 --num-epochs 1 --kv-store device > ~/data/log_device.txt 2>&1 &

python train_imagenet.py --network resnet --num-layers 152 --data-train ~/data/train --data-val ~/data/val/  --batch-size 10 --num-epochs 1 --kv-store local > ~/data/log.txt 2>&1 &

nvprof --print-summary  --cpu-profiling on --log-file ~/data/profileOutput.txt  python train_imagenet.py --network resnet --num-layers 152 --data-train ~/data/train --data-val ~/data/val/ --gpus 0,1,2,3  --batch-size 10 --num-epochs 1 --kv-store device > ~/data/log_device_222.txt 2>&1 &


nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max,pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv -l 5

MEMORY,UTILIZATION,COMPUTE
```