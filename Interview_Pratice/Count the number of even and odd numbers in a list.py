#Count the number of even and odd numbers in a list.

list = [12,545,48,14,141,54,41,5,44,1,5485]
even = 0
odd = 0
for i in list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)