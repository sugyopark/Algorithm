def max_score(N, scores):
    if N == 1:
        return scores[0]
    
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = scores[0]  
    dp[0][1] = scores[0]

    if N > 1:
        dp[1][0] = scores[1]
        dp[1][1] = scores[0] + scores[1]

    for i in range(2, N):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + scores[i]
        dp[i][1] = dp[i-1][0] + scores[i]

    return max(dp[N-1][0], dp[N-1][1])

N = 6
scores = [10, 20, 15, 25, 10, 20]
print(max_score(N, scores))