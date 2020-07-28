# choose a player to go and make it move 
# each player may take a step a head
# First one to 20 wins 

Score = 0

def function():
  P1 = str(input("WILL YOU GO FIRST OR SECOND ?"))
  if P1 ==  "first" :
    print(" Player 1 starts ")

def function2():
  P2 = input(" Enter 1 or 2 ")
  if P2 == "1":
    result = Score + 1
    print(result)
  if P2 == "2":
    result2 = Score + 2
    print(result2)

function()

while Score == 20:

  function2()
  P1 = input("Add 1 or 2 more to each move")
  P2 = input("Add 1 or 2 more to each move")
  N = int(P1) + int(P2)
  N = "Winner"
  print(N)



#Still in working progresss
