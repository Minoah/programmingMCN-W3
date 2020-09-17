import math

def nCr(N, r):
    return float(math.factorial(N) / (math.factorial(r) * math.factorial(N-r)))

#N: number of coins
#n: number of coins that head up
#p: Probability of getting a head

def prob(n, p, N):
    return float(nCr(N, n) * (p ** n) * (1 - p) ** (N - n))

def infoMeasure(n, p, N):
    return float(-math.log2(prob(n, p, N)))

def sumProb(N, p):
    """
    _ N = 10, p = 0.5 => output: 0.9990234375
    _ N = 20, p = 0.8 => output: 0.9999999999999895
    _ N = 40, p = 0.7 => output: 1.0000000000000002
    """
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p, N)
    return float(sum)

#help(sumProb)

def approxEntropy(N, p):
    """
    With p = 1/2:
        _N = 10 => output: 2.696663338227331
        _N = 500 => output: 5.529987244677518
        _N = 1000 => output: 6.029987607045884
    """
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p, N) * infoMeasure(i, p, N)
    return float(sum)
#help(approxEntropy)

