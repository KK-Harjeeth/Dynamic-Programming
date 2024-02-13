# Function to solve the problem
def solve():
    num_stones = 3
    num_colors = 3
    knapsack_size = 10
    dp = [[0] * 10005 for _ in range(105)]
    v = [[] for _ in range(105)]
    stone_weights = [1, 2, 3]
    stone_colors = [1, 2, 3]

    for i in range(num_stones):
        v[stone_colors[i]].append(stone_weights[i])

    for x in v[1]:
        dp[1][x] += 1

    for i in range(1, num_colors):
        for j in range(knapsack_size+1):
            if dp[i][j]:
                for x in v[i + 1]:
                    if j + x <= knapsack_size:
                        dp[i + 1][j + x] += 1

    ans = 0
    for j in range(1, knapsack_size+1):
        if dp[num_colors][j]:
            ans = max(ans, j)

    if ans == 0:
        print(-1)
    else:
        print(knapsack_size - ans)

# Main function
if __name__ == "__main__":
    solve()
