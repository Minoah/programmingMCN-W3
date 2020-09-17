import math

def prob(n, p):
    return float(p * (1-p) ** (n-1))

def infoMeasure(n, p):
    return float(-math.log2(prob(n,p)))

def sumProb(N, p):
    """
    _ N = 10, p = 0.7 => output: 0.9999940950999998
    _ N = 50, p = 0.7 => output: 0.9999999999999997
    _ N = 100, p = 0.5 => output: 1.0 
    """
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p)
    return float(sum)

#help(sumProb)

def approxEntropy(N, p):
    """
    function approxiEntropy approximate entropy of Geometric information source with N go to infinity
    With p = 1/2:
        _N = 10 => output: 1.98828125
        _N = 100 => output: 1.9999999999999998
        _N = 500 => output: 1.9999999999999998
        => Entropy of Geometric information source = 2
    """
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p) * infoMeasure(i, p)
    return float(sum)
#help(approxEntropy)


