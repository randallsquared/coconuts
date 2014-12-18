


# a stream is (start, end, cost)

defaultCost = 50
streams = [(0, 5, 10), (1, 3, 5), (3, 7, 12), (6, 11, 20), (14, 17, 8), (19, 24, 14), (21, 22, 2)]




def costOf(cost, start, end, streams):
    total = 0
    pos = start
    for stream in streams:
        total += (stream[0] - pos) * cost
        total += stream[3]
        pos = stream[2]
    return total



