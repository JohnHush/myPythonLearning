# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        if type(width)!= int or type(height)!= int or width<=0 or height<=0:
            raise ValueError('width or height Value error!')
        
        self.width = width
        self.height = height

        # state is the value showing the tile is clean or NOT
        # if the tile is clean, state=True
        # if the tile is not clean, state=False

        self.state = {}
        for i in xrange(width):
            for j in xrange(height):
                self.state[(i,j)] = None
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        if 0 <=int(pos.getX())< self.width and 0 <=int(pos.getY())< self.height:
            self.state[( int(pos.getX()), int(pos.getY()) )] = True
        else:
            raise ValueError( 'Position value error!' )

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if 0 <=m< self.width and 0 <=n< self.height:
            if self.state[(m,n)] == True:
                return True
            else:
                return False
        else:
            raise ValueError( 'm, n value Error!' )
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for i in xrange( self.width ):
            for j in xrange( self.height ):
                if self.isTileCleaned( i , j ):
                    count = count +1
        return count

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position( random.random()*self.width , random.random()*self.height )

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <=pos.getX()< self.width and 0 <= pos.getY()< self.height:
            return True
        return False

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # position is a Position object
        # speed is a float
        # direction is an integer
        # room is a RectangularRoom Object
        self.position = room.getRandomPosition()
        self.speed = speed
        self.direction = random.randint( 0 , 359 )
        self.room = room

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.position = self.position.getNewPosition( self.direction , self.speed )
        self.room.cleanTileAtPosition( self.position )


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            NewPosition = self.position.getNewPosition( self.direction , self.speed )
            if self.room.isPositionInRoom( NewPosition ):
                self.position = NewPosition
                self.room.cleanTileAtPosition( self.position )
                break
            else:
                self.setRobotDirection( random.randint ( 0 , 359 ) )

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    itrial = 0 
    count  = 0
    while itrial < num_trials:
        itrial += 1
        # adding room
        room = RectangularRoom( width , height )
        # adding robots list
        robotlist = []
        for _ in range( num_robots ):
            robotlist.append(robot_type( room , speed ))
        # move the list of robots
        while room.getNumCleanedTiles() < int( min_coverage*width*height ):
            count += 1
            for robot in robotlist:
                robot.updatePositionAndClean()
    return count/num_trials

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    list_num_robots = range(1,10)
    list_count = []
    for num_robots in list_num_robots:
        list_count.append( runSimulation( num_robots , 1 , 20 , 20 , 0.8 , 20 , StandardRobot ) )

    pylab.plot( list_num_robots , list_count , 'bo' )
    pylab.xlabel( 'Number of robots ' )
    pylab.ylabel( 'Spending amount of Steps' )
    pylab.title( 'Relation between Number of robots and Spending steps' )
    pylab.show()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    ratio = []
    WidthHeight = [(20,20),(25,26),(40,10),(50,8),(80,5),(100,4)]
    list_count = []
    for iWidthHeight in WidthHeight:
        ratio.append( iWidthHeight[0]/iWidthHeight[1] )
        list_count.append( runSimulation( 1 , 1 , iWidthHeight[0] , iWidthHeight[1] , 0.8 , 50 , StandardRobot ) )

    pylab.plot( ratio , list_count , 'bo' )
    pylab.xlabel( 'Width height Ratio' )
    pylab.ylabel( 'Spending amount of Steps' )
    pylab.title( 'Relation between WidthHeightRatio and Spending steps' )
    pylab.show()
# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean( self ):
        self.setRobotDirection( random.randint( 0 , 359 ) )
        while not self.room.isPositionInRoom( self.position.getNewPosition( self.direction, self.speed) ):
            self.setRobotDirection( random.randint( 0 , 359 ) )

        self.position = self.position.getNewPosition( self.direction , self.speed )
        self.room.cleanTileAtPosition( self.position )

# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    pass
