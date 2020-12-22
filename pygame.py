print('''INSTRUCTIONS
1.First enter the players name one by one
2.Enter the position in the format below
row column
ex:
1 1
1 2
2 1

3.Incase you enter other than these formats it promts you to enter again
4.You cant choose the position which was filled earlier


'''
)



li=[["...","...","..."],["...","...","..."],["...","...","..."]]
def pattern():
    print("    1   2   3")
    print()
    for i in range(3):
        print(i+1,end='  ')
        for j in range(3):
            print(li[i][j],end=' ')
        print() 
        print()
    print('-----------------------')
def win():
    r1=li[0][0]==li[0][1]==li[0][2]==' 1 ' or li[0][0]==li[0][1]==li[0][2]==' 0 ' 
    r2=li[1][0]==li[1][1]==li[1][2]==' 1 ' or li[1][0]==li[1][1]==li[1][2]==' 0 '
    r3=li[2][0]==li[2][1]==li[2][2]==' 1 ' or li[2][0]==li[2][1]==li[2][2]==' 0 '
    d1=li[0][0]==li[1][1]==li[2][2]==' 1 ' or li[0][0]==li[1][1]==li[2][2]==' 0 '
    d2=li[0][2]==li[1][1]==li[2][0]==' 1 ' or li[0][2]==li[1][1]==li[2][0]==' 0 '
    c1=li[0][0]==li[1][0]==li[2][0]==' 1 ' or li[0][0]==li[1][0]==li[2][0]==' 0 '
    c2=li[0][1]==li[1][1]==li[2][1]==' 1 ' or li[0][1]==li[1][1]==li[2][1]==' 0 '
    c3=li[0][2]==li[1][2]==li[2][2]==' 1 ' or li[0][2]==li[1][2]==li[2][2]==' 0 '
    if(r1 or r2 or r3 or d1 or d2 or c1 or c2 or c3):
        print("won  congratulations ")
        if(in1==0):
            print(str1)
        else:
            print(str2)
        print('Thank you for playing')
        exit()
def input_position():
    position=input('enter Position\n')
    while position not in {'1 1','1 2','1 3','2 1','2 2','2 3','3 1','3 2','3 3'}:
        position=input('enter valid Input')
    x,y=map(int,position.split())
    return x,y
in1=1
pattern()
print("TIC TAC TOE GAME")
print("enter position in the form of  row column : ex 1 0 or 2 1 or 3 1")
str1=input('enter first player name \n')
str2=input('enter second player name\n')
while True:
    in1=1-1*in1
    if(in1==0):
        print('player '+str1)
    else:
        print('player '+str2)
    x,y=map(int,input_position())
    while li[x-1][y-1]!='...':
        print('already filled try again different')
        x,y=map(int,input_position())
    li[x-1][y-1]=' '+str(in1)+' '
    pattern()
    win()
    k="..."
    count=0  
    for i in range(3):
        for j in range(3):
            if(li[i][j]==k):
                count+=1
    if(count==0):
        print("game over Thank you for playing")  
        exit()  

    
    

