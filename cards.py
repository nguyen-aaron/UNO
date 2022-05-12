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
    elif topCard[1] == "R":
      print("RED")
    elif topCard[1] == "Y":
      print("YELLOW")
    elif topCard[1] == "B":
      print("BLUE")
    elif topCard[1] == "G":
      print("GREEN")