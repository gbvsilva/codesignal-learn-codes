# Define a function that takes three parameters: team_name, goals_scored, and goals conceded
def print_match_results(team_name, goals_scored, goals_conceded):

    if goals_scored == goals_conceded:
        result = "tie"
    elif goals_scored > goals_conceded:
        result = "won"
    else:
        result = "lost"

    print(f"{team_name} {result} the match with a score of {goals_scored}-{goals_conceded}")

matches_info = [("Team A", 3, 1), ("Team B", 1, 2), ("Team C", 0, 0)]

for match in matches_info:
    print_match_results(match[0], match[1], match[2])
