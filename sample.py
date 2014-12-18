


# we'll get these from file shortly
defaultCost = 50
inputStreams = [(0, 5, 10), (1, 3, 5), (3, 7, 12), (6, 11, 20), (14, 17, 8), (19, 24, 14), (21, 22, 2)]



# a stream is (start, end, cost)
streams = sorted(inputStreams, key = lambda x: x[0])
start = 0
end = highestEndPositionIn(streams)





def highestEndPositionIn(streams):
    endPos = 1
    return sorted(streams, key = lambda x: x[endPos])[-1][endPos]

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



