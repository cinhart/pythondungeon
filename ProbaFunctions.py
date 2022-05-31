import math
import random # function used: random.random() -> return float between 0 and 1


## BINOMIAL DISTRIB (p=n)
# Return 0 or 1

def bernouillirand(n):
    r = random.random()
    if(r<n):
        r=1
    else:
        r=0
    return r

## UNIFORM DISTRIB FOR N VALUES (DISCRETE)
# Return a value between 1 and N

def uniformrand(n):
    r = random.random()
    return math.floor(r*n)+1


## STANDARD CAUCHY DISTRIB FROM 0 TO 2A -> MIDDLE = A (CONTINUOUS)

def cauchyrand(A):
    r = random.random()
    r = math.tan(math.pi*(r-0.5))
    return r*0.3

## POISSON DISTRIB

def poissonrand(A, k):
    r = random.random()
    r = math.pow(A,k) * math.exp(-A) / math.factorial(k)
    return r*1000