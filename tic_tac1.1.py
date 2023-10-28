import random as rad
class player:
    choosen=set()
    def __init__(self,symbol):
        # self.type=type  #user or computer
        self.go_on=True
        self.choices=[] #list of indices choose till now
        self.symbol=symbol
    def board(self,U):
        c=1  #position at board
        for i in range(3):
            for j in range(3):
                if(c in self.choices):
                    print(self.symbol,"\t",sep="",end="")
                    c+=1
                elif(c in U.choices):
                    print(U.symbol,"\t",sep="",end="")
                    c+=1
                else:
                    print(c,"\t",sep="",end="")
                    c+=1
            print()
    def take_user(self):    #user input
        global choosen
        c=int(input(f"{self.symbol}'s Chance"))
        self.choices.append(c)
        player.choosen.add(c)
        
    def comp(self,T): #computer choice
        global choosen
        choices={1,2,3,4,5,6,7,8,9}-player.choosen
        c=rad.choice(list(choices))
        self.choices.append(c)
        player.choosen.add(c)
        
    def check_win(self):
        cond=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,6,7}]
        for i in cond:
            if(set(i).issubset(set(self.choices))):
                print(f"{self.symbol} Winns")
                self.go_on=False
                break
            
    def play_user(self,usr2):
        c=0
        usr1=self
        usr1.board(usr2)
        while(usr1.go_on and usr2.go_on):     
            if(c==9):
                z=int(input("DRAW\nEnter 1 to play again, 2 to exit"))
                if(z==1):
                    c=0
                    usr1.choices.clear()
                    usr2.choices.clear()
                    print("GAME BEGINS")
                    continue
                
                elif(z==2):
                    break
                    
            usr1.take_user()
            c+=1
            usr1.board(usr2)
            usr1.check_win()
            if(usr1.go_on):
                pass
            else:
                break
            if(c==9):
                z=int(input("DRAW\nEnter 1 to play again, 2 to exit"))
                if(z==1):
                    c=0
                    usr1.choices.clear()
                    usr2.choices.clear()
                    print("GAME BEGINS")
                    continue
                
                elif(z==2):
                    break
            usr2.take_user()
            c+=1
            usr1.board(usr2)
            usr2.check_win()

    def play_comp(self,usr1):
        c=0
        comp1=self
        usr1.board(comp1)
        while(usr1.go_on and comp1.go_on):     
            if(c==9):
                z=int(input("DRAW\nEnter 1 to play again, 2 to exit"))
                if(z==1):
                    c=0
                    usr1.choices.clear()
                    comp1.choices.clear()
                    print("GAME BEGINS")
                    continue
                
                elif(z==2):
                    break
                    
            usr1.take_user()
            c+=1
            usr1.board(comp1)
            usr1.check_win()
            if(usr1.go_on):
                pass
            else:
                break
            if(c==9):
                z=int(input("DRAW\nEnter 1 to play again, 2 to exit"))
                if(z==1):
                    c=0
                    usr1.choices.clear()
                    comp1.choices.clear()
                    print("GAME BEGINS")
                    continue
                
                elif(z==2):
                    break
                
            comp1.comp(usr1)
            c+=1
            usr1.board(comp1)
            comp1.check_win()
        
mode=int(input("Enter Mode \n1 to play with friend\n2 to play with computer"))
if(mode==1):
    usr1=player("X")
    usr2=player("O")
    usr1.play_user(usr2)
    
        
if(mode==2):
    usr1=player("X")
    comp1=player("O")
    comp1.play_comp(usr1)