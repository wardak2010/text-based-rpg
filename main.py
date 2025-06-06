# Text-Based RPG: Aliens of Akrabar
# Welcome user to the game and ask their name
name = input("Welcome to Aliens of Akrabar! What is your name? ")
print(f"Hi {name}! We hope you will enjoy the game. Here we go...\n" )

# Start game
# Decsribe the starting scene
print("You wake up on a spaceship. You don't know where you are. ")
print("a) [G]et out of bed.")
print("b) Go back to [s]leep.")
ans1 = input("Choice: ").lower().strip()

# Check their answer
if ans1 == "g":
    print("You get up and look around. There are 3 other beds. There are people in them.")
    print("[W]ake the other people.")
    print("[L]eave the room.")
    ans2 = input("Choice: ").lower().strip()
    
    if ans2 == "w":
        print("The people are dead. One of them begins to vomit green stuff.")
        print("[R}un.")
        print("Get a [m]op to clean up the mess.")
        ans3 = input("Choice: ").lower().strip()
        
    if ans3 == "r":
        print("You unfortunately ran out into space. You explode and die.")
    elif ans3 == "m":
        print("You start cleaning. The one person starts to sit up.")
        
        
    elif ans2 == "l":
        print("You accidently enter space and explode into lots of flesh chunks.")
    
elif ans1 == "s":
    print("You hypersleep for 1000 years, grow old, and die. ")
print("Thanks for playing! ")