# Check if a Number is Automorphic.

def automorphic(n):
    org = n
    sq = n * n
    
    digit = sq % 10
    if org == digit:
        return True
    else:
        return False
    
n = 5
print(automorphic(n))