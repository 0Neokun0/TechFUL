while True:
  try:
     userInput = int(input())     
  except ValueError:
     print("No")
     break
  else:
     print(userInput)
     break 