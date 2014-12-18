


# we'll get these from file shortly
defaultCost = 50
inputStreams = [(0, 5, 10), (1, 3, 5), (3, 7, 12), (6, 11, 20), (14, 17, 8), (19, 24, 14), (21, 22, 2)]



# a stream is (start, end, cost); for more positions I'd probably give up and use a dict
START, END, COST = (0, 1, 2)
streams = sorted(inputStreams, key = lambda x: x[START])
start = 0
end = sorted(streams, key = lambda x: x[END])[-1][END]


def lowest(cost, start, end, possibleStreams):
    current = []
    if (end - start < 1) or not possibleStreams:
        return current
    for i, stream in enumerate(possibleStreams):
        streamEnd = stream[1]
        working = [stream] + lowest(cost, streamEnd, end, streamsAfter(streamEnd, possibleStreams))
        print(working)
        if costOf(cost, start, end, working) < costOf(cost, start, end, current): 
            current = working
    return current

def streamsAfter(endOfOldStream, streams):
    for idx, stream in enumerate(streams):
        if(endOfOldStream <= stream[START]):
            return streams[idx:]
    return []

def costOf(cost, start, end, streams):
    if not streams: 
        return (end - start) * cost
    total = 0
    pos = start
    for stream in streams:
        total += (stream[0] - pos) * cost
        total += stream[2]
        pos = stream[1]
    return total



