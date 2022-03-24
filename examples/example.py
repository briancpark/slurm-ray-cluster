import ray 
import os 
import nums
from nums import numpy as nps
from nums.core import settings
from nums.core.application_manager import instance
import time

settings.use_head = False
print("Running NumS benchmark for %s." % settings.backend_name)
print("Is NumS using head node?:", settings.use_head)

# Initialize ray and connect it to the cluster.
print(os.environ["ip_head"], os.environ["redis_password"])
ray.init(address='auto', _node_ip_address=os.environ["ip_head"].split(":")[0], _redis_password=os.environ["redis_password"])
# Initialize nums with the cluster shape. Here we set it to use all the nodes in the ray cluster.
print("number of ray nodes:", len(ray.nodes()))
print(ray.nodes())
nums.init(cluster_shape=(len(ray.nodes()) - 1, 1))
print(nums.core.settings.cluster_shape)


def main():
    X = nps.random.rand(10 ** 9)
    Y = nps.random.rand(10 ** 9)
    Z = X + Y
    Z.touch()
    print("Z's Grid shape:", Z.grid_shape, "Z's Block shape:", Z.block_shape)


if __name__ == "__main__":
    print("Waiting for raylet worker pool to finish initialization...")
    time.sleep(30)
    print("Waiting done, running main()...")
    begin = time.time()
    main()
    end = time.time()
    print("Time:", end - begin)


    print("another run")

    begin = time.time()
    main()
    end = time.time()
    print("Time:", end - begin)

    print("another run")

    begin = time.time()
    main()
    end = time.time()
    print("Time:", end - begin)

    print("another run")

    begin = time.time()
    main()
    end = time.time()
    print("Time:", end - begin)

    print("another run")

    begin = time.time()
    main()
    end = time.time()
    print("Time:", end - begin)
