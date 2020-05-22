'''
Created on Mar 7, 2020

@author: ITAUser
'''

keepPlaying = True

while keepPlaying == True:
    print("Welcome to Blackjack!\n\nYour goal is to make 21. You will have to type either Hit or Stand. If you Hit, you will be given another number, if you Stand, you will not.\nIf you exceed 21, you lose, but you want to get as close to 21 as possible.\n")
    
    import random
    import time
    
    player1 = 0
    player2 = 0
    dealer = 0
    p1 = True

    
    numPlayers = input("How many players are playing? (1 or 2?): ")
    
    if numPlayers == "1":
        player1 = (random.randint(1,11))
        dealer = (random.randint(5,11))
        print("\nYou got " + str(player1))
        print("The dealer got " + str(dealer))
        while (player1 <= 21):
            hitStand1 = input("Would you like to Hit or Stand?\n")
            if hitStand1 == ("hit" or "Hit"):
                player1 = player1 + random.randint(1,11)
                print("You now have: " + str(player1))
            else:
                print("You have: " + str(player1))
                break
        dealer = dealer + random.randint(6,10)
        print("The dealer now has: " + str(dealer))
        if player1 <= 21:
            if player1 > dealer:
                print("Congrats! You won!\nYou had: " + str(player1) + "\nThe dealer had: " + str(dealer))
                time.sleep(5)
                keepPlaying = False
            else:
                print("Oh no... you lost. Better luck next time!")
                time.sleep(3)
                keepPlaying = False
        else:
            print("Oh no! You went over 21... better luck next time!")
            time.sleep(3)
            keepPlaying = False
    elif(numPlayers == "2"):
        player1 = (random.randint(1,11))
        player2 = (random.randint(1,11))
        dealer = (random.randint(5,11))
        print("\nPlayer1 has " + str(player1))
        print("Player2 has " + str(player2))
        print("The dealer got " + str(dealer))
        p1 = True
        while (player1 <= 21):
            hitStand1 = input("Would you like to Hit or Stand, Player1?\n")
            if ((hitStand1 == ("hit" or "Hit")) and (p1 == True)):
                player1 = player1 + random.randint(1,11)
                print("Player1 has: " + str(player1))
            else:
                print("Player1 has: " + str(player1))
                break
        while (player2 <= 21):
            p1 = False
            hitStand2 = input("Would you like to Hit or Stand, Player2?\n")
            if hitStand2 == ("hit" or "Hit"):
                player2 = player2 + random.randint(1,11)
                print("Player2 has: " + str(player2))
            else:
                print("Player2 has: " + str(player2))
                break
        dealer = dealer + random.randint(6,10)
        print("The dealer now has: " + str(dealer))
        if (player1 <= 21) and (player2 <= 21):
            if (player1 > dealer) and (player1 >= player2):
                print("Congrats, Player1!\nYou had: " + str(player1) + "\nThe dealer had: " + str(dealer) + " \nPlayer2 had: " + str(player2))
                time.sleep(5)
                keepPlaying = False
            elif((player2 > dealer) and (player2 >= player1)):
                print("Congrats, Player2!\nYou had: " + str(player2) + "\nThe dealer had: " + str(dealer) + " \nPlayer1 had: " + str(player1))
                time.sleep(5)
                keepPlaying = False
            else:
                print("Oh no! The dealer won... -_-")
                time.sleep(5)
                keepPlaying = False
    else:
        print("Not a valid input.")
        keepPlaying = False
        time.sleep(3)
        keepPlaying = True
        
    keepPlaying = False
    
