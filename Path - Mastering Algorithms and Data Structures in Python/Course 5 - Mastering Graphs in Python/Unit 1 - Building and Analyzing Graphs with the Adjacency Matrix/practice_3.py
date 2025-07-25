# Number of friends
n = 5
users = ['Alice', 'Bob', 'Carol', 'David', 'Emma']

# Initialize the adjacency matrix
M = [[0] * n for _ in range(n)]

# Add relationships in the adjacency matrix
# Alice
M[0][1] = M[0][3] = M[0][4] = 1
# Bob
M[1][0] = M[1][2] = M[1][3] = 1
# Carol
M[2][1] = 1
# David
M[3][0] = M[3][1] = M[3][4] = 1
# Emma
M[4][0] = M[4][3] = 1

# Print the adjacency matrix
for row in M:
    print(row)

# Suggest friends for each user, avoiding cases where users are suggested to be friends with themselves
for i in range(n):
    for j in range(n):
        if i != j:
            if M[i][j] == 0 and any(M[i][k] and M[k][j] for k in range(n)):
                print(
                    f"Based on mutual friends, "
                    f"User {users[i]} and User {users[j]} might know each other."
                )
