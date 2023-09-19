A40 Demons and the Princess

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Input Format

The First line conatains two integers denoting the value of n and m respectively The Next N lines contains M integers denoting the value of the elements of matrix.

Constraints

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
Output Format

Print a integer which is the answer to the question

Sample Input 0

3 3
-2 -3 3
-5 -10 1
10 30 -5
Sample Output 0

7
Sample Input 1

4 4
946 655 453 72
73 708 387 749
-73 491 432 683
109 611 490 919
Sample Output 1

1

Solution:

def calculateMinimumHP(dungeon):
    if not dungeon:
        return 0

    m, n = len(dungeon), len(dungeon[0])

    dp = [[0] * n for _ in range(m)]

    # Calculate the minimum initial health needed for the princess cell
    dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

    # Calculate the last row
    for i in range(n - 2, -1, -1):
        dp[-1][i] = max(dp[-1][i + 1] - dungeon[-1][i], 1)

    # Calculate the last column
    for i in range(m - 2, -1, -1):
        dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)

    # Calculate the remaining cells
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_on_exit = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(min_on_exit - dungeon[i][j], 1)

    return dp[0][0]

# Input
n, m = map(int, input().split())
dungeon = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = calculateMinimumHP(dungeon)
print(result)

