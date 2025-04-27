W, n = map(int, input().split())
weights = list(map(int, input().split()))

def find_max(W, weights):
    n = len(weights)
    dp = [0] * (W + 1) # массив где будем хранить максимальный вес золота

    for i in weights:
        for j in range(W, i - 1, -1):
            dp[j] = max(dp[j], dp[j - i] + i) # максимум из текущей максимальной вместимости и вместимости если можем добавить ещё слиток
    return dp[W]

print(find_max(W, weights))
