import random
import string
import turtle
ch=0
#the game board:
global t
t=turtle.Pen()
def board():
    t.up()
    t.left(180+45)
    t.forward(141.4)
    t.right(45)
    t.forward(20)
    t.left(180)
    t.width(3)
    t.down()
    t.forward(40)
    t.backward(20)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.width(1)
    t.forward(10)
def draw(lives):
    if lives==5:
        t.right(90)
        t.circle(20)
        t.left(90)
        t.up()
        t.forward(40)
        t.down()
    elif lives==4:
        t.forward(90)
        t.right(45)
    elif lives==3:
        t.forward(60)
        t.backward(60)
        t.left(90)
    elif lives==2:
        t.forward(60)
        t.backward(60)
        t.right(45)
        t.backward(75)
    elif lives==1:
        t.left(45)
        t.forward(50)
        t.backward(50)
    else:
        t.right(90)
        t.forward(50)

def pick(name):
    words=[]
    name+='.txt'
    name=name.lower()
    f=open(name,'r')
    while True:
        line=f.readline().strip()
        if not line:break
        else:
            words.append(line)
    return (words[random.randint(0,len(words))])
        
def play(rand):
    letters=''
    lives=6
    for i in range(0,26):
        letters+=string.ascii_uppercase[i:i+1]+' '
    letters=letters.split()    
    word=rand
    guess=[]
    for i in range(0,len(word)):
        guess.append('_')
    print("Guess the Word:",guess)
    while lives!=0:
        print("\nLetters that u can use:\n",letters)
        if guess!=word:
            ch=input()
            ch=ch.upper()
            if letters.count(ch)==1:
                if word.count(ch)!=0:
                    for i in range(0,len(word)):
                        if word[i]==ch:
                            guess[i]=ch
                    print("Guess the Word:",guess)
                    print("Lives left:",lives)
                    letters.pop(letters.index(ch))
                else:
                    print("Incorrect\n")
                    print("Guess the Word:",guess)
                    letters.pop(letters.index(ch))
                    lives-=1
                    draw(lives)
                    print("Lives left:",lives)
                    if lives==0:
                        print("\nSorry, You Lose! :(\n")
                        print("The Word was:",word)

            else:
                print("Letter has been used already!,Try Again\n")
        elif guess==word:
            print("BINGO!! You Won :)") 
            break   
    

while ch!=2:
    print('''\nWelcome to the Hangman Game!
1.Play
2.Quit''')
    ch=eval(input("Enter your choice:"))
    if ch!=2:
        print('''Choose Categories:
1.Animals(Easy)
2.Fruits(Very Easy)
3.sowpods(very hard)''')
        cat=input("Enter category name:")
        t.reset()
        board()
        ran=pick(cat)
        rand=''
        for i in range(0,len(ran)):
            rand+=ran[i:i+1]+' '
        rand=rand.split()
        play(rand)
    else:
        print("Game Ends")
        
            
        
