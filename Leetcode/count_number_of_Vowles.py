string = "Hello My name is darshan"
def words(string):
    count = 0
    vowels = "AEIOUaeiou"
    for ch in string:
        if ch in vowels:
            count += 1
    return count
print(words(string))
