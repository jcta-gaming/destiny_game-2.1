from asyncore import loop
import random

happiness = 5

UserChoice = 'k'

def Eating():
  'a' 
  
def rides():
  'a'

print("press 'c' to continue diologue")

print(input("yo whats good bro took you a while to get here you gonna have to get your tickets over there ok!"))

print("ok see you in a sec")

player_name = input("welcome to the carnival whats your name: ") 

print("\n ok great", player_name, "welcome to this carnival we have rides to the left and and food to the rights and with you deposite of $20 you will get 40 tickets have fun and enjoy your time with us")

rules = """
************************************************************
*                happines levle = 5                        *
*    your goal is to not get lower than 0                  *
* each choice you make encreases or decreases you happines *
************************************************************
""";
print(rules);

info = input("if you understand press 'C' to continue if you want more info press 'M' for more info\n")

if(info.lower() == 'm'):
  print("the game will ask you choices while your character is in the carnival it can range from a simple question like would you like to eat to a more complex question like wich ride you want to go on and depending on your choices your happines levle will eather go up or down if it goes under 0 you loose but if you can keep your score above 0 you will win")

gohome = input("\n yo whats good guys im back i got 40 tickets what you tranna do? or do you just want to 'g' go home or 'n' no ")

while gohome != 'g':

    if gohome == 'n':
        rides = input("\n ok so you dont want to go home we have 'R' rides or? ")
        Eating = input("'F' to eat food what do you want to do? ")
    

    #WHILE TO LOOP EVERYTIME#

    if rides == 'r':
            UserChoicerides = input("what ride you want to go on 's' screamer, 'F' Ferris Wheel,  'B' Bumper Cars, 'R' The Rollercoaster, 'S' land slide ")
    elif Eating == 'f': 
            userchoicefood = input("o.k you want to eat so early its ok by me what you wanna eat? 'D' hotdog, 'H' hamburger, 'T' tacos, 'I' icecream, 'C' chunchulo ")

    #food#


    if Eating.lower() == 'd':
        happiness = happiness + 2
        print("that big long hot dog that ", player_name, "ate was amzing thats why", player_name, "is now ", happiness)
    elif Eating.lower()  == 'h':
        happiness = happiness - 2
        print("you run with your frineds over to the hamburger station thinking it would be good turns out it wasnt and")
        print("the meat was expired! ", happiness, )
    elif Eating.lower()  == 't':
        happiness = happiness + 3
        print("you sprinty to the to eat some mexican tacos beforer the line gets too big you eat and they taste amazing")
        print("that was delicious i rilly enjoyd it you happines is now", happiness, )
    elif Eating.lower()  == 'c': 
        appiness = happiness + 2
        print("you dont know what it is but it taste rilly good ", happiness, )
    elif Eating.lower()  == 'i':
        happiness = happiness + 1.5
        print("you run to get some sweet ice cream and it taste real good but you get a brain freeze", happiness, )

        Eating = print(input("\n do you want to 'g' go home or 'c' continue? "))
    if Eating.lower == 'c':
            rides = input("\n ok so you dont want to go home we have 'R' rides or? ")
            Eating = input("'F' to eat food what do you want to do? ")
    if Eating.lower == 'g':
            print("ok we could play another day bye",player_name )
            print("you score ended up being", happiness,)
            break

#rides#


    if rides == 's':
        happiness = happiness + 1
        print("you walk ove to the screamer specticle wondering if its going to be good you go on it and it turns out its canda fun")
        print("good choice your happines is now ", happiness,)
    elif rides  == 'f':
        happiness = happiness - 1
        print("you run with your frineds over to ferris wheel thinking it would be exiting turns out it wasnt and")
        print("i mean it was ok not that exiting but good your happiness is now", happiness, )
    elif rides  == 'b':
        happiness = happiness + 2
        print("you sprinty to the bumper cars beforer the line gets too big you get in have have the time of your life")
        print("that was fun i rilly enjoyd it you happines is now", happiness, )
    elif rides  == 'r':
        happiness = happiness + 3
        print("yo lets not go back there bro i almost vomited that was rilly fun. your happines is now", happiness, )
    elif rides  == 's':
        happiness = happiness + 1.5
        print("that was fun it wasnt as scary as i thought it was tho :( this is you happiness", happiness,) 
 

    elif gohome == 'g':
         print("ok we could play another day bye",player_name )
         print("you score ended up being", happiness,)
         break