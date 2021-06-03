#-- Author: Henok Tilahun
#-- Date:  6/3/2021
#-- Program: Cop V Killer text game

#- Functions
def start_room():
  start_room_option = ["1","2","3"]
  user_choice = ''
  while user_choice not in start_room_option:
    print('''Your name is Max. You just came back to work after a national holiday. You work in the FBI and your manager has called your whole team into the office. Confused and slightly excited, you make your way into the room. There you find that everyone else is already waiting for you. On the screen is a couple of murders. That's when you raelize what this is about. The dang killer. Again. Suddenly your excitement turns into dread as your superior starts talking about the case again. You've already memorized each murder with the frequency in which the killer was brought up. What do you do?
  
    1) Go on autopliot
    2) Listen intently''')

    user_choice = str(input("Enter Option Number: "))
  print ("You have selected " + user_choice)
  if user_choice == start_room_option[0]:
    room01
  elif user_choice == start_room_option[1]:
    room02
  e

start_room()