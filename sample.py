#!/usr/bin/env python3

import sys, itertools

START, END, COST = (0, 1, 2)

class Coconut:
    def __init__(self, defaultCost, streams):
        # a stream is (start, end, cost); for more positions I'd probably give up and use a dict
        self.streams = sorted(streams, key = lambda x: x[START])
        self.defaultCost = defaultCost

        self.start = 0
        self.end = sorted(streams, key = lambda x: x[END])[-1][END]
    
    def lowest(self):
        current = []
        currentCost = ( self.end - self.start ) * self.defaultCost
        for i in range(0, len(self.streams)):
            print("starting with i: %s" % i)
            for streamPath in itertools.combinations(self.streams, i):
                if self.validStreamPath(streamPath):
                    cost = self.costOf(streamPath)
                    print("cost(%s): %s" % (str(streamPath), cost))
                    if cost < currentCost:
                        current = streamPath
                        currentCost = cost
        return current
    
    def validStreamPath(self, streamPath):
        oldEnd = 0
        for stream in streamPath:
            if stream[START] < oldEnd:
                return False
            oldEnd = stream[END]
        return True
    
    def costOf(self, streamPath):
        if not streamPath: 
            return (self.end - self.start) * self.defaultCost
        total = 0
        pos = self.start
        for stream in streamPath:
            total += (stream[START] - pos) * self.defaultCost
            total += stream[COST]
            pos = stream[END]
        total += (self.end - pos) * self.defaultCost
        return total



if(len(sys.argv) < 2): 
    print("Please supply a filename as the first parameter to this script.\n")
    exit()

try:
    config = open(sys.argv[1], 'r')
except FileNotFoundError:
    print("Please supply a valid configuration file as the first parameter to this script.\n")
    exit()

inputStreams = []
defaultCost = None
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

coco = Coconut(defaultCost, inputStreams)

answer = coco.lowest()
total = coco.costOf(answer)

print("The lowest cost path found had a cost of %s and jet streams %s\n" % (total, answer))


