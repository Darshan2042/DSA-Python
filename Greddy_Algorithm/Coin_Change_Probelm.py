# def coinchange(coins,target):
#     coins.sort(reverse=True)
#     c = 0
#     for coin in coins:
#         while coin < target:
#             target -= coin
#             c += 1
#     print(c)
# coins = [1,2,10,25]
# target = 65
# coinchange(coins,target)


coins  = [10,5,2,1]
amount = 25
c = 0
for coin in coins:
    if amount >= coin:
        c += amount // coin
        amount = amount % coin
print(c)


