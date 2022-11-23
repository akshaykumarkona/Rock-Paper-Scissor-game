import random
print("""-------------ROCK,PAPER AND SCISSOR-------------""")
print("""*******Rules*******


Rock vs Paper -> Paper wins
Rock vs Scissor -> Rock wins
Paper vs Scissor -> Scissor wins


""")

def sologame():
    name=input("enter your name:")
    score_a=0
    score_b=0
    gn1=" "
    no_of_plays=int(input("Enter no of plays you want to:"))
    for i in range(1,no_of_plays+1):
        std=random.choice(["rock","paper","scissor"])
        gn=input("Enter rock or paper or scissor:") 
        print("""You can enter "rock" or "r" or "R" or "Rock" for rock choice,similarly for scissors and paper choices""")
        if gn in ['r','R',"Rock","rock"]:
            gn1="rock"
        elif gn in ['s','S',"scissor","Scissor"]:
            gn1="scissor"
        elif gn in ['p','P',"paper","Paper"]:
            gn1="paper"
        else:
            print(f"{name} ,Please give correct response")

        #print(f"{name} response is   {gn1}")
        print(f"computer choice is    {std}")

        #DETERMINING WINNER AND SCORE OF EACH
        if gn1==std:
            print("draw")
        else:
            if gn1=="rock":
                if std=="scissor":
                    score_a+=1
                else:
                    score_b+=1
            elif gn1=="paper":
                if std=="rock":
                    score_a+=1
                else:
                    score_b+=1
            elif gn1=="scissor":
                if std=="paper":
                    score_a+=1
                else:
                    score_b+=1
        print(f"score of {name} is {score_a}")
        print(f"score of computer is {score_b}")
    if score_a > score_b:
        print(f"{name} wins over computer")
    elif score_a == score_b:
        print(f"Match Tied")
    else:
        print(f"Computer wins over {name}")




def dualgame():
        name1=input("enter player 1 name:")
        name2=input("enter player 2 name:")
        score_a=0
        score_b=0
        gn11=" "
        gn22=" "
        no_of_plays=int(input("Enter no of plays you want to:"))
        for i in range(1,no_of_plays+1):
            #std=random.choice(["rock","paper","scissor"])
            print("""You can enter "rock" or "r" or "R" or "Rock" for rock choice,similarly for scissors and paper choices""")
            print(f"{name1}")
            gn1=input("Enter your choice:")
            print(f"{name2}")
            gn2=input("Enter your choice:")
            
            if gn1 in ['r','R',"Rock","rock"]:
                gn11="rock"
            elif gn1 in ['s','S',"scissor","Scissor"]:
                gn11="scissor"
            elif gn1 in ['p','P',"paper","Paper"]:
                gn11="paper"
            else:
                print(f"{name1}Please give correct response")


            if gn2 in ['r','R',"Rock","rock"]:
                gn22="rock"
            elif gn2 in ['s','S',"scissor","Scissor"]:
                gn22="scissor"
            elif gn2 in ['p','P',"paper","Paper"]:
                gn22="paper"
            else:
                print(f"{name2} ,Please give correct response")
            

            #print(f"{name1} response is    {gn11}")
            print(f"{name2} choice is    {gn22}")

        #DETERMINING WINNER AND SCORE OF EACH
            if gn11==gn22:
                print("draw")
            else:
                if gn11=="rock":
                    if gn22=="scissor":
                        score_a+=1
                    else:
                        score_b+=1
                elif gn11=="paper":
                    if gn22=="rock":
                        score_a+=1
                    else:
                        score_b+=1
                elif gn11=="scissor":
                    if gn22=="paper":
                        score_a+=1
                    else:
                        score_b+=1
            print(f"score of {name1} is {score_a}")
            print(f"score of {name2} is {score_b}")
            if score_a > score_b:
                print(f"{name1} wins over {name2}")
            elif score_a == score_b:
                print(f"Match Tied")
            else:
                print(f"{name2} wins over {name1}")



choice=int(input("If you want to play with a friend enter 1 otherwise enter 0 for playing a solo game: "))
if choice==0:
    sologame()
elif choice==1:
    dualgame()

# ask()
# def ask():
#     choice=int(input("If you want to play with a friend enter 1 otherwise enter 0 for playing a solo game"))
#     if choice==0:
#         sologame()
#     elif choice==1:
#         dualgame()


    
askinput=int(input("If you wish to play a game again press 1 otherwise 0:"))
while askinput==1:
    ch=int(input("If you want to continue playing with your friend enter 1 otherwise enter 0 for playing a solo game: "))

# if askinput==1:
    if ch==0:
        sologame()
    elif ch==1:
        dualgame()
    # ask()

if askinput==0:
    print("****Thanks for Playing****")









