numberofPlayers = 4
playerNameNumber = 0
def playerListLength(r1, r2):
  return list(range(r1, r2+1))

r1, r2 = 1, int(numberofPlayers)
playerList = playerListLength(r1, r2)

for x in range (0, int(numberofPlayers)):
  print("Player", playerNameNumber+1, "enter name:")
  playerList[playerNameNumber] = input("")
  playerNameNumber = playerNameNumber + 1

