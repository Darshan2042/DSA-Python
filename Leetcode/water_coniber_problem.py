# approach Two Pointer 
def water(height):
    start = 0
    end = len(height) -1
    max_value = 0
    while start < end:
        length = end - start
        bridth = min(height[start], height[end])
        Area = length * bridth
        max_value = max(max_value,Area)
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return max_value

height = [1,8,6,2,5,4,8,3,7]
print(water(height))