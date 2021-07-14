#CrimsoN
#Casino program

import random
import time
#imports^^



print("Welcome to the Casino")



def start():
    game=input("\n"+"Would you like to do Roulette, the Bandit machines or leave?: ").lower()#lower() makes first letter lowercase
    if game=="roulette":
        roulette()#calls roulette
    elif game=="bandit machines":
        bandit()#calls bandit
    elif game=="leave":
        print("Goodbye")
    else:
        print("\n"+"Sorry that is not an option")
        print("Please enter either Roulette or Bandit machines")
        start()#restarts function



        
def rouletteQ():
    question1=input("Do you want to play roulette again? Y/N: ").lower()
    if question1=="y" or question1=="yes":#or means it only has to meet one of the two requirements to run
        roulette()#calls roulette
    else:
        start()#calls start function



        
def banditQ():
    question2=input("\n"+"Do you want to play Bandit machines again? Y/N: ")
    if question2=="y" or question2=="yes":
        bandit()#calls bandit
    else:
        start()#calls start function



        
def roulette():
    user69=input("Pick either: black (40% chancec), red (40% chance) or green (20% chance): "+"\n").lower()
    roulette1=random.choice(["red","red","red","red","black","black","black","black","green","green"])#picks from the list its presented with
    print("It landed on", roulette1)
    if user69=="red" and roulette1=="red":
        print("Congrats you got it"+"\n")#\n is new line
    elif user69=="green" and roulette1=="green":
        print("Congrats you got it"+"\n")
    elif user69=="black" and roulette1=="black":
        print("Congrats you got it"+"\n")
    else:
        print("RIP you guessed wrong"+"\n")
    rouletteQ()#calls rouletteQ 



    
def bandit():
    user=input("Press enter to start....."+"\n")
    list1=random.choice(["Orange","Bannana","Apple"])#picks random from the 3 fruits
    list2=random.choice(["Orange","Bannana","Apple"])#picks random from the 3 fruits
    list3=random.choice(["Orange","Bannana","Apple"])#picks random from the 3 fruits
    print(list1)
    time.sleep(0.5)#pause .5 seconds
    print(list2)
    time.sleep(0.5)#pause .5 seconds
    print(list3)
    time.sleep(0.5)#pause .5 seconds
    print("\n")
    if list1==list2 and list1==list3:#and means it has to meet both requirements
        print("You win"+"\n")
    else:
        print("Unlucky"+"\n")
    banditQ()#calls banditQ function



    
start()#starts the program

