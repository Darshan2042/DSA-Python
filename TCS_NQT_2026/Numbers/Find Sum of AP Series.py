# Find Sum of AP Series

def ap_series(a, d, n):        # function with a = first term, d = common difference, n = number of terms
    total = 0                  # variable to store the sum of the AP series
    term  = a                  # start with the first term

    for i in range(n):         # loop runs n times (for n terms)
        total += term          # add the current term to the total sum
        term += d              # generate the next term by adding common difference

    return total               # return the final sum


print(ap_series(2,2,5))       # calling the function with a=2, d=2, n=5