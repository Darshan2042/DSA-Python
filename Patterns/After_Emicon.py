# n = 4
# for i in range(n + 1):
#     print("*" * i)
# for j in range(n-1,-1,-1):
#     print("*" * j)


# n = 4
# for i in range(n):
#     print("*"*n)
# print()

# n = 4
# c = 6
# for i in range(n):
#     for j in range(c):
#         if i ==0 or j == 0 or i == n-1 or j == c-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == j or i+j == n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == n//2 or j == n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")

#     for k in range(2*i+1):
#         print("*",end="")
#     print()
    


# string = "india is greater "
# result = ""
# word = ""

# for ch in string:
#     if ch != " ":
#         word += ch
#     else:
#         rev = ""
#         i = len(word)-1

#         while i >= 0:
#             rev += word[i]
#             i -=1

#         result += rev + " "
#         word = ""

# print(result.strip())

# string = "India is greater "
# result = ""
# word = ""

# for ch in string:
#     if ch != " ":
#         word += ch
#     else:
#         # reverse the word manually
#         rev = ""
#         i = len(word) - 1
#         while i >= 0:
#             rev += word[i]
#             i -= 1

#         result += rev + " "
#         word = ""

# # remove last extra space
# print(result.strip())


# n = 7

# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 7
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")

#     for k in range(2*i+1):
#         print("*",end="")

#     print()

# n = 7 
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*(n - i) - 1):
#         print("*",end=""
#     print()


# n = 7
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print(i,end=" ")
#         elif i==j or i+j==n-1:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 5

# for i in range(1,n+1):
#     print("*" * i)
# for j in range(n-1,0,-1):
#     print("*"*j)


# n = 5
# for i in range(n+1):
#     print("*"*i)

# n = 5
# for i in range(n,0,-1):
#     print("*"*i)

# n = 7

# for i in range(1,n+1):
#     print("*"*i)
# for j in range(n-1,0,-1):
#     print("*"*j)


# n = 5

# for i in range(n):
#     for j in range(n):
#         if i==n//2 and j==n//2 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 5

# for i in range(n):
#     for j in range(n):
#         if i == 0 or j ==0 or i == n-1 or j == n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n = 5

# for i in range(n):
#     for j in range(n):
#         if i ==n//2 or j == n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n =5
# for i in range(n):
#     for j in range(n):
#         if i == j  or i+j == n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()


# n = 5 
# for i in range(1,n+1):
#     print(" "*(n-i) + "*"*i)


# n = 7
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()


# while True:
#     n = int(input("Enter Number: "))
#     for i in range(n):
#         for j in range(i):
#             print(" ",end="")
#         for k in range(2*(n-i)-1):
#             print("*",end="")
#         print()




N=3
for i in range(N):
    for s in range(N - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()

# Lower part (start from same index)
for i in range(N - 1, -1, -1):
    for s in range(N - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()