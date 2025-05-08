#FINAL PROJECT (Sotaro, Daniel)


from graphics import *
import random
import math


class Background:
   '''This class draws a background for the game, (the field with a goal and lines).'''


   def __init__(self, win):
       '''This init method calls everything we need for drawing the field: lines, circles, and the penalty box.'''
       self.win = win
       self.win.setBackground("green")
       self.leftSideline = self.drawLeftSideline()
       self.rightSideline = self.drawRightSideline()
       self.endLine = self.drawEndline()
       self.midfieldCircle = self.drawMidfieldCircle()
       self.halfcircle = self.drawHalfCircle()
       self.pBox1 = self.drawPenaltyBox()
       self.pBox2 = self.drawPenaltyBox2()
       self.goal = self.drawGoal()
       self.penaltySpot = self.drawPenaltySpot()


   def drawLeftSideline(self):
       '''This draws the left side line.'''
       leftSideline = Line(Point(100, 50), Point(100, 1000))
       leftSideline.setFill("white")
       leftSideline.draw(self.win)
       return leftSideline
  
   def drawRightSideline(self):
       '''This draws the right side line.'''
       rightSideline = Line(Point(900, 50), Point(900, 1000))
       rightSideline.setFill("white")
       rightSideline.draw(self.win)
       return rightSideline
  
   def drawEndline(self):
       '''This draws the end line.'''
       endline = Line(Point(100, 50,), Point(900, 50))
       endline.setFill("white")
       endline.draw(self.win)
       return endline
  
   def drawMidfieldCircle(self):
       '''This draws the center circle on the half-way line of the whole field (This circle appears as a
       semicircle in the game since our game only needs a half field).'''
       midfieldCircle = Circle(Point(500, 1000), (175))
       midfieldCircle.setOutline("white")
       midfieldCircle.draw(self.win)
       return midfieldCircle
  
   def drawHalfCircle(self):
       '''This draws the half circle on the edge of the penalty area.'''
       halfCircle = Circle(Point(500, 180), 125)
       halfCircle.setOutline("white")
       halfCircle.draw(self.win)
       return halfCircle
  
   def drawPenaltyBox(self):
       '''This draws the penalty box (18 yards from the end line in the real field).'''
       pBox1 = Rectangle(Point(250, 50), Point(750, 250))
       pBox1.setOutline("white")
       pBox1.setFill("green")
       pBox1.draw(self.win)
       return pBox1
  
   def drawPenaltyBox2(self):
       '''This draws the smaller penalty box (6 yards from the end line in the real field).'''
       pBox2 = Rectangle(Point(400, 50), Point(600, 125))
       pBox2.setOutline("white")
       pBox2.setFill("green")
       pBox2.draw(self.win)
       return pBox2
  
   def drawGoal(self):
       '''This draws the goal.'''
       goal = Rectangle(Point(450, 50), Point(550, 25))
       goal.setFill("white")
       goal.setOutline("white")
       goal.draw(self.win)
       return goal
  
   def drawPenaltySpot(self):
       '''This draws the penalty spot.'''
       penaltySpot = Circle(Point(500, 187.5), 2.5)
       penaltySpot.setFill("white")
       penaltySpot.setOutline("white")
       penaltySpot.draw(self.win)
       return penaltySpot
  

    
class Game:
    '''The Game class creates an object that contains the code necessary for the game to run, including all
       responses to user input and computer intelligence. Computer intelligence is incorporated by using
       self.probability to make it more difficult to complete passes of longer distance and easier to complete
       shorter passes, making the game more realistic.'''
    
    def __init__(self, win):
        '''Draws all of the initial player (Circle), player number (Text), directions (Rectangle/Text) and 
            computer (Circle) objects. Sets the variable inPosession to 1 (because Player 1 "has" the ball
            to begin the game)'''
        self.win = win
        self.computer2 = self.drawComputer(525, 625)
        self.computer3 = self.drawComputer(325, 325)
        self.computer4 = self.drawComputer(675, 325)
        self.player1 = self.drawPlayer(500, 775)
        self.playerNumber1 = self.drawPlayerNumber(500, 775, 1)
        self.player2 = self.drawPlayer(200, 500)
        self.playerNumber2 = self.drawPlayerNumber(200, 500, 2)
        self.player3 = self.drawPlayer(400, 300)
        self.playerNumber3 = self.drawPlayerNumber(400, 300, 3)
        self.player4 = self.drawPlayer(800, 400)
        self.playerNumber4 = self.drawPlayerNumber(800, 400, 4)
        self.ball = self.drawBall(500, 775)
        self.inPossession = 1
        self.directionsBackground, self.directionsText = self.drawDirections()
            

    def checkBoundsPlayer1(self, x1, y1):
       '''Checks the x and y coordinate values for Player 1, returning True if they are inside the defined 
       boundaries and False if they are not'''
       if 351<=x1<=751 and 500<=y1<=900:
           return True
       else:
           return False
      
    def checkBoundsPlayer2(self, x2, y2):
       '''Checks the x and y coordinate values for Player 2, returning True if they are inside the defined 
       boundaries and False if they are not'''
       if 100<=x2<=300 and 100<=y2<=800:
           return True
       else:
           return False
      
    def checkBoundsPlayer3(self, x3, y3):
       '''Checks the x and y coordinate values for Player 3, returning True if they are inside the defined 
       boundaries and False if they are not'''
       if 300<=x3<=700 and 100<=y3<=500:
           return True
       else:
           return False
      
    def checkBoundsPlayer4(self, x4, y4):
       '''Checks the x and y coordinate values for Player 4, returning True if they are inside the defined 
       boundaries and False if they are not'''
       if 700<=x4<=900 and 100<=y4<=800:
           return True
       else:
           return False
     
    def drawBall(self, x, y):
        '''Returns drawn ball (Circle object).'''
        ball = Circle(Point(x, y), 10)
        ball.setFill("white")
        ball.draw(self.win)
        return ball
     
    def drawPlayer(self, x, y):
        '''Returns drawn player (Circle object).'''
        player = Circle(Point(x, y), 25)
        player.setFill("blue4")
        player.draw(self.win)
        return player
    
    def drawPlayerNumber(self, x, y, number):
        '''Returns drawn player number (Text object).'''
        playerNumber = Text(Point(x, y), number)
        playerNumber.setSize(25)
        playerNumber.setFill("white")
        playerNumber.draw(self.win)
        return playerNumber

    def drawComputer(self, x, y):
        '''Returns drawn computer player/defender (Circle object).'''
        computer = Circle(Point(x, y), 25)
        computer.setFill("red4")
        computer.draw(self.win)
        return computer
    
    def getCoordinates(self, object):
       '''Returns x and y coordinates of given object.'''
       center = object.getCenter()
       x, y = center.getX(), center.getY()
       return x, y 

    def game(self):
      '''The game method contains all responses to user keyboard input. The method is divided into two parts: player 
      movement and passing.'''
      
      '''Initially sets the pass count to 0. This is necessary to determine when the user has won the game'''
      passCount = 0 
      

      while self.win.isOpen():
          key = self.win.checkKey()

          '''Starts game by removing game directions from GraphWin window'''
          if key == "Return":
                self.directionsBackground.undraw()      
                self.directionsText.undraw()         
          
          '''Moves player and ball objects based on user input of arrow keys. Does not move objects
          if player is not within restricted area (if checkBoundsPlayer is false). If a player has the ball
          (indicated by self.inPossession), both the player and the ball will move simultaneously.'''

          x1, y1 = self.getCoordinates(self.player1)
          x2, y2 = self.getCoordinates(self.player2)
          x3, y3 = self.getCoordinates(self.player3)
          x4, y4 = self.getCoordinates(self.player4) 

          if key == 'Up':
              if self.checkBoundsPlayer1(x1, y1-50):
                  self.player1.move(0, -50)
                  self.playerNumber1.move(0,-50)
                  if self.inPossession == 1:
                     self.ball.move(0,-50)
              if self.checkBoundsPlayer2(x2, y2-50):
                  self.player2.move(0, -50)  
                  self.playerNumber2.move(0,-50)
                  if self.inPossession == 2:
                     self.ball.move(0,-50)
              if self.checkBoundsPlayer3(x3, y3-50):
                self.player3.move(0, -50)
                self.playerNumber3.move(0,-50)
                if self.inPossession == 3:
                     self.ball.move(0,-50)
              if self.checkBoundsPlayer4(x4, y4-50):
                self.player4.move(0, -50)
                self.playerNumber4.move(0,-50)
                if self.inPossession == 4:
                     self.ball.move(0,-50)

          if key == 'Down':
              if self.checkBoundsPlayer1(x1, y1+50):
                  self.player1.move(0, 50)
                  self.playerNumber1.move(0, 50)
                  if self.inPossession == 1:
                     self.ball.move(0,50)
              if self.checkBoundsPlayer2(x2, y2+50):
                  self.player2.move(0, 50)
                  self.playerNumber2.move(0, 50)
                  if self.inPossession == 2:
                     self.ball.move(0,50)
              if self.checkBoundsPlayer3(x3, y3+50):
               self.player3.move(0, 50)
               self.playerNumber3.move(0, 50)
               if self.inPossession == 3:
                     self.ball.move(0,50)
              if self.checkBoundsPlayer4(x4, y4+50):
               self.player4.move(0, 50)
               self.playerNumber4.move(0, 50)
               if self.inPossession == 4:
                     self.ball.move(0,50)

          if key == 'Right':
              if self.checkBoundsPlayer1(x1+50, y1):
                  self.player1.move(50, 0)
                  self.playerNumber1.move(50, 0)
                  if self.inPossession == 1:
                     self.ball.move(50, 0)
              if self.checkBoundsPlayer2(x2+50, y2):
                  self.player2.move(50, 0)
                  self.playerNumber2.move(50, 0)
                  if self.inPossession == 2:
                     self.ball.move(50, 0)
              if self.checkBoundsPlayer3(x3+50, y3):
                self.player3.move(50, 0)
                self.playerNumber3.move(50, 0)
                if self.inPossession == 3:
                     self.ball.move(50, 0)
              if self.checkBoundsPlayer4(x4+50, y4):
                self.player4.move(50, 0)
                self.playerNumber4.move(50, 0)
                if self.inPossession == 4:
                     self.ball.move(50, 0)

          if key == 'Left':
              if self.checkBoundsPlayer1(x1-50, y1):
                  self.player1.move(-50, 0)
                  self.playerNumber1.move(-50, 0)
                  if self.inPossession == 1:
                     self.ball.move(-50, 0)
              if self.checkBoundsPlayer2(x2-50, y2):
                  self.player2.move(-50, 0)
                  self.playerNumber2.move(-50, 0)
                  if self.inPossession == 2:
                     self.ball.move(-50, 0)
              if self.checkBoundsPlayer3(x3-50, y3):
                 self.player3.move(-50, 0)
                 self.playerNumber3.move(-50, 0)
                 if self.inPossession == 3:
                     self.ball.move(-50, 0)
              if self.checkBoundsPlayer4(x4-50, y4):
                 self.player4.move(-50, 0)
                 self.playerNumber4.move(-50, 0)
                 if self.inPossession == 4:
                     self.ball.move(-50, 0)


          '''Completes passing animation depending on user keyboard input (number keys). Does not complete animation 
          if the chosen player already has the ball. Depending on the value of self.probability, the pass animation is 
          either completed and the variable count is increased by 1, or self.failPass is called to indicate a loss for 
          the user.'''           
        
          xball, yball = self.getCoordinates(self.ball)
          distance1 = self.calculateDistance(self.player1)
          distance2 = self.calculateDistance(self.player2)
          distance3 = self.calculateDistance(self.player3)
          distance4 = self.calculateDistance(self.player4)

    
          if key == '1' and (not (self.inPossession == 1)):
            if self.probability(distance1):

                '''Using the distance from the ball to the player, a pass is animated using a for loop. For each iteration of
                the loop, the ball moves at a rate of the difference in x values of the ball and player divded by the distance 
                and a rate of the difference in y values divded by the distance. The range of the for loop is divided by 10 to
                decrease the nubmer of iterations and move the ball in a faster and smoother fashion. (Sorry I hope this makes 
                sense)''' 

                for i in range(1, int(distance1/10)):
                    self.ball.move(((x1-xball)/distance1*10), ((y1-yball)/distance1*10))
               
                self.inPossession = 1
                passCount += 1
            else:
                self.failPass(self.computer2)

          elif key == '2' and (not (self.inPossession == 2)):
            if self.probability(distance2):
               for i in range(1, int(distance2/10)):
                    self.ball.move(((x2-xball)/distance2*10), ((y2-yball)/distance2*10))

               self.inPossession = 2
               passCount += 1
            else:
                self.failPass(self.computer3)

            
          elif key == '3' and (not (self.inPossession == 3)):
            if self.probability(distance3):
                for i in range(1, int(distance3/10)):
                    self.ball.move(((x3-xball)/distance3*10), ((y3-yball)/distance3*10))
                
                self.inPossession = 3
                passCount += 1
            else:
                rng = random.randint(1, 2)
                if rng == 1:
                    self.failPass(self.computer3)
                else: 
                    self.failPass(self.computer4)

          elif key == '4' and (not (self.inPossession == 4)):
                if self.probability(distance4):
                    for i in range(1, int(distance4/10)):
                        self.ball.move(((x4-xball)/distance4*10), ((y4-yball)/distance4*10))

                    self.inPossession = 4
                    passCount += 1
                else:
                    self.failPass(self.computer4)
            
          '''If the count variable reaches 5, self.drawSuccessScreen is called to indicate a win for 
          the user.'''
          if passCount == 5:
            self.drawSuccessScreen()


            
    def probability(self, distance):
        '''This method determines the probability of making a pass, depending on the distance between each player and the ball.
        If the distance is smaller, it is more likely that a user succesfully makes a pass. The probabilities in this code are
        80%, 60%, and 40%, depending on the distances.'''

        rng = random.randint(1, 10)
        if distance < 500:
            if rng <= 8:
                return True
            else:
                return False
        elif distance < 700:
            if rng <= 6:
                return True
            else:
                return False
        else:
            if rng <= 4:
                return True
            else:
                return False


    def calculateDistance(self, player):
        '''This method calculates a distance between the ball and a given player.'''
        xball, yball = self.getCoordinates(self.ball)
        x, y = self.getCoordinates(player)
        distance = math.sqrt(((xball-x)**2)+((yball-y)**2))
        return distance


    def failPass(self, computer):
        '''This method moves/animates the ball from a player who has the ball to one of the defenders (computer players)
        when self.probability decides that the user loses the ball. After moving the ball to one of the
        defenders, it calls the method of drawing the fail screen, letting the user know that they lost the game.'''


        xball, yball = self.getCoordinates(self.ball)
        xComp2, yComp2 = self.getCoordinates(self.computer2)
        xComp3, yComp3 = self.getCoordinates(self.computer3)
        xComp4, yComp4 = self.getCoordinates(self.computer4)
        distanceComp2 = self.calculateDistance(self.computer2)
        distanceComp3 = self.calculateDistance(self.computer3)
        distanceComp4 = self.calculateDistance(self.computer4)


        if computer == self.computer2:
            for i in range(1, int(distanceComp2/10)):
                self.ball.move(((xComp2-xball)/distanceComp2*10), ((yComp2-yball)/distanceComp2*10))
        if computer == self.computer3:
            for i in range(1, int(distanceComp3/10)):
                self.ball.move(((xComp3-xball)/distanceComp3*10), ((yComp3-yball)/distanceComp3*10))
        if computer == self.computer4:
            for i in range(1, int(distanceComp4/10)):
                self.ball.move(((xComp4-xball)/distanceComp4*10), ((yComp4-yball)/distanceComp4*10))
        self.drawFailScreen()


            
    def drawFailScreen(self):
        '''This method shows the screen when an user loses the game by failing a pass.'''
        failBackground = Rectangle(Point(250, 400), Point(750, 600))
        failBackground.setFill("black")
        failBackground.draw(self.win)
        failText = Text(Point(500, 500), "Sorry, you lose!")
        failText.setFill("white")
        failText.setSize(36)
        failText.draw(self.win)
        return failBackground, failText


    def drawSuccessScreen(self):
        '''This method shows the screen when an user wins the game by completing 5 passes.'''
        successBackground = Rectangle(Point(250, 400), Point(750, 600))
        successBackground.setFill("white")
        successBackground.draw(self.win)
        successText = Text(Point(500, 500), "Amazing, you win!")
        successText.setFill("blue")
        successText.setSize(36)
        successText.draw(self.win)
        return successBackground, successText


    def drawDirections(self):
        '''This method shows the directions of the game.'''
        directionsBackground = Rectangle(Point(250, 400), Point(750, 600))
        directionsBackground.setFill("white")
        directionsBackground.draw(self.win)
        directionsText = Text(Point(500, 500), "DIRECTIONS \n Arrow Keys: move players around \n 1, 2, 3, 4: Choose the player you want to pass to \n \n The goal of the game is to complete 5 passes. \n Press Enter/Return to start game.")
        directionsText.setFill("black")
        directionsText.setSize(18)
        directionsText.draw(self.win)
        return directionsBackground, directionsText


def main():
   win = GraphWin("final project", 1000, 1000)
   field = Background(win)
   soccer = Game(win)
  
   while win.isOpen():
       soccer.game()
      


main()