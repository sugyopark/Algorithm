def max_score(N, scores):
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = 0
    dp[0][1] = scores[0]

    if N > 1:
        dp[1][0] = scores[1]
        dp[1][1] = max(scores[0] + scores[1], scores[1])

    for i in range(2, N):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + scores[i]
        dp[i][1] = dp[i-1][0] + scores[i]

    return max(dp[N-1][0], dp[N-1][1])

def main():
    N = int(input("Enter the number of steps (N): "))
    scores = []
    for n in range(N):
        score = int(input(f"Enter the score for {n+1} step: "))
        scores.append(score)

    result = max_score(N, scores)
    print("Maximum score:", result)

main()


