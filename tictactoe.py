import random as r
def printBoard(player,Mee):
    one=playersign if player[0] else (Meesign if Mee[0] else 1)
    two=playersign if player[1] else (Meesign if Mee[1] else 2)
    three=playersign if player[2] else (Meesign if Mee[2] else 3)
    four=playersign if player[3] else (Meesign if Mee[3] else 4)
    five=playersign if player[4] else (Meesign if Mee[4] else 5)
    six=playersign if player[5] else (Meesign if Mee[5] else 6)
    seven=playersign if player[6] else (Meesign if Mee[6] else 7)
    eight=playersign if player[7] else (Meesign if Mee[7] else 8)
    nine=playersign if player[8] else (Meesign if Mee[8] else 9)

    print(f"{one} | {two} | {three}")
    print(f"--|---|--")
    print(f"{four} | {five} | {six}")
    print(f"--|---|--")
    print(f"{seven} | {eight} | {nine}")
def sum(scorer,l):
    s=scorer[l[0]]+scorer[l[1]]+scorer[l[2]]
    return s 

def checkWin(player,Mee):
    Win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in Win:
        if(sum(player,i)==3):
            print("* YOU WON *")
        elif(sum(Mee,i)==3):
            print(" *MEE WON *")

if __name__=="__main__":
    player=[0,0,0,0,0,0,0,0,0]
    Mee=[0,0,0,0,0,0,0,0,0]
    move=1 #1 for X & 0 or O
    print("***Play Tic Tac Toe with 'MEE'***")
    playersign=input("Choose your Sign(X/O) : ")
    playersign=playersign.upper()
    if(playersign not in ['X','O']):
        print("Invalid Symbol")
    if(playersign=='X'):
        Meesign='O'
    elif(playersign=='O'):
        Meesign='X'
    while(True):
        printBoard(player,Mee)
        if (move==1):
            print("# Your Chance #")
            place=int(input("Enter a place from 1 to 9 : "))
            if(place>=1 and place<=9):
                player[place-1]=1
            else:
                print("Wrong Choice : ")
        else:
            print("# MEE's Chance #")
            place=r.randint(1,9)
            Mee[place-1]=1
        checkWin(player,Mee)
        move=1-move
