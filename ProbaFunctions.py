import math
import random # function used: random.random() -> return float between 0 and 1


## BINOMIAL DISTRIB. (p=n)
# Return 0 or 1

def bernouillirand(n):
    r = random.random()
    if(r<n):
        r=1
    else:
        r=0
    return r

## NON UNIFORM 3 POSSIBILITIES DISTRIB.
# p=a opt 1, p=b opt 2, p=a-b opt 3

def nonuniformrand3(a,b):
    r=random.random()
    if(r<=a):
        r=1
    elif(r<=a+b):
        r=2
    else:
        r=3
    return r

## UNIFORM DISTRIB. FOR N VALUES
# Return a value between 1 and N

def uniformrand(n):
    r = random.random()
    return math.floor(r*n)+1


## TRIANG. DISTRIB.
# Return a value between a and b, more chances to be close to c

def triangrand(a,b,c):
    c= (c-a)/(b-a)
    r = random.random()

    if(r<=c):
        r=math.sqrt(r*c)
        r=r*(b-a)+a
    elif(r>c):
        r=math.sqrt((1-r)*(1-c))
        r=r*(a-b)+b
    return(r)

## KURAMASWAMY DISTRIB.
#Return a value between 0 and 1, probabilities depens on A and B

def kuramaswamyrand(A,B):
    r = random.random()
    r = 1 - (1-r**A)**B
    return r

## STANDARD CAUCHY DISTRIB FROM 0 TO 2A -> MIDDLE = A

#Return random value which can go up to infinite. Center = 0
def cauchyrand(A,l):
    r = random.random()
    r = l*math.tan(math.pi*(r-0.5))
    return r

#Return random value between A-1/2 and A+1/2. Center = A
def bornedcauchyrand(A,l=1):
    r = cauchyrand(A,l)
    while(abs(r)>=A/2):
        r = cauchyrand(A,l)
    return r+A

## POISSON DISTRIB - UNUSED

#def poissonrand(A, k):
#   r = random.random()
#   r = math.pow(A,k) * math.exp(-A) / math.factorial(k)
#   return r*1000