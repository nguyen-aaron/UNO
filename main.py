import random
from players import playerList
def game():
  ## card list, 1st character is card value, 2nd character is card color
  ## Color Index:
  ## R = RED
  ## Y = YELLOW
  ## B = BLUE
  ## G = GREEN
  ## Type Index:
  ## S: SKIPx
  ## V: REVERSE 
  ## T: PLUS 2
  ## PF: PLUS 4 WITH COLOR CHANGE
  ## CC: COLOR CHANGE
  ## ex: SY = skip yellow, VB = reverse blue, TG = plus 2 green, etc.
  originalSet= ("0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","0Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","0B","1B","2B","3B","4B","5B","6B","7B","8B","9B","0G","1G","2G","3G","4G","5G","6G","7G","8G","9G","SR","SY","SB","SG","VR","VY","VB","VG","TR","TY","TB","TG","CC","PF")
  cards = ["0R","1R","2R","3R","4R","5R","6R","7R","8R","9R","1R","2R","3R","4R","5R","6R","7R","8R","9R","0Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","1Y","2Y","3Y","4Y","5Y","6Y","7Y","8Y","9Y","0B","1B","2B","3B","4B","5B","6B","7B","8B","9B","1B","2B","3B","4B","5B","6B","7B","8B","9B","0G","1G","2G","3G","4G","5G","6G","7G","8G","9G","1G","2G","3G","4G","5G","6G","7G","8G","9G","SR","SR","SY","SY","SB","SB","SG","SG","VR","VR","VY","VY","VB","VB","VG","VG","TR","TR","TY","TY","TB","TB","TG","TG","CC","CC","CC","CC","PF","PF","PF","PF"]
  usedCards = []
  playerCards = []
  usedCards.append(cards.pop(random.randrange(0,75))) # generate a random first card
  turn = 0
  displayCardNeeded = True
  isRunning = True
  reverse = False
  colorChangeInProgress = False

  player1 = [] # randomly generate 7 cards for each player
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
    if len(player1) and len(player2) and len(player3) and len(player4) != 0: # if nobody has 0 cards
      topCard = str(usedCards[-1]) # topCard will be the last item appended in the used cards list (top of the card pile)
      if len(cards) != 0: #if there are cards that can still be drawn
        if displayCardNeeded == True: #if the topCard needs to be displayed
          if topCard[0].isdigit(): #use indexing to figure out how to print the top card out in words
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
          displayCardNeeded = False # once the topCard is displayed, set displayCardNeeded to False
        elif displayCardNeeded == False: # if displayCardNeeded is false
          if turn == 0: # if it is the first player's turn
            print(player1) #print player1's cards
            print(playerList[turn], "what card would you like to play?") # get input from player1
            cardPlayed = input("").upper()
            if cardPlayed in player1 and cardPlayed[0] == "C" and cardPlayed in originalSet: # if player1 plays color change
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like to change to?").upper() # get input from player1
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
              usedCards.append(cardPlayed) # add the cardPlayed to the usedCards pile
              player1.remove(cardPlayed) # remove the cardPlayed from player1's card list
              print("Playing", cardPlayed) #print the cardPlayed
              if reverse == False: #if the order is not reversed, go to the next person
                turn +=1
              else: #if the order is reversed, go to the previous person
                turn = 3
              displayCardNeeded = True # set displayCardNeeded to be true to display the top card again
              
            elif cardPlayed in player1 and cardPlayed[0] == "T" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet: # if player1 plays a plus two card
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
                for x in range (0,2): # add two cards to the next player
                  player2.append(cards.pop(random.randrange(len(cards))))
                  player2.sort()
              elif reverse == True:
                turn = 3
                for x in range (0,2): # add two cards to the previous player
                  player4.append(cards.pop(random.randrange(len(cards))))
                  player4.sort()
              displayCardNeeded = True
              
            elif cardPlayed in player1 and cardPlayed[0] == "S" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet: # if player1 plays a skip
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False: # add 2 to turn order and skip next player
                turn +=2
              elif reverse == True:
                turn = 2
              displayCardNeeded = True   
              
            elif cardPlayed in player1 and cardPlayed[0] == "V" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet: #if player1 plays a reverse card
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True: # set reverse order to false if it was previously true
                turn +=1
                reverse = False
              elif reverse == False: # set reverse order to true if it was previously false
                turn = 3
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player1 and cardPlayed[0] == "P" and cardPlayed in originalSet: # if player1 plays a plus four card
              colorChangeInProgress = True 
              while colorChangeInProgress == True: # get user input for color
                colorChange = input("What color would you like to change to?").upper()
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
                for x in range (0,4): # add 4 cards to next player who has next turn
                  player2.append(cards.pop(random.randrange(len(cards))))
                  player2.sort()
              elif reverse == True:
                turn = 3
                for x in range (0,4):
                  player4.append(cards.pop(random.randrange(len(cards))))
                  player4.sort()
              displayCardNeeded = True

            elif cardPlayed in player1 and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet: # if player1 plays a card that is the same color or type
              usedCards.append(cardPlayed)
              player1.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=1
              else:
                turn = 3
              displayCardNeeded = True
            elif cardPlayed == "DRAW": # if player1 needs to draw
              player1.append(cards.pop(random.randrange(len(cards)))) # add a random card to player1's list
              print("Drawing",player1[-1]) # print the new card they get
              player1.sort() # sort cards again
            else:
              print("Invalid Card. Try Again.") # if user input does not match anything, it must be an invalid card
              
          elif turn == 1:
            print(player2)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player2 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like to changeto?").upper()
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

            elif cardPlayed in player2 and cardPlayed[0] == "S" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player2.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn +=2
              elif reverse == True:
                turn = 3
              displayCardNeeded = True
    
            elif cardPlayed in player2 and cardPlayed[0] == "V" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
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
                colorChange = input("What color would you like to change to?").upper()
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
            elif cardPlayed == "DRAW":
              player2.append(cards.pop(random.randrange(len(cards))))
              print("Drawing",player2[-1])
              player2.sort()
            else:
              print("Invalid Card. Try Again.")
          elif turn == 2:
            print(player3)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player3 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like to change to?").upper()
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
            elif cardPlayed in player3 and cardPlayed[0] == "S" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn = 0
              elif reverse == True:
                turn = 0
              displayCardNeeded = True
              
            elif cardPlayed in player3 and cardPlayed[0] == "V" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player3.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True:
                turn +=1
                reverse = False
              elif reverse == False:
                turn -=1
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player3 and cardPlayed[0] == "P" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like to change to?").upper()
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
            elif cardPlayed == "DRAW":
              player3.append(cards.pop(random.randrange(len(cards))))
              print("Drawing",player3[-1])
              player3.sort()
            else:
              print("Invalid Card. Try Again.")
          elif turn == 3:
            print(player4)
            print(playerList[turn], "what card would you like to play?")
            cardPlayed = input("").upper()
            if cardPlayed in player4 and cardPlayed[0] == "C" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like to change to?").upper()
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
              
            elif cardPlayed in player4 and cardPlayed[0] == "S" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == False:
                turn = 1
              elif reverse == True:
                turn = 1
              displayCardNeeded = True
              
            elif cardPlayed in player4 and cardPlayed[0] == "V" and (topCard[0] == cardPlayed[0] or topCard[1] == cardPlayed[1]) and cardPlayed in originalSet:
              usedCards.append(cardPlayed)
              player4.remove(cardPlayed)
              print("Playing", cardPlayed)
              if reverse == True:
                turn = 0
                reverse = False
              elif reverse == False:
                turn -=1
                reverse = True
              displayCardNeeded = True
                  
            elif cardPlayed in player4 and cardPlayed[0] == "P" and cardPlayed in originalSet:
              colorChangeInProgress = True
              while colorChangeInProgress == True:
                colorChange = input("What color would you like to change to?").upper()
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
            elif cardPlayed == "DRAW":
              player4.append(cards.pop(random.randrange(len(cards))))
              print("Drawing",player4[-1])
              player4.sort()
            else:
              print("Invalid Card. Try Again.")    
      elif len(cards) == 0:
        cards.extend(usedCards)
        usedCards.clear()
    else:
      if len(player1) == 0:
        print(playerList[0], "has won!")
      elif len(player2) == 0:
        print(playerList[1], "has won!")
      elif len(player3) == 0:
        print(playerList[2], "has won!")
      elif len(player4) == 0:
        print(playerList[3], "has won!")
      isRunning = False
  
def main():
  game()
  while input("Would you like to play again? (Y/N)").upper() == "Y":
    game()
main()


