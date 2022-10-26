from graphics import *
import random



RADIUS = 20
color = "blue"
WIN_WIDTH = 800
WIN_HEIGHT = 600

# instantiate window
win = GraphWin("window", WIN_WIDTH, WIN_HEIGHT)


# instantiate a point with (x, y) coordinates of (160, 120)
center = Point(WIN_WIDTH//2, WIN_HEIGHT//2)

#game message
message = Text(Point(WIN_WIDTH//2, WIN_HEIGHT//2), "PONG GAME")
message.setSize(15)
message.setFill("red")
message.draw(win)

del message

# instantiate ball with center at (160, 120)
ball = Circle(center, RADIUS)

# fill the circle with black
ball.setFill(color)

# draw the circle to the window
ball.draw(win)
xVelocity = .1
yVelocity = .1

#paddles
lp1 = Point(30,350)
lp2 = Point(40,225)
rp1 = Point(WIN_WIDTH-50, 350)
rp2 = Point(WIN_WIDTH-40, 225)

leftPaddle = Rectangle(lp1, lp2)
rightPaddle = Rectangle(rp1, rp2)

leftPaddle.setFill(color)
rightPaddle.setFill(color)

leftPaddle.draw(win)
rightPaddle.draw(win)

#original paddle movement


def paddleMove(leftPaddle, rightPaddle):
    user_event = win.checkKey()
    if user_event == "w":
        leftPaddle.move(0, -30)
    if user_event == "s":
        leftPaddle.move(0, 30)
    if user_event == "Up":
        rightPaddle.move(0, -30)
    if user_event == "Down":
        rightPaddle.move(0, 30)

rScore = 0
lScore = 0
   
lMessage = Text(Point(WIN_WIDTH//2+150, WIN_HEIGHT//2+100), "Right Score: "+str(lScore))
lMessage.setSize(30)
lMessage.draw(win)

rMessage = Text(Point(WIN_WIDTH//2-150, WIN_HEIGHT//2+100), "Left Score: "+str(rScore))
rMessage.setSize(30)
rMessage.draw(win)

while True:
   
    rPadPt = rightPaddle.getP2()
    rPadY = rPadPt.getY()
    lPadPt = leftPaddle.getP2()
    lPadY = lPadPt.getY()

   
    #rPadY is bottom of right paddle
    paddleMove(leftPaddle, rightPaddle)
   
    # move ball along x-axis
    ball.move(xVelocity, yVelocity)

    # get x-coordinate of circle
    centerBall = ball.getCenter()
    xBall = centerBall.getX()

    # get y-coordinate of circle
    yBall = centerBall.getY()

    # bounce off right edge of window
    #TODO
    if xBall+RADIUS>=WIN_WIDTH:
        xVelocity = xVelocity*-1
   
    # bounce off left edge of window
    #TODO
    if xBall-RADIUS<=0:
        xVelocity = xVelocity*-1
       
    # bounce off top
    if yBall+RADIUS>=WIN_HEIGHT:
        yVelocity = yVelocity*-1

    # bounce off bottom
    if yBall-RADIUS<=0:
        yVelocity = yVelocity*-1

    #bounce off of right paddle
    if xBall+RADIUS>=760 and yBall<=rPadY+125 and yBall>=rPadY:
        xVelocity = xVelocity*-1

    #bounce off of left paddle
    if xBall-RADIUS<=40 and yBall<=lPadY+125 and yBall>=lPadY:
        xVelocity = xVelocity*-1

    #score for left side (ball hits right wall)
    if xBall+RADIUS>=WIN_WIDTH:
        rScore=rScore+1
        rMessage.setText
        rMessage.setText("Left Score:"+str(rScore))
       
    #score for right side (ball hits left wall)
    if xBall-RADIUS<=0:
        lScore=lScore+1
        lMessage.setText("Right Score:"+str(lScore))
       
    # if there is a mouse click on window, close the window
    if win.checkMouse():
        win.close()
        break

exit(0)
