print("Welcome to my computer quiz!")

playing=input("do you want to play?")

if playing.lower() != yes:
  quit()
print("Okay! let's play:)")
score = 0

answer=input("""What is the highest individual score ever recorded in Test cricket?""")
if answer.lower() == "400":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer=input("""In cricket, what is the term used to describe when a bowler dismisses a batsman with three consecutive deliveries?""")
if answer.lower() == "hat-trick":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer=input("""Which country won the ICC Cricket World Cup in 2019?""")
if answer.lower() == "England":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer=input("""Who holds the record for the fastest century in One Day International (ODI) cricket?""")
if answer.lower() == "AB de Villiers":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer=input("""What does LBW stand for in cricket?""")
if answer.lower() == "Leg Before Wicket(LBW)":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")
print("You got"+ str(score) + "questions correct!")
print("You got"+ str((score/4)*100) + "%.")
