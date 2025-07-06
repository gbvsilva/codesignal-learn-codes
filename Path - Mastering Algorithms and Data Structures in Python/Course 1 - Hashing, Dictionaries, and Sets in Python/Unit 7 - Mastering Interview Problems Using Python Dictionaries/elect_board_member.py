from collections import defaultdict


def elect_board_member(votes):
    # implement this
    counter = defaultdict(int)
    for vote in votes:
        counter[vote] += 1
        if counter[vote] >= len(votes) / 3:
            return vote
    return -1


print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1
