"""
Given a lowercase string s:
1. Keep only the first occurrence of each character.
2. Remove all later duplicates.
3. From the remaining characters:
   - Put all vowels (a, e, i, o, u) first, sorted.
   - Then put all consonants, sorted.
Return the final transformed string.
"""

def transfrom_sting(s):
    seen = set()
    unique_ch = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            unique_ch.append(ch)
    vowles = []
    con = []
    vowles_li = ['a','e','i','o','u']
    for ch in unique_ch:
        if ch in vowles_li:
            vowles.append(ch)
        else:
            con.append(ch)
    vowles.sort()
    con.sort()
    return "".join(vowles + con)

print(transfrom_sting("ahkgfykfncqkbdvoquebv"))