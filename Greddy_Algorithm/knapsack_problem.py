def knapsack(profits , weights , capacity):
    items = []
    for i in range(len(profits)):
        ratio = profits[i] / weights[i]
        items.append((profits[i] , weights[i] , ratio))

    items.sort(key = lambda item: item[2] , reverse=True)

    total_profit = 0.0
    remianing_capacity = capacity

    for profit , weight ,ratio in items:
        if remianing_capacity == 0:
            break
        if weight <= remianing_capacity:
            total_profit += profit
    return total_profit

profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(knapsack(profits, weights, capacity))