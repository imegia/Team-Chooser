from random import choice

players = ["Harry", "Hermione", "Neville", "Ginny"]
print("Players:", players)

teamA = []
teamB = []

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

print("Team A:", teamA)
print("Team B:", teamB)
