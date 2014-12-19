#!/usr/bin/env python3

import sys, itertools

# we'll get these from file shortly
defaultCost = None
inputStreams = []

# a stream is (start, end, cost); for more positions I'd probably give up and use a dict
START, END, COST = (0, 1, 2)



# def lowest(cost, start, end, possibleStreams):
#     current = []
#     if (end - start < 1) or not possibleStreams:
#         return current
#     for stream in possibleStreams:
#         working = [stream] + lowest(cost, stream[END], end, streamsAfter(stream[END], possibleStreams))
#         if costOf(cost, start, end, working) < costOf(cost, start, end, current): 
#             current = working
#     return current
# 
# def streamsAfter(endOfOldStream, streams):
#     for idx, stream in enumerate(streams):
#         if endOfOldStream <= stream[START]:
#             return streams[idx:]
#     return []


def lowest(possibleStreams):
    current = []
    currentCost = ( end - start ) * defaultCost
    for i in range(len(possibleStreams), 0, -1):
        for streamPath in itertools.combinations(possibleStreams, i):
            if validStreamPath(streamPath):
                cost = costOf(defaultCost, start, end, streamPath)
                print("cost(%s, %s, %s, %s): %s" % (defaultCost, start, end, str(streamPath), cost))
                if cost < currentCost:
                    current = streamPath
                    currentCost = cost
    return current

def validStreamPath(streams):
    oldEnd = 0
    for stream in streams:
        if stream[START] < oldEnd:
            return False
        oldEnd = stream[END]
    return True

def costOf(cost, start, end, streams):
    if not streams: 
        return (end - start) * cost
    total = 0
    pos = start
    for stream in streams:
        total += (stream[0] - pos) * cost
        total += stream[2]
        pos = stream[1]
    total += (end - pos) * cost
    return total


if(len(sys.argv) < 2): 
    print("Please supply a filename as the first parameter to this script.\n")
    exit()

try:
    config = open(sys.argv[1], 'r')
except FileNotFoundError:
    print("Please supply a valid configuration file as the first parameter to this script.\n")
    exit()

first = True
for line in open(sys.argv[1], 'r'):
    if first:
        defaultCost = int(line)
        first = False
        continue
    # otherwise, we have a stream triple
    triple = line.split(' ')
    inputStreams.append((int(triple[START]), int(triple[END]), int(triple[COST])))

if not defaultCost: 
    print("Please supply a valid configuration file with the first line containing a cost integer.\n")
    exit()

streams = sorted(inputStreams, key = lambda x: x[START])
start = 0
end = sorted(streams, key = lambda x: x[END])[-1][END]

answer = lowest(streams)
total = costOf(defaultCost, start, end, answer)

print("The lowest cost path found had a cost of %s and jet streams %s\n" % (total, answer))


