print("Welcome to your Game")
name = input("What is your name? ")
print("hi ",name)
age = int(input("What is your age? "))
#print(age)
#print(name,"you are good to go. As you are",age,"years old")
health = 10
print("you are starting with ",health,"health")
if age > 18:
    print("you can continue the game.")
    want_to_play = input("Dow you want to play?")
    if want_to_play.lower() == 'yes':
        print("lets play ")

        choice = input("you wanna go left or right? ")
        if choice.lower() == "left":
            ans = input("you came the right way. Now you follow and reach the lake. Do you wanna swim or go around? ")

            if ans.lower() == "around":
                print("you went around and reached the other side of the lake.")


            elif ans.lower() == "across":
                print("you went around and lost 5 health.")
                health-=5


            ans2 = input("you notice a house and river. where do you go? ")
            if ans2.lower() == 'house':
                print("you went to the house and you are safe.")
            else:
                print('you couldnt swim now.')
                health-=5

                if health == 0:
                    print("you lose")

        else:
            print("you went in the wrong way")


    else:
        print("see you then")

else:
    print("you cannot continue the game")


#print("The game begins")