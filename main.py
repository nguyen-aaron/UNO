import math, random, time
from players import playerList
def main():
  ## card list, 1st character is card value, 2nd character is card color
  ## S: skip 
  ## V: reverse 
  ## T: plus 2
  ## PF: plus 4 with color change
  ## CC: color change
  ## ex: SY = skip yellow, VB = reverse blue, TG = plus 2 green, etc.
  displayCardNeeded = True
  gameisRunning = True
  usedCards = []
  playerCards= []
  playersToCards = {}
  turn = 0
  cards = ["0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","1R","2R","3R","4R","5R","6R","7R","8R","9R","OY","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","0B","1B","2B","3B","4B","5B","6B","7B","8B","9B","1B","2B","3B","4B","5B","6B","7B","8B","9B","0G","1G","2G","3G","4G","5G","6G","7G","8G","9G","1G","2G","3G","4G","5G","6G","7G","8G","9G","SR","SR","SY","SY","SB","SB","SG","SG","VR","VR","VY","VY","VB","VB","VG","VG","TR","TR","TY","TY","TB","TB","TG","TG","CC","CC","CC","CC","PF","PF","PF","PF"]

  player1 = []
  for x in range (0,7):
    player1.append(cards.pop(random.randrange(len(cards))))
  player1.sort()

  player2 = []
  for x in range (0,7):
    player2.append(cards.pop(random.randrange(len(cards))))
  player2.sort()

  player3 = []
  for x in range (0,7):
    player3.append(cards.pop(random.randrange(len(cards))))
  player3.sort()

  player4 = []
  for x in range (0,7):
    player4.append(cards.pop(random.randrange(len(cards))))
  player4.sort()

  player5 = []
  for x in range (0,7):
    player5.append(cards.pop(random.randrange(len(cards))))
  player5.sort()
  
  player6 = []
  for x in range (0,7):
    player6.append(cards.pop(random.randrange(len(cards))))
  player6.sort()
  #get a random card from the deck to play with
  usedCards.append(cards.pop(random.randrange(len(cards))))
    
  while gameisRunning == True:

    playerCards = player1 + player2 + player3 + player4 + player5 + player6
    print(usedCards)
    topCard = str(usedCards[-1])

    if (len(usedCards) + len(playerCards)) < 108:
      if displayCardNeeded == True:
        if topCard[0].isdigit():
          print(topCard[0])
        elif topCard[0].isalpha():
          if topCard[0] == "S":
            print("SKIP")
          elif topCard[0] == "V":
              print("REVERSE")
          elif topCard[0] == "T":
            print("PLUS TWO")
          elif topCard[0] == "C":
            print("COLOR CHANGE")
        if topCard[1] == "R":
          print("RED")
        elif topCard[1] == "Y":
          print("YELLOW")
        elif topCard[1] == "B":
          print("BLUE")
        elif topCard[1] == "G":
          print("GREEN")
        displayCardNeeded = False

      elif displayCardNeeded == False:
        if turn < len(playerList):
          print(playerList[turn], "what card would you like to play?")
          carPlayed = input("")
          if carPlayed in playerList
          turn = turn + 1
          displayCardNeeded = True
          
        else:
          turn = 0
          print(playerList[turn], "what card would you like to play?")
          cardPlayer = input("")
          turn = turn + 1
          displayCardNeeded = True

if __name__ == "__main__":
    main()