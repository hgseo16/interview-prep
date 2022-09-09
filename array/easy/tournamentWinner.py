competitions = [
    ['HTML', 'C#'],
    ['C#', 'Python'],
    ['Python', 'HTML']
]

results = [0, 0, 1]


# Time O(n) | Space O(k)
# n is the number of competitions and k is the number of teams

def tournamentWinner(competitions, results):
    scoreboard = {}
    winner = None
    topscore = 0


    for idx, val in enumerate(results):
        for team in competitions[idx]:
            if team not in scoreboard:
               scoreboard[team] = 0
        if val == 0:
            # away team [1] won
            scoreboard[competitions[idx][1]] += 3
            if scoreboard[competitions[idx][1]] > topscore:
                topscore = scoreboard[competitions[idx][1]]
                winner = competitions[idx][1]
        else:
            # home team [0] won
            scoreboard[competitions[idx][0]] += 3
            if scoreboard[competitions[idx][0]] > topscore:
                topscore = scoreboard[competitions[idx][0]]
                winner = competitions[idx][0]

    return winner

print(tournamentWinner(competitions, results))
