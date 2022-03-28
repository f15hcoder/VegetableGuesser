print("Pick either Carrot, Broccoli, Peas or Sweetcorn")
print("I will attempt to guess your choice.")
print("Is this vegetable green?")
answer = input().lower()
if answer == "y":
  print("Does the vegetable look like a tree?")
  answer = input().lower()
  if answer == "y":
    print("It must be a Broccoli!")
  else:
    print("It must be a Peas!")
else: 
  print("Is this vegetable yellow?")
  answer = input().lower()
  if answer == "y":
    print("It must be a Sweetcorn!")
  else:
    print("It must be a Carrot!")