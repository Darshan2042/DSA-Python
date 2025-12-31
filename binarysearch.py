# def binary(arr,key):
#     low  = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if ( arr[mid] == key):
#             return mid
#         elif arr[mid] < key:
#             low = mid + 1
#         else :
#             high = mid - 1
#     return -1

# arr = [12,15,32,45,85,96]
# key = int(input("Enter The Number: "))
# b = binary(arr,key)

# if b == None:
#     print("absent")
# else:
#     print("present" ,b)


# arr = [12,45,65,55,65,45,78,45,41,45,2,5]
# key = int(input("Enter key: "))
# def linear(arr ,key):
#     for i in range(len(arr)):
#         if (arr[i] == key):
#             return i 
#     return -1
# s = linear(arr ,key)
# if s == None:
#     print("absent")
# else :
#     print("present" , s)

# def min_mix(arr):
#     minimum = min(arr)
#     maximum = max(arr)
#     return minimum, maximum

# arr = [12, 45, 65, 55, 78, 41, 2, 5]
# print("Min and Max:", min_mix(arr))


# def palindrome(n):
#     original = n
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev*10 + digit
#         n = n // 10

#     return original == rev

# n = 1234
# if palindrome(n):
#     print("Yes")
# else:
#     print("No")

