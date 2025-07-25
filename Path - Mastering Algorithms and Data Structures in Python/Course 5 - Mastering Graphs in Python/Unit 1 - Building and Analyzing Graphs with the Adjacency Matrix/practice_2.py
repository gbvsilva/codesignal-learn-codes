# Trying to unearth possible friends within our social network
# We have 6 people at a party. A knows everybody, yet E is a bit shy and only knows A.

# A: 0, B: 1, C: 2, D: 3, E: 4, F: 5,
# Let's put this into an adjacency matrix

# Number of people
n = 6
users = ['A', 'B', 'C', 'D', 'E', 'F']

# Initialize the adjacency matrix
M = [[0] * n for _ in range(n)]

# Map the relationships
# A knows B, C, D, E, F
M[0][1] = M[0][2] = M[0][3] = M[0][4] = M[0][5] = 1

# B, C, D, E, F know A
M[1][0] = M[2][0] = M[3][0] = M[4][0] = M[5][0] = 1
M[1][4] = M[4][1] = 1

# Print the Graph
for row in range(n):
    print(M[row])

# Suggest friends for each user, avoiding cases where users are suggested to be friends with themselves
for i in range(n):
    for j in range(n):
        if i != j:
            if M[i][j] == 0 and any(M[i][k] and M[k][j] for k in range(n)):
                print(
                    f"Based on mutual friends, "
                    f"User {users[i]} and User {users[j]} might know each other."
                )
