

def count_well_formed_parenthesis(n_couples: int) -> int:
    dp = [0] * (n_couples + 1)
    dp[0] = 1
    for i in range(1, n_couples + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    return dp[n_couples]

if __name__ == "__main__":
    for n in range(1, 16):
        print(f"n = {n}: {count_well_formed_parenthesis(n)}")