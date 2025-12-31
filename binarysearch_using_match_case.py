# def binary(arr,key):
#             if high < low:
#                 return -1
#             mid = (low + high)//2
#             if nums[mid]== target:
#                 return mid
#             elif nums[mid]<target:
#                 return bSearch(mid+1,high)
#             else:
#                 return bSearch(low,mid-1)	
#     return bSearch(0, len(nums) - 1)