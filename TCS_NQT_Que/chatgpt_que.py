def chatgpt(s):
    consent = 0
    vowels = 0
    digits = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consent +=1
        if ch.isdigit():
            digits +=1
    
    print("count of consent:",consent)
    print("count of vowles:",vowels)
    print("count of Digits:",digits)

s = input()
chatgpt(s)