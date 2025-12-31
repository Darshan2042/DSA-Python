def seconf_highest_number(arr):
    if len(arr) < 2:
        return None
    s = sorted(arr  , reverse=True)
    print(s)
    return s[1]

array = [10,50,50,440,90,50,10,220,30,]

d = seconf_highest_number(array)
print(f"The Second Highest number is{d}")