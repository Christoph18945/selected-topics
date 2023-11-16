# Rats & Mazes
# First, create a Blackboard (cite reference) which is an object on which
# anyone may record information. This particular blackboard draws a maze,
# and is used as information comes back about the structure of a maze from
# the rats that are investigating it. Add Comment
# Now create the maze itself. Like a real maze, this object reveals very little
# information about itself — given a coordinate, it will tell you whether there
# are walls or spaces in the four directions immediately surrounding that
# coordinate, but no more. For starters, read the maze in from a text file but
# consider hunting on the internet for a maze-generating algorithm. In any
# event, the result should be an object that, given a maze coordinate, will
# report walls and spaces around that coordinate. Also, you must be able to
# ask it for an entry point to the maze. Add Comment
# Finally, create the maze-investigating Rat class. Each rat can
# communicate with both the blackboard to give the current information
# and the maze to request new information based on the current position of
# the rat. However, each time a rat reaches a decision point where the maze
# branches, it creates a new rat to go down each of the branches. Each rat is
# driven by its own thread. When a rat reaches a dead end, it terminates
# itself after reporting the results of its final investigation to the blackboard.
# Add Comment
# The goal is to completely map the maze, but you must also determine
# whether the end condition will be naturally found or whether the
# blackboard must be responsible for the decision. Add Comment
# An example implementation by Jeremy Meyer:
# # c13:Maze.py
# class Maze(Canvas):
# private Vector lines # a line is a char array
# private int width = -1
# private int height = -1
# public static void main (String [] args)
# throws IOException:
# if (args.length < 1):
# print “Enter filename“
# System.exit(0)
# Maze m = Maze()
# m.load(args[0])
# Frame f = Frame()
# f.setSize(m.width*20, m.height*20)
# f.add(m)
# Rat r = Rat(m, 0, 0)
# f.setVisible(1)
# def __init__(self):
# lines = Vector()
# setBackground(Color.lightGray)
# synchronized public boolean
# isEmptyXY(int x, int y):
# if (x < 0) x += width
# if (y < 0) y += height
# # Use mod arithmetic to bring rat in line:
# byte[] by =
# (byte[])(lines.elementAt(y%height))
# return by[x%width]==' '
# synchronized public void
# setXY(int x, int y, byte newByte):
# if (x < 0) x += width
# if (y < 0) y += height
# byte[] by =
# (byte[])(lines.elementAt(y%height))
# by[x%width] = newByte
# repaint()
# public void
# load(String filename) throws IOException:
# String currentLine = null
# BufferedReader br = BufferedReader(
# FileReader(filename))
# for(currentLine = br.readLine()
# currentLine != null
# currentLine = br.readLine()) :
# lines.addElement(currentLine.getBytes())
# if(width < 0 ||
# currentLine.getBytes().length > width)
# width = currentLine.getBytes().length
# height = len(lines)
# br.close()

# def update(self, Graphics g): paint(g)
# public void paint (Graphics g):
# int canvasHeight = self.getBounds().height
# int canvasWidth = self.getBounds().width
# if (height < 1 || width < 1)
# return # nothing to do
# int width =
# ((byte[])(lines.elementAt(0))).length
# for (int y = 0 y < len(lines) y++):
# byte[] b
# b = (byte[])(lines.elementAt(y))
# for (int x = 0 x < width x++):
# switch(b[x]):
# case ' ': # empty part of maze
# g.setColor(Color.lightGray)
# g.fillRect(
# x*(canvasWidth/width),
# y*(canvasHeight/height),
# canvasWidth/width,
# canvasHeight/height)
# break
# case '*': # a wall
# g.setColor(Color.darkGray)
# g.fillRect(
# x*(canvasWidth/width),
# y*(canvasHeight/height),
# (canvasWidth/width)-1,
# (canvasHeight/height)-1)
# break
# default: # must be rat
# g.setColor(Color.red)
# g.fillOval(x*(canvasWidth/width),
# y*(canvasHeight/height),
# canvasWidth/width,
# canvasHeight/height)
# break


# # :~
# # c13:Rat.py
# class Rat:
# static int ratCount = 0
# private Maze prison
# private int vertDir = 0
# private int horizDir = 0
# private int x,y
# private int myRatNo = 0
# def __init__(self, Maze maze, int xStart, int
# yStart):
# myRatNo = ratCount++
# print ("Rat no." + myRatNo +
# " ready to scurry.")
# prison = maze
# x = xStart
# y = yStart
# prison.setXY(x,y, (byte)'R')
# Thread():
# def run(self){ scurry()
# .start()
# def scurry(self):
# # Try and maintain direction if possible.
# # Horizontal backward
# boolean ratCanMove = 1
# while(ratCanMove):
# ratCanMove = 0
# # South
# if (prison.isEmptyXY(x, y + 1)):
# vertDir = 1 horizDir = 0
# ratCanMove = 1

# # North
# if (prison.isEmptyXY(x, y - 1))
# if (ratCanMove)
# Rat(prison, x, y-1)
# # Rat can move already, so give
# # this choice to the next rat.
# else:
# vertDir = -1 horizDir = 0
# ratCanMove = 1

# # West
# if (prison.isEmptyXY(x-1, y))
# if (ratCanMove)
# Rat(prison, x-1, y)
# # Rat can move already, so give
# # this choice to the next rat.
# else:
# vertDir = 0 horizDir = -1
# ratCanMove = 1

# # East
# if (prison.isEmptyXY(x+1, y))
# if (ratCanMove)
# Rat(prison, x+1, y)
# # Rat can move already, so give
# # this choice to the next rat.
# else:
# vertDir = 0 horizDir = 1
# ratCanMove = 1

# if (ratCanMove): # Move original rat.
# x += horizDir
# y += vertDir
# prison.setXY(x,y,(byte)'R')
# # If not then the rat will die.
# try:
# Thread.sleep(2000)
# catch(InterruptedException ie):
# print ("Rat no." + myRatNo +
# " can't move..dying..aarrgggh.")
# # :~
# The maze initialization file: Add Comment
# #:! c13:Amaze.txt
# * ** * * ** *
# *** * ******* * ****
# *** ***
# ***** ********** *****
# * * * * ** ** * * * ** *
# * * * * ** * * * * **
# * ** * **
# * ** * ** * ** * **
# *** * *** ***** * *** **
# * * * * * *
# * ** * * * ** * *
# # :~
# Other maze resources
# A discussion of algorithms to create mazes as well as Java source code to
# implement them: Add Comment
# http://www.mazeworks.com/mazegen/mazegen.htm
# A discussion of algorithms for collision detection and other
# individual/group moving behavior for autonomous physical objects:
# http://www.red3d.com/cwr/steer/