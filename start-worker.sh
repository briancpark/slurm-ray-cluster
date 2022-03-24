#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

conda activate nums
echo "starting ray worker node"
ray start --address $1 --redis-password=$2 --num-cpus=32 --object-store-memory=40000000000 --temp-dir=$SCRATCH/ray
sleep infinity
