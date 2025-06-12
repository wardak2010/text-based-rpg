# Text-Based RPG: The Hunger Games Survival
# Welcome user to the game and ask their name
name = input("Welcome to The Hunger Games Survival! What is your name? ")
print(f"Hi {name}! We hope you will enjoy the game. Here we go...\n" )

# Start game
# Decsribe the starting scene
print("You wake up in the 10th district of Panem on the morning of your twelfth birthday. Typically, this would be a day to celebrate with your friends and family, but that is not the case for you. This is the day you have been dreading since you were born, as you know that you are now officially old enough for your name to be enrolled in the draw to compete in The Hunger Games, a battle between 24 kids until only one survivor remains. The reaping ceremony, where tributes are chosen, is going to happen in two days.\n")
print("Start [t]raining.")
print("Ask your older sibling for [a]dvice.")
ans1 = input("Choice: ").lower().strip()

# Check their answer
if ans1 == "t":
    print("You brainstorm what skills you are required to learn and improve. You decide to try and improve your climbing, archery, combat, and first aid. You spend the next two days enhancing these skills so you are prepared for anything. It is now the day of the reaping.\n")
    print("Go with your sibling to the [c]eremony.")
    print("Stay at home and try to [a]void the ceremony altogether.")
    ans2 = input("Choice: ").lower().strip()
    
    if ans2 == "c":
        print("You go to the ceremony and find your spot beside the other twelve year olds. You notice the sweat dripping down their foreheads and the panicked look on their faces. This triggers a sense of alarm in you as well. The mayor starts welcoming everybody, then brings out the horrifying wheel with all the pieces of paper inside it. She picks out the first name, and shouts “Dax Varyn!” You see a pale boy walk slowly onto the stage. The next second, you hear another name being called. Oh wait, it’s yours. You freeze.\n")
        print("Run [f]ar away.")
        print("Get onto the [s]tage.")
        ans3 = input("Choice: ").lower().strip()
        
        if ans3 == "f":
            print("You bolt as fast as you can, but three peacekeepers quickly catch up to you and grab you by the arms. They take you to a nearby prison as a penalty. There is no escaping now. You spend the rest of your years in this prison until you die. That’s unfortunate…\n")
            print("Thanks for playing! ")
            
        elif ans3 == "s":
            print("You get onto the stage as the crowd applauds you. The ceremony concludes, and you get taken into a room. You get to see your family for two minutes. Tears in your eyes, you tell them to root for you if  you have any chance of surviving this. The doors close and you get taken into a room. One week passes, and it is now time for the games to start. You stand on your plate as the clock counts ten seconds.\n")
            print("Get off the plate [e]arly to get a headstart.")
            print("Wait for the [h]orn signaling to start.")
            ans4 = input("Choice: ").lower().strip()
            
            if ans4 == "e":
                print("You step off the plate before the timer is over and get blown to bits immediately. Pieces of you are everywhere. Oh well…\n")
                print("Thanks for playing! ")
                
            elif ans4 == "h":
                print("You step off as soon as the horn blows. Everything is all over the place, with some people running far away, some going to the middle to get weapons, and some staying put on their plate.\n")
                print("[R]un into the woods.")
                print("Go to the middle to get [w]eapons.")
                ans5 = input("Choice: ").lower().strip()
                
                if ans5 == "r":
                    print("You sprint into the woods and spot a backpack on the floor. Regardless of knowing what’s inside, you pick it up and keep running until you find a tall tree. Using the tree climbing skills you practiced earlier, you quickly climb to the top to protect yourself from other tributes. You open the backpack and see it is stocked with food. You let out a sigh of relief. You stay safe on the tree for three days straight until you run out of food. There are only three tributes left. You climb down and spot some berries.You are starving.\n")
                    print("[E]at a few.")
                    print("[D]on’t eat them.")
                    ans6 = input("Choice: ").lower().strip()
                    
                    if ans6 == "e":
                        print(f"You place one into your mouth, and quickly notice your throat tightening up. Unfortunately, you just ate poison berries. You feel a burning sensation take over your body until you collapse onto the floor and die a painful death. You were so close {name}…\n")
                        print("Thanks for playing! ")
                        
                    elif ans6 == "d":
                        print("You decide not to eat them, and wait it out instead. You climb back up your tree and take a nap for what seems like a few hours. You suddenly wake up to the sound of music blasting in your ears. You hear the words “I pronounce you our final standing tribute!” There are no tributes left. You are the winner! You successfully made it out of the arena. Well done!\n")
                        print(f"Good job {name}! You have survival instincts! Thanks for playing! ")
                    
                elif ans5 == "w":
                    print("You run as fast you possibly can into the middle, hoping to get armed as soon as possible. However, you unfortunately face another tribute who creeps up behind you and takes an aggressive swing at your head with a wooden bat. You fall to the floor, and they continue to whack you with the bat. You soon die from the trauma to your body. Maybe you should’ve gone to the woods instead.\n")
                    print("Thanks for playing! ")
                    
                else:
                    print("Not an option...you lose.")
                    print("Thanks for playing! ")
                    
                    
                    
            else:
                print("Not an option...you lose.")
                print("Thanks for playing! ")
    
        else:
            print("Not an option...you lose.")
            print("Thanks for playing! ")

    elif ans2 == "a":
        print("You stay at home, hoping no one will notice. An hour goes by and you hear a bang on your front door. You answer the door and see two Capitol controlled guards, called peacekeepers. They drag you out the door, and you struggle to free yourself from their firm grip. Through the train, they take you to the Capitol’s head office. You are told you will now work as a peacekeeper for your penalty, and will never see your loved ones again. You should’ve just gone to the ceremony…\n")
        print("Thanks for playing! ")
        
    else:
        print("Not an option...you lose.")
        print("Thanks for playing! ")
        
elif ans1 == "a":
    print(f"You go to your sibling’s room knowing that they have never been drawn for the games, so they may not be too helpful. Regardless, you ask them for advice, and just as you expected they tell you they don’t know anything about the games. You go to the reaping ceremony two days later in a panic, but the mayor calls out two names, and they aren’t yours. You didn’t get picked. You didn't compete in the Hunger Games after all {name}. Let’s hope you get the same luck next year…\n")
    print("Thanks for playing! ")
        
else:
    print("Not an option...you lose.")
    print("Thanks for playing! ")

        

    
