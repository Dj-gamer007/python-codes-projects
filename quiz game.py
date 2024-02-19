print("Welcome to my computer quiz!")

playing=input("do you want to play?")

if playing != yes:
  quit()
print("Okay! let's play:)")

answer=input("""What is the highest individual score ever recorded in Test cricke?""")
if answer == "400":
  print("Correct!")
else:
  print("Incorrect!")

answer=input("""In cricket, what is the term used to describe when a bowler dismisses a batsman with three consecutive deliveries?""")
if answer == "hat-trick":
  print("Correct!")
else:
  print("Incorrect!")

answer=input("""Which country won the ICC Cricket World Cup in 2019?""")
if answer == "England":
  print("Correct!")
else:
  print("Incorrect!")

answer=input("""Who holds the record for the fastest century in One Day International (ODI) cricket?""")
if answer == "AB de Villiers":
  print("Correct!")
else:
  print("Incorrect!")

answer=input("""What does LBW stand for in cricket?""")
if answer == "Leg Before Wicket(LBW)":
  print("Correct!")
else:
  print("Incorrect!")
