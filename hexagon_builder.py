from math import sin, cos, pi, sqrt, tan

THETA = pi / 3.0 # Angle from one point to the next
HEXES_HIGH = 45 # How many rows of hexes
HEXES_WIDE = 55 # How many hexes in a row
RADIUS = 60 # Size of a hex
HEX_HEIGHT = RADIUS * 2
HEX_WIDTH = sqrt(3.0)/2.0 * HEX_HEIGHT
IMAGE_WIDTH = int(HEX_WIDTH * (HEXES_WIDE))
IMAGE_HEIGHT = int(HEX_HEIGHT * (HEXES_HIGH) * 0.6) #why is this too big?


def hex_points_next3(n):
    #return a valid hexagon starting corner and the 2 next sequential for given starting random int n
    return n%6, (n+1)%6, (n+2)%6

def hex_points(x,y):
    #Given x and y of the origin, return the six points around the origin of RADIUS distance
    for i in range(6):
        yield sin(THETA * i) * RADIUS + x, cos(THETA * i) * RADIUS + y #POINTYTOP

def rhombus_points1(x,y):
    #Given x and y of the origin, return rhombus points around the origin of RADIUS distance
    for i in range(1,4):
        yield sin(THETA * i) * RADIUS + x, cos(THETA * i) * RADIUS + y

def rhombus_points2(x,y):
    #Given x and y of the origin, return rhombus points around the origin of RADIUS distance
    for i in range(3, 6):
        yield sin(THETA * i) * RADIUS + x, cos(THETA * i) * RADIUS + y

def rhombus_points_next3(x,y,n):
    #inputs: x,y hexagon center coordinates, n random seed for starting corner
    #given n starting random number,  return the x,y coords of the rhombus generated by
    #the 3 corners and the center of the hex
    corners = list(hex_points_next3(n))
    for i in corners:
        yield sin(THETA * i) * RADIUS + x, cos(THETA * i) * RADIUS + y

def hex_centers():
    for x in range(HEXES_WIDE+2):
        for y in range(HEXES_HIGH+4):
            yield (x * HEX_WIDTH + (.5 * HEX_WIDTH * (y % 2))), ((y) * HEX_HEIGHT * 0.75)

def hex_centers_grid():
    for x in range(HEXES_WIDE+2):
        for y in range(HEXES_HIGH+4):
            yield x, y