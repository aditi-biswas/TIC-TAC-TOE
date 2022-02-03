chk=0   #variable with help of which we will check if there is a tie or not
def display(a):      #displaying tic-tac-toe board
    print('\n'*10)     # This prints 10 blank lines in terminal so that there is space between the previous and the current entries
    
    for i in range(len(a[0])):
        print(a[0][i],end=' ')
        if i<2:
            print("|",end=' ')
    print('\n')

    for i in range(len(a[0])):
        print('__',end='  ')
    print('\n')

    for i in range(len(a[1])):
        print(a[1][i],end=' ')
        if i<2:
            print("|",end=' ')
    print('\n')

    for i in range(len(a[0])):
        print('__',end='  ')
    print('\n')

    for i in range(len(a[2])):
        print(a[2][i],end=' ')
        if i<2:
            print("|",end=' ')
    print('\n')


def user_input():    #function to check user input
    global game_list
    choice1=[' ',' ']
    choice2=False
    while choice1[0].isdigit()==False or choice1[1].isdigit()==False or choice2==False:
        choice1[0]=input("Enter row between 0-2")
        choice1[1]=input("Enter column between 0-2")
        if choice1[0].isdigit() == False or choice1[1].isdigit()==False:
            print("You did not enter 2 numbers")
        else:
            if(choice1[0] in ['0','1','2'] and choice1[1] in ['0','1','2']):
                if(game_list[int(choice1[0])][int(choice1[1])]==' '):
                    choice2=True
                else:
                    print("Please enter another position as the position is already full")
            else:
                print("Your number is out of acceptable range")
    return [int(choice1[0]),int(choice1[1])]

cou=0
def replacement_choice(arr,position,val):     #function to replace empty space with 'X' or 'O'
    global cou
    if cou%2==0:
        user_placement=val
    else:
        if val=='X':
            user_placement='O'
        else:
            user_placement='X'
    arr[position[0]][position[1]]=user_placement
    cou=cou+1
    return arr


def gameon_choice():     #function to check if players want to play again
    choice1=' '
    while choice1.upper() not in ['Y','N']:
        choice1=input("Would you like to keep playing? Y or N ")
        if choice1.upper() not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
        else:
            if(choice1.upper()=='Y'):
                return True
            else:
                return False


def sign_choice():     #function to choose what sign does player1 wants to make
    choice1=' '
    while choice1.upper() not in ['X','O']:
        choice1=input("What does Player1 wants to mark? X or O ")
        if choice1.upper() not in ['X','O']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
        else:
            print('\n')
            print("LET'S START THE GAME!!")
            return choice1.upper()

def winning_condition(ar):     #function to determine who is winner
    global cou
    global chk
    global c
    if(ar[0][0]==ar[1][1]==ar[2][2]!=' ' or ar[0][2]==ar[1][1]==ar[2][0]!=' ' or ar[0][0]==ar[0][1]==ar[0][2]!=' ' or ar[0][0]==ar[1][0]==ar[2][0]!=' ' or ar[0][1]==ar[1][1]==ar[2][1]!=' ' or ar[1][0]==ar[1][1]==ar[1][2]!=' ' or ar[2][0]==ar[2][1]==ar[2][2]!=' ' or ar[0][2]==ar[1][2]==ar[2][2]!=' '):
        chk=1
        if((cou-1)%2==0):
            print("CONGRATULATIONS!! Player 1 is WINNER")
        else:
            print("CONGRATULATIONS!! Player 2 is WINNER")
        c=0


rows1=[' ',' ',' ']
rows2=[' ',' ',' ']
rows3=[' ',' ',' ']
game_list=[rows1,rows2,rows3]
game_on=True
display(game_list)
inp=sign_choice()
while game_on==True:
    c=0
    posi=user_input()
    game_list=replacement_choice(game_list,posi,inp)
    display(game_list)
    for i in range(len(game_list)):
        for j in range(len(game_list[i])):
            if game_list[i][j]==' ':
                c+=1    
    winning_condition(game_list)             
    if(c==0):
        if chk==0:
            print("TIE !!")
        game_on=gameon_choice()
        if game_on==True:
            inp=sign_choice()
        rows1=[' ',' ',' ']
        rows2=[' ',' ',' ']
        rows3=[' ',' ',' ']
        game_list=[rows1,rows2,rows3]
        cou=0


