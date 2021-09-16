#########################PROJECT: PuzzleCube#################################
##
##PuzzleCube -  Pseudocode
##(Python)
##
##START
##
##Import Serial Library
##Import OS Library
##Import Time Library
##Import Turtle Library
##
##Define function for serial servo control taking in string value
##	Define variable and set equal to Serial Bus address
##
##	If string value is equal to “open”
##		Define and set userData variable to 1
##	Else if string value is equal to “close”
##		Define and set userData variable to 179		//note these are
##											degrees for
##											the servo
##	Define and set variable equal to the string of userData
##	Write new variable to serial communication port variable
##
##Define function to setup turtle screen
##	Define and make global variable “cursor” equal to Turtle instance
##	Define and make global variable “typing” equal to another Turtle instance
##	Define and make global variable “window” equal to window instance.
##	Set parameters for each variables corresponding instance
##
##Define function for Introduction Screen
##	Define and make variable “cursorIntro” equal to Turtle instance
##
##Define and make variable turtleWaiting taking in string value
##	Set variable “cursor” position to top right corner of screen
##	Define and set count “seconds” to 0
##	While seconds is less than or equal to user time
##		Change cursor color to black
##		Wait .5 seconds
##		Change cursor color to green
##		Wait .5 seconds
##	Stop cursor from printing
##	Set cursor color to black
##
##Define function for printing to Turtle Window taking in string value
##	Set variable “cursor” to top right corner of screen
##	Set cursor color to green
##	Write string value to screen
##	Set cursor color to black
##	
##
##Define function for typing into Turtle Window
##
##	Define variable userTyping
##	Define variable enterHit and set equal to “n”
##	Define variable cursorOn
##	Define variable microLoopCount
##
##
##	Define functions A-Z for key inputs
##		concatenate string userTyping with each key equal to key letter
##
##		While enterHit is equal to “n”
##			Listen for key inputs
##			If key pressed
##				Concatenate String user typing with that character
##Call function for screen intro
##Call function for Turtle Screen Setup
##
##Define and set variable “passwordCorrect” to false
##While “passwordCorrect” is equal to false
##	Call function typing and set check if equal to defined password
##
##//Execute game code here…. Once game complete
##Call function serial servo control to open box
##END ALL
##
##PuzzleCube -  Pseudocode
##(Aurdino)
##
##START
##
##Servo pos = 0
##
##Import Serial Library
##
##If Serial Bus is not busy
##	Servo pos = Serial Input
##
##END ALL


##########################IMPORTED LIBRARYS#################################

import time
import os
import serial
import turtle

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#Fuctions used through the code
def servoControl(data):
    ser = serial.Serial("/dev/cu.usbmodem1411",9600)
    
    if data == "open":
        userData = 35
    elif data == "close":
        userData = 179
        
    convertedData = str(userData) + ","
    ser.write(convertedData.encode())
    
def clearScreen():
    window.clear()
    turtleScreenSetup()
    
def turtleScreenSetup():
    global cursor
    global typingCursor
    global window
    
    turtle.setup(1920,1080,0, 0)
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("WOPR")
    
    cursor  = turtle.Turtle()
    cursor.penup()
    cursor.shape("arrow")
    cursor.color("black")
    cursor.pensize(3)
    
    typingCursor = turtle.Turtle()
    typingCursor.penup()
    typingCursor.shape("arrow")
    typingCursor.pensize(0)
    typingCursor.ht()
    
    global cursor
    global typingCursor
    global window
    
    
def introScreen():
    global window
    
    turtle.setup(1920,1080,0, 0)
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("PuzzleCube")
    
    cursorIntro  = turtle.Turtle()
    cursorIntro.penup()
    cursorIntro.shape("arrow")
    cursorIntro.color("white")
    cursorIntro.pensize(3)
    cursorIntro.ht()

    cursorIntro.goto(-605,310)
    cursorIntro.pencolor("black")
    cursorIntro.write("Welcome to the PuzzleCube!", move=False, align="left", font=("American Typewriter", 45, "normal"))
    time.sleep(4)
    cursorIntro.clear()


    cursorIntro.goto(-605,310)
    cursorIntro.pencolor("black")
    cursorIntro.write("If you complete the following challenges...", move=False, align="left", font=("American Typewriter", 45, "normal"))
    time.sleep(4)
    cursorIntro.clear()
    
    cursorIntro.goto(-605,310)
    cursorIntro.pencolor("black")
    cursorIntro.write("The cube will open to reveal an item!", move=False, align="left", font=("American Typewriter", 45, "normal"))
    time.sleep(4)
    cursorIntro.clear()
    
    cursorIntro.goto(-605,310)
    cursorIntro.pencolor("black")
    cursorIntro.write("Are you ready?", move=False, align="left", font=("American Typewriter", 45, "normal"))
    time.sleep(4)
    cursorIntro.clear()
    
def turtleWaiting(userTime):
    global cursor
    cursor.goto(-625,325)
    cursor.color("green")
    seconds = 0
    cursor.pendown()
    while seconds <= userTime:
        cursor.color("green")
        time.sleep(.5)
        cursor.color("black")
        time.sleep(.5)
        seconds = seconds + 1
    cursor.penup()
    cursor.color("black")
    
def screenPrint(printed):
    global cursor
    cursor.goto(-605,310)
    cursor.pencolor("green")
    cursor.write(printed, move=False, align="left", font=("American Typewriter", 25, "normal"))
    cursor.pencolor("black")
    
def typing():
    global userTyping
    global cursor
    
    userTyping = ""
    enterHit = "n"       
    cursorOn = "n"
    microLoopCount = 0
    cursor.goto(-625,325)

    def keyA():
        global userTyping
        userTyping = userTyping + "A"
        
    def keyB():
        global userTyping
        userTyping = userTyping + "B"
        
    def keyC():
        global userTyping
        userTyping = userTyping + "C"
        
    def keyD():
        global userTyping
        userTyping = userTyping + "D"
        
    def keyE():
        global userTyping
        userTyping = userTyping + "E"
        
    def keyF():
        global userTyping
        userTyping = userTyping + "F"      

    def keyG():
        global userTyping
        userTyping = userTyping + "G"      

    def keyH():
        global userTyping
        userTyping = userTyping + "H"
        
    def keyI():
        global userTyping
        userTyping = userTyping + "I"
        
    def keyJ():
        global userTyping
        userTyping = userTyping + "J"
        
    def keyK():
        global userTyping
        userTyping = userTyping + "K"
        
    def keyL():
        global userTyping
        userTyping = userTyping + "L"
        
    def keyM():
        global userTyping
        userTyping = userTyping + "M"
        
    def keyN():
        global userTyping
        userTyping = userTyping + "N"
        
    def keyO():
        global userTyping
        userTyping = userTyping + "O"
        
    def keyP():
        global userTyping
        userTyping = userTyping + "P"
        
    def keyQ():
        global userTyping
        userTyping = userTyping + "Q"
        
    def keyR():
        global userTyping
        userTyping = userTyping + "R"
        
    def keyS():
        global userTyping
        userTyping = userTyping + "S"
        
    def keyT():
        global userTyping
        userTyping = userTyping + "T"
        
    def keyU():
        global userTyping
        userTyping = userTyping + "U"
        
    def keyV():
        global userTyping
        userTyping = userTyping + "V"
        
    def keyW():
        global userTyping
        userTyping = userTyping + "W"
        
    def keyX():
        global userTyping
        userTyping = userTyping + "X"
        
    def keyY():
        global userTyping
        userTyping = userTyping + "Y"

    def keyZ():
        global userTyping
        userTyping = userTyping + "Z"
        
    def keyEnter():
        global enterHit
        global userTyping    
        enterHit = "y"
        
    def keyBackspace():
        global userTyping
        userTyping = userTyping[0:-2]
        
    def keySpace():
        global userTyping
        userTyping = userTyping + " "
        
  
    
    while enterHit == "n":
        global enterHit
        
        window.onkey(keyEnter, "Return")
        window.onkey(keyA, "a")
        window.onkey(keyB, "b")
        window.onkey(keyC, "c")
        window.onkey(keyD, "d")
        window.onkey(keyE, "e")
        window.onkey(keyF, "f")
        window.onkey(keyG, "g")
        window.onkey(keyH, "h")
        window.onkey(keyI, "i")
        window.onkey(keyJ, "j")
        window.onkey(keyK, "k")
        window.onkey(keyL, "l")
        window.onkey(keyM, "m")
        window.onkey(keyN, "n")
        window.onkey(keyO, "o")
        window.onkey(keyP, "p")
        window.onkey(keyQ, "q")
        window.onkey(keyR, "r")
        window.onkey(keyS, "s")
        window.onkey(keyT, "t")
        window.onkey(keyU, "u")
        window.onkey(keyV, "v")
        window.onkey(keyW, "w")
        window.onkey(keyX, "x")
        window.onkey(keyY, "y")
        window.onkey(keyZ, "z")
        window.onkey(keySpace, "space")
        window.onkey(keyBackspace, "Delete")
        
        
        typingCursor.goto(-500,310)
        typingCursor.pencolor("green")
        typingCursor.write(userTyping, move=False, align="left", font=("American Typewriter", 25, "normal"))

        window.listen()

        microLoopCount = microLoopCount + 1
        
        if microLoopCount >= 25:
            if cursorOn == "n":
                cursor.color("green")
                cursorOn = "y"
                microLoopCount = 0
                
            elif cursorOn == "y":
                cursor.color("black")
                cursorOn = "n"
                microLoopCount = 0

    return userTyping

def loading():
    global cursor
    loadingBar = ""
    cursor.pencolor("green")
    
    for i in range (100):
        loadingBar = loadingBar + ":"
        cursor.goto(-605,295)
        cursor.write(loadingBar, move=False, align="left", font=("American Typewriter", 25, "normal"))
        
    cursor.pencolor("black")
              

def ticTacToe():
    
    clearScreen()
    global cursor
    
   
    screenPrint("Let's play a game of Tic-Tac-Toe...")
    turtleWaiting(1)
    clearScreen()

    def entryCommandsSetup():
        global enterCommand
        
        enterCommand = turtle.Turtle()
        enterCommand.penup()
        enterCommand.shape("arrow")
        enterCommand.color("black")
        enterCommand.pensize(0)
        enterCommand.goto(-605, 0)
        enterCommand.write("Enter desired location and symbol: ", move=False, align="left", font=("American Typewriter", 25, "normal"))
        enterCommand.goto(-605, -100)
        enterCommand.ht()


    def entryTyping():
        entryCommandsSetup()
        
        global enterCommand
        global userTyping
        
        userTyping = ""
        enterHit = "n"       
        cursorOn = "n"
        microLoopCount = 0
        cursor.goto(-625,325)


        def key1():
            global userTyping
            userTyping = userTyping + "1"
            
        def key2():
            global userTyping
            userTyping = userTyping + "2"
            
        def key3():
            global userTyping
            userTyping = userTyping + "3"
        
        def keyA():
            global userTyping
            userTyping = userTyping + "A"
            
        def keyB():
            global userTyping
            userTyping = userTyping + "B"
            
        def keyC():
            global userTyping
            userTyping = userTyping + "C"
            
        def keyD():
            global userTyping
            userTyping = userTyping + "D"
            
        def keyE():
            global userTyping
            userTyping = userTyping + "E"
            
        def keyF():
            global userTyping
            userTyping = userTyping + "F"      

        def keyG():
            global userTyping
            userTyping = userTyping + "G"      

        def keyH():
            global userTyping
            userTyping = userTyping + "H"
            
        def keyI():
            global userTyping
            userTyping = userTyping + "I"
            
        def keyJ():
            global userTyping
            userTyping = userTyping + "J"
            
        def keyK():
            global userTyping
            userTyping = userTyping + "K"
            
        def keyL():
            global userTyping
            userTyping = userTyping + "L"
            
        def keyM():
            global userTyping
            userTyping = userTyping + "M"
            
        def keyN():
            global userTyping
            userTyping = userTyping + "N"
            
        def keyO():
            global userTyping
            userTyping = userTyping + "O"
            
        def keyP():
            global userTyping
            userTyping = userTyping + "P"
            
        def keyQ():
            global userTyping
            userTyping = userTyping + "Q"
            
        def keyR():
            global userTyping
            userTyping = userTyping + "R"
            
        def keyS():
            global userTyping
            userTyping = userTyping + "S"
            
        def keyT():
            global userTyping
            userTyping = userTyping + "T"
            
        def keyU():
            global userTyping
            userTyping = userTyping + "U"
            
        def keyV():
            global userTyping
            userTyping = userTyping + "V"
            
        def keyW():
            global userTyping
            userTyping = userTyping + "W"
            
        def keyX():
            global userTyping
            userTyping = userTyping + "X"
            
        def keyY():
            global userTyping
            userTyping = userTyping + "Y"

        def keyZ():
            global userTyping
            userTyping = userTyping + "Z"
            
        def keyComma():
            global userTyping
            userTyping = userTyping + ","
            
        def keyEnter():
            global enterHit
            global userTyping    
            enterHit = "y"
            
        def keyBackspace():
            global userTyping
            userTyping = userTyping[0:-2]
            
        def keySpace():
            global userTyping
            userTyping = userTyping + " "
            
      
        
        while enterHit == "n":
            global enterHit
            global enterCommand
            
            window.onkey(keyEnter, "Return")
            window.onkey(keyA, "a")
            window.onkey(keyB, "b")
            window.onkey(keyC, "c")
            window.onkey(keyD, "d")
            window.onkey(keyE, "e")
            window.onkey(keyF, "f")
            window.onkey(keyG, "g")
            window.onkey(keyH, "h")
            window.onkey(keyI, "i")
            window.onkey(keyJ, "j")
            window.onkey(keyK, "k")
            window.onkey(keyL, "l")
            window.onkey(keyM, "m")
            window.onkey(keyN, "n")
            window.onkey(keyO, "o")
            window.onkey(keyP, "p")
            window.onkey(keyQ, "q")
            window.onkey(keyR, "r")
            window.onkey(keyS, "s")
            window.onkey(keyT, "t")
            window.onkey(keyU, "u")
            window.onkey(keyV, "v")
            window.onkey(keyW, "w")
            window.onkey(keyX, "x")
            window.onkey(keyY, "y")
            window.onkey(keyZ, "z")
            window.onkey(key1, "1")
            window.onkey(key2, "2")
            window.onkey(key3, "3")
            window.onkey(keyComma, ",")
            window.onkey(keySpace, "space")
            window.onkey(keyBackspace, "Delete")
            
            
            enterCommand.goto(-0,-300)
            enterCommand.pencolor("green")
            enterCommand.write(userTyping, move=False, align="left", font=("American Typewriter", 25, "normal"))

            window.listen()


        return userTyping

        
           
    def ticTacScreen(printed):
        global cursor
        cursor.pencolor("green")
        cursor.write("X", 0, "left", font=("American Typewriter", 80, "normal"))
        cursor.pencolor("black")
        
    def gridUpdate(value1,value2,value3):
        global cursor
        global window
        cursor.pencolor("green")
        
        cursor.goto(-200,200)
        cursor.write(value1[0], 0, "center", font=("American Typewriter", 80, "normal"))  #GRID1

        cursor.goto(40,200)
        cursor.write(value1[1], 0, "center", font=("American Typewriter", 80, "normal"))

        cursor.goto(265,200)
        cursor.write(value1[2], 0, "center", font=("American Typewriter", 80, "normal"))



        cursor.goto(-200,50)
        cursor.write(value2[0], 0, "center", font=("American Typewriter", 80, "normal"))  #GRID2

        cursor.goto(40,50)
        cursor.write(value2[1], 0, "center", font=("American Typewriter", 80, "normal"))

        cursor.goto(265,50)
        cursor.write(value2[2], 0, "center", font=("American Typewriter", 80, "normal"))



        cursor.goto(-200,-150)
        cursor.write(value3[0], 0, "center", font=("American Typewriter", 80, "normal"))  #GRID3

        cursor.goto(40,-150)
        cursor.write(value3[1], 0, "center", font=("American Typewriter", 80, "normal"))

        cursor.goto(265,-150)
        cursor.write(value3[2], 0, "center", font=("American Typewriter", 80, "normal"))
        
    def computerTurn():
        for i in range (0,2):
            if GRID1[i] != "X" and GRID1[i] != "O":
                if i <= 1 :
                    if GRID2[i+1] != "X" and GRID2[i+1] != "O":
                       GRID1[i+1] = "O"
                elif i >= 1:
                    if GRID1[i-1] != "X" and GRID1[i-1] != "O":
                        GRID1[i-1] = "O"
                else:
                    if GRID2[i] != "X" and GRID2[i] != "O":
                        GRID2[i] = "O"
                    else:
                        if i <= 1:
                            if GRID2[i+1] != "X" and GRID2[i+1] != "O":
                                GRID2[i+1] = "O"
                        elif i >= 1:
                            if GRID2[i-1] != "X" and GRID2[i-1] != "O":
                                GRID2[i-1] = "O"
                                                      
            return
                    
            if GRID2[i] != "X" and GRID2[i] != "O":
                if i <= 1:
                    if GRID2[i+1] != "X" and GRID2[i+1] != "O":
                        GRID2[i+1] = "O"
                elif i >= 1:
                    if GRID2[i-1] != "X" and GRID2[i-1] != "O":
                        GRID2[i-1] = "O"
                else:
                    if GRID3[i] != "X" and GRID3[i] != "O":
                        GRID3[i] = "O"
                    else:
                        if i <= 1:
                            if GRID1[i+1] != "X" and GRID1[i+1] != "O":
                                GRID1[i+1] = "O"
                        elif i >= 1:
                            if GRID1[i-1] != "X" and GRID1[i-1] != "O":
                                GRID1[i-1] = "O"
            return

            if GRID3[i] != "X" and GRID3[i] != "O":
                if i <= 1:
                    if GRID3[i+1] != "X" and GRID3[i+1] != "O":
                       GRID3[i+1] = "O"
                elif i >= 1:
                    if GRID2[i-1] != "X" and GRID2[i-1] != "O":
                       GRID3[i-1] = "O"
                return


        
    def logicCheck():
        winner = ""
        global winner
        
        if GRID1[0] == GRID1[1] and GRID1[1] == GRID1[2] and GRID1[0] != "" and GRID1[1] != "" and GRID1[2] != "":                  #Checks for:    X  X  X
            if GRID1[0] == "X":                                                                                                     #
                winner = "Player"                                                                                                   #
                gameOn = False                                                                                                                                   
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True 
        
        
        if GRID2[0] == GRID2[1] and GRID2[1] == GRID2[2] and GRID2[0] != "" and GRID2[1] != "" and GRID2[2] != "":                  #Checks for:
             if GRID2[0] == "X":                                                                                                    #               X  X  X
                winner = "Player"                                                                                                   #
                gameOn = False                                                                                                                                   
                return True                                                                                                             
             else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True 
                                                                                                                            


        if GRID3[0] == GRID3[1] and GRID3[1] == GRID3[2] and GRID3[0] != "" and GRID3[1] != "" and GRID3[2] != "":                  #Checks for:
            if GRID3[0] == "X":                                                                                                     #
                winner = "Player"                                                                                                   #               X  X  X
                gameOn = False                                                                                                                                   
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True 
 

        

        if GRID1[0] == GRID2[0] and GRID2[0] == GRID3[0] and GRID1[0] != "" and GRID2[0] != "" and GRID3[0] != "":                  #Checks for:    X
            if GRID1[0] == "X":                                                                                                     #               X
                winner = "Player"                                                                                                   #               X 
                gameOn = False                                                                                                                                   
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True 

        
        
        if GRID1[1] == GRID2[1] and GRID2[1] == GRID3[1] and GRID1[1] != "" and GRID2[1] != "" and GRID3[1] != "":                  #Checks for:        X            
            if GRID1[1] == "X":                                                                                                     #                   X
                winner = "Player"                                                                                                   #                   X 
                gameOn = False                                                                                                                                 
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True 
        

        if GRID1[2] == GRID2[2] and GRID2[2] == GRID3[0] and GRID1[2] != "" and GRID2[2] != "" and GRID3[2] != "":                  #Checks for:            X
            if GRID1[2] == "X":                                                                                                     #                       X
                winner = "Player"                                                                                                   #                       X 
                gameOn = False                                                                                                                                 
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True 
        


        if GRID1[0] == GRID2[1] and GRID2[1] == GRID3[2] and GRID1[0] != "" and GRID2[1] != "" and GRID3[2] != "":                  #Checks for:      X
            if GRID1[0] == "X":                                                                                                     #                   X
                winner = "Player"                                                                                                   #                     X 
                gameOn = False                                                                                                                                 
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True        
        
        if GRID1[2] == GRID2[1] and GRID2[1] == GRID3[0] and GRID1[2] != "" and GRID2[1] != "" and GRID3[0] != "":                  #Checks for:            X            
            if GRID1[2] == "X":                                                                                                     #                     X
                winner = "Player"                                                                                                   #                   X 
                gameOn = False                                                                                                                                 
                return True                                                                                                             
            else:
                winner = "Computer"
                gameOn = False                                                                                                                                  
                return True        
                                                                                                                  
        
        
    gameOn = True
    
    userChoice = ""
    
    GRID1 = ["","",""]
    GRID2 = ["","",""]
    GRID3 = ["","",""]


    window.bgpic("BackgroundForTicTacToe.gif")          
    while gameOn == True:

        xLocation = 0
        yLocation = 0

        computerTurn()
        gridUpdate(GRID1,GRID2,GRID3)
        
        if logicCheck() == True:
            return True

        userSelection = entryTyping()
        if len(userSelection) == 3:
            if userSelection[0] == "a" or  userSelection[0] == "b" or userSelection[0] == "c" or userSelection[0] == "A" or userSelection[0] == "B" or userSelection[0] == "C":
               if userSelection[1] == ",":
                   if userSelection[2] == "1" or userSelection[2] == "2" or userSelection[2] == "3":
                        if userSelection[0] == "A" or userSelection[0] == "a":
                            
                            xLocation = 600
                        
                            if userSelection[2] == "1":
                                yLocation = 0
                                if GRID1[0] != "X" and GRID1[0] != "O":
                                    GRID1[0] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                            elif userSelection[2] == "2":
                                yLocation = -200
                                if GRID1[1] != "X" and GRID1[1] != "O":
                                    GRID1[1] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                            elif userSelection[2] == "3":
                                yLocation = -400
                                if GRID1[2] != "X" and GRID1[2] != "O":
                                    GRID1[2] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                        elif userSelection[0] == "B" or userSelection[0] == "b":
                            
                            xLocation = 400

                            if userSelection[2] == "1":
                                yLocation = 0
                                if GRID2[0] != "X" and GRID2[0] != "O":
                                    GRID2[0] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                            elif userSelection[2] == "2":
                                yLocation = -200
                                if GRID2[1] != "X" and GRID2[1] != "O":
                                    GRID2[1] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                            elif userSelection[2] == "3":
                                yLocation = -400
                                if GRID2[2] != "X" and GRID2[2] != "O":
                                    GRID2[2] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                        

                        elif userSelection[0] =="C" or userSelection[0] == "c":
                            
                            xLocation = 200

                            if userSelection[2] == "1":
                                yLocation = 0
                                if GRID3[0] != "X" and GRID3[0] != "O":
                                    GRID3[0] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                            elif userSelection[2] == "2":
                                yLocation = -200
                                if GRID3[1] != "X" and GRID3[1] != "O":
                                    GRID3[1] = "X"
                                else:
                                    screenPrint("INVALID SELECTION!")
                                    
                            elif userSelection[2] == "3":
                                yLocation = -400
                                if GRID3[2] != "X" and GRID3[2] != "O":
                                    GRID3[2] = "X"
                                    
                                else:
                                    screenPrint("INVALID SELECTION!")
                        
            else:
                screenPrint("Invalid Selection!")
                turtleWaiting(1)
        else:
            screenPrint("Invalid Selection!")
            turtleWaiting(1)
            
        cursor.goto(xLocation,yLocation)
        clearScreen()
        window.bgpic("BackgroundForTicTacToe.gif")
        gridUpdate(GRID1,GRID2,GRID3)
        if logicCheck() == True:
            return True
    
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#


introScreen()              
turtleScreenSetup()
turtleWaiting(1)
screenPrint("W.O.P.R. LOADING... ")
loading()
turtleWaiting(1)
clearScreen()

passwordCorrect = False

while passwordCorrect == False:

    turtleScreenSetup()
    screenPrint("LOGIN: ")
    myLogon= typing()
    time.sleep(2)

    if (myLogon == "JOSHUA"):
        clearScreen()
        screenPrint("LOGIN ACCEPTED")
        turtleWaiting(1)
        clearScreen()
        screenPrint("GREETINGS PROFESSOR FALKEN.")
        turtleWaiting(1)
        clearScreen()
        passwordCorrect = True
        
    elif (myLogon == "ARTYMIS"):
        clearScreen()
        screenPrint("BACKDOOR ACTIVATED")
        time.sleep(2)
        clearScreen()
        screenPrint("GREETINGS CALEB.")
        turtleWaiting(1)
        clearScreen()
        
        doorMode = 1

        while doorMode== 1:
            

            clearScreen()
            turtleScreenSetup()
            servoSetup = input("Enter action: ")
            servoSetup = str(servoSetup)
            
            if servoSetup == "open" or servoSetup == "close":
                servoControl(servoSetup)
                clearScreen()
                
            elif servoSetup == "EXIT":
                doorMode = 0
                clearScreen()
                
            clearScreen()
            

    else:
        clearScreen()
        screenPrint("CONNECTION TERMINATED.")
        time.sleep(2)
        clearScreen()

playGame = "n"        
screenPrint("WOULD YOU LIKE TO PLAY A GAME?")
turtleWaiting(1)
clearScreen()
screenPrint("Y or N: ")
cursor.goto(-605,295)
typingCursor.goto(-605,295)

while playGame == "n":
    turtleWaiting(.10)
    userInput = typing()
    
    if userInput == "Y":
        clearScreen()
        playGame = "Y"
        
    else:
        clearScreen()
        userInput = ""
        screenPrint("Y or N: ")
        cursor.goto(-605,295)
        typingCursor.goto(-605,295)


winGame = False

while winGame == False:
    
    outCome = ticTacToe()

    if outCome == True:
        clearScreen()
        turtleScreenSetup()
        turtleWaiting(1)
        screenPrint("The only way to win is not to play...")
        turtleWaiting(1)
        clearScreen()
        screenPrint(winner + " Is Victorious!!!")
        turtleWaiting(1)
        clearScreen()
        turtleScreenSetup()
        turtleWaiting(1)
        screenPrint("You have proved worthy, take the prize...")
        servoControl("open")
        winGame = True
        
    else:
        winGame = False
