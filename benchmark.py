import os, time
from multiprocessing import Process
from threading import Thread
import grpc
import numpy as np
import interface_pb2 as pb
import interface_pb2_grpc as dan_grpc

# 147.47.206.16:9999
addr = "147.46.123.28:9090"

def _ping(*, addr):
    try:
        with grpc.insecure_channel(addr) as channel:
            conn = dan_grpc.DANInterfaceStub(channel)
            code = conn.ping(pb.Void())
            # print("OK", code)        
    except Exception as e:
        print(e)

def ping(n):
    for i in range(n):
        _ping(addr=addr)

tasks = 1000
# workers = os.cpu_count()
workers = 100
threads = []
st = time.time()
for i in range(workers):
    threads.append(Thread(target=ping, args=(tasks,)))

for t in threads:
    t.start()

for t in threads:
    t.join()

ed = time.time()
total_time = ed - st
print("running in %.2f" % total_time)
print("throughput %.2f" % (tasks*workers/total_time))