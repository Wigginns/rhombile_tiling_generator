#! python
import sys, random
from PIL import Image, ImageDraw
from math import sin, cos, pi, sqrt, tan

THETA = pi / 3.0 # Angle from one point to the next
HEXES_HIGH = 5 # How many rows of hexes
HEXES_WIDE = 8 # How many hexes in a row
RADIUS = 90 # Size of a hex
HEX_HEIGHT = RADIUS * 2
HEX_WIDTH = sqrt(3.0)/2.0 * HEX_HEIGHT
IMAGE_WIDTH = int(HEX_WIDTH * (HEXES_WIDE))
IMAGE_HEIGHT = int(HEX_HEIGHT * (HEXES_HIGH))

def hex_points_random3(n):
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

def rhombus_points_random(x,y,n):
    corners = list(hex_points_random3(n))
    for i in corners:
        yield sin(THETA * i) * RADIUS + x, cos(THETA * i) * RADIUS + y

def hex_centres():
    for x in range(HEXES_WIDE):
        for y in range(HEXES_HIGH):
            yield (x * HEX_WIDTH + (0.5 * HEX_WIDTH * (y % 2))), ((y+1.25) * HEX_HEIGHT * 0.75)


def color_generator():
    while True:
        yield 255, 0, 0 # red
        yield 255, 0, 255 # magenta
        yield 0, 0, 255 # blue
        yield 255, 255, 0 # yellow
        yield 0, 255, 0 # green
        yield 0, 255, 255 # cyan
        yield 192,192,192 # Silver
        yield 128,128,128 #Gray
        yield 128,0,0 #Maroon
        yield 128,128,0 #Olive
        yield 0,128,0 #Green
        yield 128,0,128 #Purple
        yield 0,128,128 #Teal
        yield 0,0,128 #Navy

def pil_hex():
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    colors = color_generator()
    draw = ImageDraw.Draw(image)
    for x,y in hex_centres():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        # draw.polygon((list(rhombus_points1(x,y)) + [x,y]), fill=next(colors), outline=128)
        # draw.polygon((list(rhombus_points2(x,y)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_random(x,y,n)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_random(x,y,n+2)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_random(x,y,n+4)) + [x,y]), fill=next(colors), outline=128)
        # draw.polygon(list(hex_points(x,y)), fill=next(colors))
        # draw.polygon((list(rhombus_points1(x,y)) + [x,y]), fill=next(colors))
        # draw.polygon((list(rhombus_points2(x,y)) + [x,y]), fill=next(colors))
    image.save('pil_hexes_pointy.png', 'PNG')

sys.stdout.write("hello from Python %s\n" % (sys.version,))
pil_hex()
