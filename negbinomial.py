import math

def nCr(N, r):
    return float(math.factorial(N) / (math.factorial(r) * math.factorial(N-r)))


def prob(n, p, r):
    return float(nCr(n-1, n-r) * (p ** r) * (1 - p) ** (n - r))

def infoMeasure(n, p, r):
    return float(-math.log2(prob(n, p, r)))

def sumProb(N, p, r):
    """
    _ N = 10, p = 0.5, r = 3=> output: 0.9453125
    _ N = 20, p = 0.7, r = 5=> output: 0.9999944497469216
    _ N = 100, p = 0.4 , r = 6=> output: 0.9999999999999994
    """
    sum = 0
    for i in range(r, N+1):
        sum += prob(i, p, r)
    return float(sum)

#help(sumProb)

def approxEntropy(N, p, r):
    """
    With p = 1/2:
        _N = 10, r = 3 => output: 2.7565968690112412
        _N = 100, r = 3 => output: 3.1156477963110514
        _N = 1000, r = 3 => output: 3.1156477963110514
        _r = 10
            N = 20 => output: 2.250000374614748
            N = 100 => output: 4.150775320863947
            N = 1000 => output: 4.150775320863947
    """
    sum = 0
    for i in range(r, N+1):
        sum += prob(i, p, r) * infoMeasure(i, p, r)
    return float(sum)
#help(approxEntropy)