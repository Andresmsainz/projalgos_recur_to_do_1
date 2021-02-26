#Recursive Sigma
def rSigma(num):
    if (num > 0): 
        return rSigma(num - 1) + num
    return 0

print("rSigma 5 = ",rSigma(5))
print("rSigma 2.5 = ",rSigma(2.5))
print("rSigma -1 = ",rSigma(-1))

#Recursive Fraction
def rFact(num):
    if (num > 1): 
        return rFact(num - 1) * num
    return 1

print("rFact 3 = ",rFact(3))
print("rFact 6.5 = ",rFact(6.5))
