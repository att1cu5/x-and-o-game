# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
turnorder=int(input("which player should go first X or O type 1 for X and 2 for O: "))
a=0
b=0
c=0
d=0
e=0
f=0
userone=0
usertwo=0
while(1==1):
  if(turnorder==1):
    while(1==1):
        print("x turn")
        userone=int(input())

        if(userone==usertwo or userone>9 and userone>0):
            print("X pick another number")
            userone=int(input())
        if(userone!=usertwo):    
            turnorder=2
            break
   
  elif(turnorder==2):
      while(1==1):
      
        print("o turn")
        usertwo=int(input())

        if(userone==usertwo or usertwo>9 and usertwo>0):
            print("O pick another number")
            usertwo=int(input())
        if(userone!=usertwo):  
            turnorder=1
            break
  if(userone!=usertwo and userone!=0 and usertwo!=0):  
            a=userone
            b=usertwo

            break


if(userone==1 and usertwo==2):
                print("X | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")

if(userone==2 and usertwo==1):
                print("O | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==3):
                print("X | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==1):
                print("O | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==3):
                print("- | X | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==2):
                print("- | O | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==4):
                print("- | X | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==4):
                print("- | - | X")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==4):
                print("X | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==5):
                print("X | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==5):
                print("- | X | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==5):
                print("- | - | X")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | X | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("X | O | -")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==6):
                print("X | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==6):
                print("- | X | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==6):
                print("- | - | X")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | X")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("X | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | X")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | X | O")
                print("---------")
                print("- | - | -")
if(userone==7 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==1 and usertwo==7):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==2 and usertwo==7):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==3 and usertwo==7):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("X | - | -")
if(userone==4 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("X | - | -")
if(userone==5 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("X | - | -")
if(userone==6 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("O | - | -")
if(userone==8 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==1 and usertwo==8):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | -")
if(userone==2 and usertwo==8):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | -")
if(userone==3 and usertwo==8):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | X | -")
if(userone==4 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | X | -")
if(userone==5 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | X | -")
if(userone==6 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | X | -")
if(userone==7 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | O | -")
if(userone==9 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==1 and usertwo==9):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==2 and usertwo==9):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==3 and usertwo==9):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | X")
if(userone==4 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | X")
if(userone==5 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | X")
if(userone==6 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | X")
if(userone==7 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | O")
if(userone==9 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | X")
if(userone==8 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | O")


usertwo=0
userone=0
while(1==1):
    if(turnorder==1):
        while(1==1):
            print("x turns")
            userone=int(input())
    
            if(userone==usertwo or usertwo>9 or usertwo>0 or userone==b or userone==a):
                
                print("X pick another number")
                
            if(userone!=usertwo and userone!=a and userone!=b):    
                turnorder=2
                break

    elif(turnorder==2):
        while(1==1):
            print("o turns")
            usertwo=int(input())
    
            if(userone==usertwo or usertwo>9 or usertwo>0 or usertwo==b or usertwo==a):
                print("O pick another number")
                

    
            if(userone!=usertwo and usertwo!=a and usertwo!=b):
                turnorder=1
                break
    if(userone!=usertwo and usertwo!=0 and userone!=0):  
            d=usertwo
            c=userone
            break
  
if(userone==1 and usertwo==2):
                print("X | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==1):
                print("O | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==3):
                print("X | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==1):
                print("O | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==3):
                print("- | X | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==2):
                print("- | O | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==4):
                print("- | X | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==4):
                print("- | - | X")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==4):
                print("X | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==5):
                print("X | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==5):
                print("- | X | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==5):
                print("- | - | X")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | X | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("X | O | -")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==6):
                print("X | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==6):
                print("- | X | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==6):
                print("- | - | X")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | X")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("X | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | X")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | X | O")
                print("---------")
                print("- | - | -")
if(userone==7 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==1 and usertwo==7):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==2 and usertwo==7):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==3 and usertwo==7):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("X | - | -")
if(userone==4 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("X | - | -")
if(userone==5 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("X | - | -")
if(userone==6 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("O | - | -")
if(userone==8 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==1 and usertwo==8):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | -")
if(userone==2 and usertwo==8):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | -")
if(userone==3 and usertwo==8):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | X | -")
if(userone==4 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | X | -")
if(userone==5 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | X | -")
if(userone==6 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | X | -")
if(userone==7 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | O | -")
if(userone==9 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==1 and usertwo==9):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==2 and usertwo==9):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==3 and usertwo==9):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | X")
if(userone==4 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | X")
if(userone==5 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | X")
if(userone==6 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | X")
if(userone==7 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | O")
if(userone==9 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | X")
if(userone==8 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | O")
usertwo=0
userone=0
while(1==1):
    if(turnorder==1):
        while(1==1):
            print("x turns")
            userone=int(input())
    
            if(userone==usertwo or usertwo>9 or usertwo>0 or userone==d or userone==c or userone==a or userone==b):
                
                print("X pick another number")
                
            if(userone!=usertwo and userone!=a and userone!=b and userone!=d and userone!=c):    
                turnorder=2
                break
      
    elif(turnorder==2):
        while(1==1):
            print("o turns")
            usertwo=int(input())
    
            if(userone==usertwo or usertwo>9 or usertwo>0 or usertwo==b or usertwo==a or usertwo==c or usertwo==d):
                print("O pick another number")
                

    
            if(userone!=usertwo and usertwo!=a and usertwo!=b and usertwo!=d and usertwo!=c):
                turnorder=1
                break
    if(userone!=usertwo and userone!=0 and usertwo!=0):  
            e=usertwo
            f=userone
            break
  
if(userone==1 and usertwo==2):
                print("X | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==1):
                print("O | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==3):
                print("X | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==1):
                print("O | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==3):
                print("- | X | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==2):
                print("- | O | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==4):
                print("- | X | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==4):
                print("- | - | X")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==4):
                print("X | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==5):
                print("X | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==5):
                print("- | X | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==5):
                print("- | - | X")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | X | -")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("X | O | -")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==1 and usertwo==6):
                print("X | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==2 and usertwo==6):
                print("- | X | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | -")
if(userone==3 and usertwo==6):
                print("- | - | X")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | X")
                print("---------")
                print("- | - | -")
if(userone==4 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("X | - | O")
                print("---------")
                print("- | - | -")
if(userone==6 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | X")
                print("---------")
                print("- | - | -")
if(userone==5 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | X | O")
                print("---------")
                print("- | - | -")
if(userone==7 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==1 and usertwo==7):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==2 and usertwo==7):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | -")
if(userone==3 and usertwo==7):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("X | - | -")
if(userone==4 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("X | - | -")
if(userone==5 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("O | - | -")
if(userone==7 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("X | - | -")
if(userone==6 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("O | - | -")
if(userone==8 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==1 and usertwo==8):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | -")
if(userone==2 and usertwo==8):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | -")
if(userone==3 and usertwo==8):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | X | -")
if(userone==4 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | X | -")
if(userone==5 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | X | -")
if(userone==6 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | O | -")
if(userone==8 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | X | -")
if(userone==7 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | O | -")
if(userone==9 and usertwo==1):
                print("O | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==1 and usertwo==9):
                print("X | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==2):
                print("- | O | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==2 and usertwo==9):
                print("- | X | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==3):
                print("- | - | O")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | X")
if(userone==3 and usertwo==9):
                print("- | - | X")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==4):
                print("- | - | -")
                print("---------")
                print("O | - | -")
                print("---------")
                print("- | - | X")
if(userone==4 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("X | - | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==5):
                print("- | - | -")
                print("---------")
                print("- | O | -")
                print("---------")
                print("- | - | X")
if(userone==5 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | X | -")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==6):
                print("- | - | -")
                print("---------")
                print("- | - | O")
                print("---------")
                print("- | - | X")
if(userone==6 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | X")
                print("---------")
                print("- | - | O")
if(userone==9 and usertwo==7):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("O | - | X")
if(userone==7 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("X | - | O")
if(userone==9 and usertwo==8):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | O | X")
if(userone==8 and usertwo==9):
                print("- | - | -")
                print("---------")
                print("- | - | -")
                print("---------")
                print("- | X | O")
