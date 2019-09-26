import math

def Time_Period(PI,G,M,R):
    A = (4**(PI**2)*(R**3))
    B = G*M
    T = math.sqrt(A/B) 
    return T