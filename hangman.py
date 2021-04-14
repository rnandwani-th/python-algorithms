import turtle, random
turtle.speed(0)
turtle.hideturtle()
turtle.up()
turtle.down()

def drawgallow():
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.seth(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(20)
    turtle.fd(20)
    turtle.rt(90)

def drawhead():
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.seth(90)
    turtle.fd(200)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(20)
    turtle.fd(20)
    turtle.rt(90)
    turtle.circle(20)
    turtle.lt(90)
    turtle.up()
    turtle.fd(40)
    turtle.down()

def drawtorso():
    turtle.goto(-100,120)
    turtle.down()
    turtle.seth(270)
    turtle.fd(70)


def drawarm1():
    turtle.goto(-100,70)
    turtle.down()
    turtle.seth(45)
    turtle.fd(55)

def drawarm2():
    turtle.goto(-100,70)
    turtle.down()
    turtle.seth(135)
    turtle.fd(55)

def drawleg1():
    turtle.up()
    turtle.goto(-100,50)
    turtle.down()
    turtle.seth(315)
    turtle.fd(40)

def drawleg2():
    turtle.goto(-100,50)
    turtle.down()
    turtle.seth(225)
    turtle.fd(40)

def makeunderscores():
    turtle.down()
    turtle.fd(25)
    turtle.up()
    turtle.fd(15)
    turtle.down()



wordlist = ['phone','tacos','newyork','laundry','water','france','kenya','calibre','walnut','calorie','mailbox','candle','actor','keychain','magnify','abolish','bachelor','backfire','jacket','janitor']
n = random.randint(0,19)
word = wordlist[n]
word = str(word)
underscores = len(word)
turtle.up()
turtle.goto(-200,-100)
position = []
for i in range(underscores):
    x = turtle.pos()
    makeunderscores()
    position.append(x)




wrong_letters = ''
correct_letters = ''
letters_guessed = []
done = False
while len(word) != len(correct_letters) and len(wrong_letters) < 6:
    guess = str(turtle.textinput("Let's play hangman!",'Guess a letter')).lower()
    oo = (-200,-200)
    if guess in correct_letters:
        turtle.up()
        turtle.goto(oo)
        turtle.write('You already guessed that letter','center',font=('Arial',10,'normal'))
        turtle.seth(270)
        turtle.fd(5)
        oo = (oo[0],oo[1]-13)
    elif guess in wrong_letters:
        turtle.up()
        turtle.goto(oo)
        turtle.write('You already guessed that letter','center',font=('Arial',10,'normal'))
        turtle.seth(270)
        turtle.fd(5)
        oo = (oo[0],oo[1]-13)
    elif guess in word:
        indexofguess = word.index(guess)            
        uu = position[indexofguess]                 
        uu = (uu[0]+12.5,uu[1])                     
        turtle.seth(0)
        turtle.up()
        turtle.goto(uu)
        turtle.write(guess,'center',font=('Arial',15,'normal'))
        turtle.up()
        turtle.down()
        correct_letters += guess
    elif guess not in word:
        wrong_letters += guess
        if (wrong_letters.count('') -1) == 0:
            turtle.up()
            drawgallow()
        if (wrong_letters.count('') - 1) == 1:
            turtle.up()
            drawhead()
        elif (wrong_letters.count('') -1) == 2:
            turtle.up()
            drawtorso()
        elif (wrong_letters.count('') -1) == 3:
            turtle.up()
            drawarm1()
        elif (wrong_letters.count('') -1) == 4:
            turtle.up()
            drawarm2()
        elif (wrong_letters.count('') -1 )== 5:
            turtle.up()
            drawleg1()
        elif (wrong_letters.count('') -1) ==6:
            turtle.up()
            drawleg2()
            done = True                  #setting a condition to check if the game has ended


if len(word) == len(correct_letters):
    turtle.up()
    turtle.goto(-170,250)
    turtle.write('Congratulations! You won!','center',font = ('Arial',20,'normal'))
    turtle.up()


if done:               #this is used to end the game
    turtle.up()
    turtle.goto(-170,250)
    turtle.write('Sorry! You lose.','center',font = ('Arial',20,'normal'))
    turtle.goto(100,100)
    turtle.write('The word was ' + word,'center',font = ('Arial',15,'normal'))