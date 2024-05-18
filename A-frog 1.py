def afrog():
    n = int(input())
    stones = list(map(int, input().split()))

    dp = [0] * n
    dp[n-2] = abs(stones[n-2] - stones[n-1])

    for i in range(n-3, -1, -1):

        dp[i] = min(abs(stones[i] - stones[i+1]) + dp[i+1], abs(stones[i] - stones[i+2]) + dp[i+2])

    print(dp[0])

afrog()
