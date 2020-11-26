from tkinter import *
from time import *
from random import *

root = Tk()
s = Canvas(root, width=1280, height=720, background="black")

#Import Images
def importIMG():
    global logo, gameBG, menuBG, pinkchar, turqchar
    global Numbers, winTxt, loseTxt, homeBut
    global multiply, correct, wrong, instruction
    logo = PhotoImage(file = "splashscreen.gif")
    gameBG = PhotoImage(file = "background.gif")
    menuBG = PhotoImage(file = "menuscreen.gif")
    pinkchar = PhotoImage(file = "pinkchar.gif")
    turqchar = PhotoImage(file = "turqchar.gif")
    Numbers = [PhotoImage(file = "Zero.gif"), PhotoImage(file = "One.gif"), PhotoImage(file = "Two.gif"), PhotoImage(file = "Three.gif"), PhotoImage(file = "Four.gif"), PhotoImage(file = "Five.gif"), PhotoImage(file = "Six.gif"), PhotoImage(file = "Seven.gif"), PhotoImage(file = "Eight.gif"), PhotoImage(file = "Nine.gif")]
    winTxt = PhotoImage(file = "win.gif")
    loseTxt = PhotoImage(file = "lose.gif")
    homeBut = PhotoImage(file = "home.gif")
    multiply = PhotoImage(file = "multiply.gif")
    correct = PhotoImage(file = "correct.gif")
    wrong = PhotoImage(file = "wrong.gif")
    instruction = PhotoImage(file = "rules.gif")

#Set initial values
def setInitialValues():
    global xPinkchar, yPinkchar, Pinkchar, xTurqchar, yTurqchar, Turqchar
    global xMouse, yMouse, scene, number1, number2
    global MultiNum1, MultiNum2, xMultiNum, yNumber, numIMG, answer, answered
    global rightAnswer, AnswerNums
    global ansX, ansY, ansX2, ansY2
    global sign, lose, win, home
    global lastTime, signAppeared, wrongAnswered, questionAppeared, questionClicked

    xPinkchar = 64
    yPinkchar = 360
    Pinkchar = 0
    xTurqchar = 64
    yTurqchar = 460
    Turqchar = 0
    xMouse = 0
    yMouse = 0
    scene = 0
    number1 = 0
    number2 = 0
    MultiNum1 = 0
    MultiNum2 = 0
    xMultiNum = 100
    yNumber = 620
    numIMG = []
    answer = 0
    answered = False
    rightAnswer = 0
    AnswerNums = []
    ansX = 0
    ansY = 0
    ansX2 = 0
    ansY2 = 0
    sign = 0
    lose = 0
    win = 0
    home = 0
    lastTime = 0
    signAppeared = 0
    wrongAnswered = 0
    questionAppeared = 0
    questionClicked = False

#Draw correct symbol
def correctANS():
    global sign, signAppeared, lastTime
    s.delete(sign)
    signAppeared = True

    #Time sign created
    lastTime = time()
    sign = s.create_image(220, 620, image = correct)
    
#Draw correct symbol
def wrongANS():
    global sign, signAppeared, lastTime
    s.delete(sign)
    signAppeared = True

    #Time sign created
    lastTime = time()
    sign = s.create_image(220, 620, image = wrong)

#Deletes wrong or right signs
def delSign():
    global sign
    s.delete(sign)

#Draw Turqoise character
def drawTurq():
    global Turqchar, xTurqchar, yTurqchar
    s.delete(Turqchar)
    Turqchar = s.create_image(xTurqchar, yTurqchar, image = turqchar)
    
def updateTurq():
    global xTurqchar
    xTurqchar += 78
    
#Draw Background
def background():
    #Background(race track, sky, answer boxes)
    gamescreen = s.create_image(640, 360, image = gameBG)
    #Multiplication sign
    multiSign = s.create_image(220, 620, image = multiply)

#Draw Splash screen
def drawSplashScreen():
    s.update()
    sleep(1)
    splashscreen = s.create_image(640, 360, image = logo)
    s.update()
    sleep(4)
    s.delete(splashscreen)
    
#Menu screen
def drawMenuScreen():
    global scene, menuScreen
    scene = 0
    menuScreen = s.create_image(640, 360, image = menuBG)

#Mouse click
def mouseClickHandler(event):
    global mouseX, mouseY, scene, rightAnswer, ansX, ansY, ansX2, ansY2
    global questionAppeared, wrongAnswered , questionClicked
    mouseX = event.x
    mouseY = event.y
    ansX = 460
    ansY = 580
    ansX2 = 660
    ansY2 = 660
    #Start menu clicks
    if scene == 0:
        if mouseX >= 400 and mouseY >=320 and mouseX <= 840 and mouseY <= 440:
            s.delete(menuScreen)
            runGame()
        if mouseX >= 460 and mouseY >= 460 and mouseX <= 800 and mouseY <= 580:
            root.destroy()

    #Game clicks
    if scene == 1:
        #Doesn't allow spamming of button
        if questionClicked == False:
            #Box one clicked
            if mouseX >= ansX and mouseY >= ansY and mouseX <= ansX2 and mouseY <= ansY2:
                questionClicked = True
                #Check if answer right or wrong in box 1
                if rightAnswer == 0:
                    correctANS()
                    updateTurq()
                    equation()
                else:
                    wrongANS()
                    questionAppeared = False
                    wrongAnswered = time()

            #Box two clicked
            if mouseX >= ansX+280 and mouseY >= ansY and mouseX <= ansX2+280 and mouseY <= ansY2:
                questionClicked = True
                #Check if answer right or wrong in box 2
                if rightAnswer == 1:
                    correctANS()
                    updateTurq()
                    equation()
                else:
                    wrongANS()
                    questionAppeared = False
                    wrongAnswered = time()

            #Box three clicked
            if mouseX >= ansX+560 and mouseY >= ansY and mouseX <= ansX2+560 and mouseY <= ansY2:
                questionClicked = True
                #Check if answer right or wrong in box 3
                if rightAnswer == 2:
                    correctANS()
                    updateTurq()
                    equation()
                else:
                    wrongANS()
                    questionAppeared = False
                    wrongAnswered = time()

def homeclickHandler(event):
    global mouseX, mouseY
    mouseX = event.x
    mouseY = event.y
    if mouseX >= 400 and mouseY >= 520 and mouseX <= 900 and mouseY <= 680:
        print("here")
        gamerun()
        s.bind( "<Button-1>", mouseClickHandler )
    

#Game mechanics
#creating question
def question():
    global MultiNum1, MultiNum2, xMultiNum, yNumber, number1, number2, Numbers
    #Random question and selecting image based on question
    MultiNum1 = randint(0, 9)
    s.delete(number1)
    number1 = s.create_image(xMultiNum, yNumber, image = Numbers[MultiNum1])

    MultiNum2 = randint(0,9)
    s.delete(number2)
    number2 = s.create_image(xMultiNum + 240, yNumber, image = Numbers[MultiNum2])


#Randomly placing correct answer then random wrong answer
def answerOptions():
    global rightAnswer, AnswerNums
    
    #Correct answer
    answer = str(MultiNum1 * MultiNum2).zfill(2)
    wrongans1 = str(randint(0,9) * randint(0,9)).zfill(2)
    wrongans2 = str(randint(0,9) * randint(0,9)).zfill(2)
    
    #Numbers can't be the same
    while wrongans1 == answer or wrongans2 == answer or wrongans1 == wrongans2:
        wrongans1 = str(randint(0,9) * randint(0,9)).zfill(2)
        wrongans2 = str(randint(0,9) * randint(0,9)).zfill(2)

    #Randomly shuffles the answers into the boxes
    AnswerArr = [answer, wrongans1, wrongans2]
    shuffle(AnswerArr)

    #Right answer is in this spot
    rightAnswer = AnswerArr.index(answer)

    for x in AnswerNums:
        s.delete(x)

    #Draws the numbers into boxes
    for x in range(3):
        for y in range(2):
            digit = int(AnswerArr[x][y])
            AnswerNums.append(s.create_image(500+280*x+120*y, 620, image = Numbers[digit]))

#Key click Handler
def keyDownHandler(event):
    global scene

    #Skip rules
    if scene == 3:
        if event.keysym == "c":
            gamerun()


#Declares winner
def endGame():
    global lose, win, home, loseTxt, homeBut, winTxt, scene, xTurqchar
    s.delete("all")
    #If you win
    if xTurqchar >= 1220:
        win = s.create_image(640, 300, image = winTxt)
        print("win")
        print(xTurqchar)

    #If computer wins
    else:
        lose = s.create_image(640, 300, image = loseTxt)
        print("lose")
        print(xTurqchar)

    #Return to home screen button
    home = s.create_image(250, 330, image = homeBut)
    scene = 2
    s.update()
    s.bind( "<Button-1>", homeclickHandler )

#Intructions
def instructions():
    global rule, scene
    scene = 3
    rule = s.create_image(640, 360, image = instruction)
    s.update()

#Question and answer funtion
def equation():
    global questionClicked
    questionClicked = False
    question()
    answerOptions()
                                
#Runs splash screen
def runsplash():
    global scene
    importIMG()
    drawSplashScreen()
    instructions()

#Runs the entire game
def gamerun():
    setInitialValues()
    drawMenuScreen()
    
#Draw Pink character
def drawPink():
    global Pinkchar
    s.delete(Pinkchar)
    Pinkchar = s.create_image(xPinkchar, yPinkchar, image = pinkchar)

#Change pinkSpd Practice Lvl = 1 speed, +0.1 speed for increase in lvl
#People who beat lvl 10 (2 speed) have reached god level multiplying speed
def updatePink():
    global xPinkchar
    xPinkchar += 1.8

#Runs the interactive game itself
def runGame():
    global scene, signAppeared, questionAppeared, wrongAnswered 
    background()
    equation()
    scene = 1
    while xTurqchar < 1220 and xPinkchar < 1220:
        drawPink()
        drawTurq()
        
        #If there is a sign and more than 0.5 seconds has passed, delete the sign
        if signAppeared == True and time() - lastTime > 0.3:
            delSign()
            signAppeared = False

        #Time penalty if question is answered wrong of 1.5 seconds
        if questionAppeared == False and time() - wrongAnswered > 1.5:
            equation()
            questionAppeared = True
            
        s.update()
        sleep(0.03)
        updatePink()
    
    sleep(1)
    endGame()
    
#Runs game right away
root.after(0, runsplash)

#Bind mouse clicks
s.bind( "<Button-1>", mouseClickHandler )

#Bind keyboard click
s.bind( "<Key>", keyDownHandler )

s.pack()
s.focus_set()
root.mainloop()
