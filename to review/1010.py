def numPairsDivisibleBy60(time):
    c = [0] * 60
    res = 0
    for t in time:
        res += c[-t % 60]
        c[t % 60] += 1
    return res