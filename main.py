import math, random, time
from players import playerList
def cardGeneration():
  ## card list, 1st character is card value, 2nd character is card color
  ## S: skip 
  ## V: reverse 
  ## T: plus 2
  ## PF: plus 4 with color change
  ## CC: color change
  ## ex: SY = skip yellow, VB = reverse blue, TG = plus 2 green, etc.
  originalSet= ("0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","0Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","0B","1B","2B","3B","4B","5B","6B","7B","8B","9B","0G","1G","2G","3G","4G","5G","6G","7G","8G","9G","SR","SY","SB","SG","VR","VY","VB","VG","TR","TY","TB","TG","CC","PF")
  cards = ["0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","1R","2R","3R","4R","5R","6R","7R","8R","9R","0Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","0B","1B","2B","3B","4B","5B","6B","7B","8B","9B","1B","2B","3B","4B","5B","6B","7B","8B","9B","0G","1G","2G","3G","4G","5G","6G","7G","8G","9G","1G","2G","3G","4G","5G","6G","7G","8G","9G","SR","SR","SY","SY","SB","SB","SG","SG","VR","VR","VY","VY","VB","VB","VG","VG","TR","TR","TY","TY","TB","TB","TG","TG","CC","CC","CC","CC","PF","PF","PF","PF"]
  usedCards = []
  playerCards = []
  usedCards.append(cards.pop(random.randrange(0,75)))
  turn = 0
  displayCardNeeded = True
  isRunning = True
  reverse = False
  colorChangeInProgress = False

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

  while isRunning == True:
    if len(player1) and len(player2) and len(player3) and len(player4) != 0:
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
            elif topCard[0] == "P":
              print("PLUS FOUR")
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
          if turn == 0:
            print(player1)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player1 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn = 3
              displayCardNeeded = True
            elif cardPlayed in player1 and cardPlayed[0] == "T" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,2):
                  player2.append(cards.pop(random.randrange(len(cards))))
                  player2.sort()
              elif reverse == True:
                turn = 3
                for x in range (0,2):
                  player4.append(cards.pop(random.randrange(len(cards))))
                  player4.sort()
              displayCardNeeded = True
    
            elif cardPlayed in player1 and cardPlayed[0] == "R" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True:
                turn +=1
                reverse = False
              elif reverse == False:
                turn = 3
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player1 and cardPlayed[0] == "P" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,4):
                  player2.append(cards.pop(random.randrange(len(cards))))
                  player2.sort()
              elif reverse == True:
                turn = 3
                for x in range (0,4):
                  player4.append(cards.pop(random.randrange(len(cards))))
                  player4.sort()
              displayCardNeeded = True

            elif cardPlayed in player1 and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn = 3
              displayCardNeeded = True
            else:
              print("Invalid Card. Try Again.")
          elif turn == 1:
            print(player2)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player2 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player2.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn -=1
              displayCardNeeded = True
            elif cardPlayed in player2 and cardPlayed[0] == "T" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player2.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,2):
                  player3.append(cards.pop(random.randrange(len(cards))))
                  player3.sort()
              elif reverse == True:
                turn +=1
                for x in range (0,2):
                  player1.append(cards.pop(random.randrange(len(cards))))
                  player1.sort()
              displayCardNeeded = True
    
            elif cardPlayed in player2 and cardPlayed[0] == "R" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player2.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True:
                turn +=1
                reverse = False
              elif reverse == False:
                turn -=1
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player2 and cardPlayed[0] == "P" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player2.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,4):
                  player3.append(cards.pop(random.randrange(len(cards))))
                  player3.sort()
              elif reverse == True:
                turn -=1
                for x in range (0,4):
                  player1.append(cards.pop(random.randrange(len(cards))))
                  player1.sort()
              displayCardNeeded = True

            elif cardPlayed in player2 and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player2.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn -=1
              displayCardNeeded = True
            else:
              print("Invalid Card. Try Again.")
          elif turn == 2:
            print(player3)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player3 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn -=1
              displayCardNeeded = True
            elif cardPlayed in player3 and cardPlayed[0] == "T" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,2):
                  player4.append(cards.pop(random.randrange(len(cards))))
                  player4.sort()
              elif reverse == True:
                turn -=1
                for x in range (0,2):
                  player2.append(cards.pop(random.randrange(len(cards))))
                  player2.sort()
              displayCardNeeded = True
    
            elif cardPlayed in player3 and cardPlayed[0] == "R" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True:
                turn +=1
                reverse = False
              elif reverse == False:
                turn +=1
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player3 and cardPlayed[0] == "P" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,4):
                  player4.append(cards.pop(random.randrange(len(cards))))
                  player4.sort()
              else:
                turn -=1
                for x in range (0,4):
                  player2.append(cards.pop(random.randrange(len(cards))))
                  player2.sort()
              displayCardNeeded = True

            elif cardPlayed in player3 and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn -=1
              displayCardNeeded = True
            else:
              print("Invalid Card. Try Again.")
          elif turn == 3:
            print(player4)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player4 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn = 0
              else:
                turn -=1
              displayCardNeeded = True
            elif cardPlayed in player4 and cardPlayed[0] == "T" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn = 0
                for x in range (0,2):
                  player1.append(cards.pop(random.randrange(len(cards))))
                  player1.sort()
              else:
                turn -=1
                for x in range (0,2):
                  player3.append(cards.pop(random.randrange(len(cards))))
                  player3.sort()
              displayCardNeeded = True
    
            elif cardPlayed in player4 and cardPlayed[0] == "R" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True:
                turn +=1
                reverse = False
              elif reverse == False:
                turn = 0
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player4 and cardPlayed[0] == "P" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like change?").upper()
                if colorChange == "R":
                  print("RED")
                  colorChangeInProgress = False
                elif colorChange == "B":
                  print("BLUE")
                  colorChangeInProgress = False
                elif colorChange == "Y":
                  print("YELLOW")
                  colorChangeInProgress = False
                  False
                elif colorChange == "G":
                  print("GREEN")
                  colorChangeInProgress = False
                else:
                  print("Invlaid Color.")
              topCard = "x"+colorChange
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn = 0
                for x in range (0,4):
                  player1.append(cards.pop(random.randrange(len(cards))))
                  player1.sort()
              elif reverse == True:
                turn -=1
                for x in range (0,4):
                  player3.append(cards.pop(random.randrange(len(cards))))
                  player3.sort()
              displayCardNeeded = True

            elif cardPlayed in player4 and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn = 0
              else:
                turn -=1
              displayCardNeeded = True
            else:
              print("Invalid Card. Try Again.")
    else:
      if len(player1) == 0:
        print(playerList[0], "has won! UNO!")
      elif len(player2) == 0:
        print(playerList[1], "has won! UNO!")
      elif len(player3) == 0:
        print(playerList[2], "has won! UNO!")
      elif len(player4) == 0:
        print(playerList[3], "has won! UNO!")
      isRunning = False
  
def main():
  cardGeneration()
  while input("Would you like to play again? (Y/N)").upper() == "Y":
    cardGeneration()
main()


