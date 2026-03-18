# Permutations in which N people can occupy R seats in a classroom.
########### CHAT-GPT Copy ###############
def permutation(n, r):
    result = 1
    for i in range(r):
        result *= (n - i)
    return result


print(permutation(5, 3))