#!/usr/bin/env python
from QuickFind import QuickFind as Algorithm
import time
start_time = time.time()

# Create the Tree
filename = 'create.txt'
with open(filename) as f:
    lines = f.readlines()

arraySize = int(lines.pop(0))
nodes = Algorithm(arraySize)

for line in lines:
    [first, second] = line.split(',')
    nodes.union(int(first), int(second))

# Compare
filename = 'compare.txt'
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    [first, second] = line.split(',')
    connected = nodes.connected(int(first), int(second))
    print("%s is connected to %s ? %s" % (first, second, connected))

print("Time Taken --- %s seconds ---" % (time.time() - start_time))
