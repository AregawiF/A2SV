def afrog():
    n, k = map(int, input().split())
    stones = list(map(int, input().split()))

    dp = [0] * n
    dp[n-2] = abs(stones[n-2] - stones[n-1])

    for i in range(n-3, -1, -1):
        val = float('inf')
        for j in range(1, k+1):
            if i+j < n:
                val = min(val, abs(stones[i] - stones[i+j]) + dp[i+j]) 
            else:
                break
        dp[i] = val
    print(dp[0])

afrog()
