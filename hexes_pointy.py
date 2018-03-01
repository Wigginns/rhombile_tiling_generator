#! python
import sys, random
from PIL import Image, ImageDraw, ImageFont
from math import sin, cos, pi, sqrt, tan

THETA = pi / 3.0 # Angle from one point to the next
HEXES_HIGH = 10 # How many rows of hexes
HEXES_WIDE = 10 # How many hexes in a row
RADIUS = 60 # Size of a hex
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

def hex_centers():
    for x in range(HEXES_WIDE+2):
        for y in range(HEXES_HIGH+4):
            yield (x * HEX_WIDTH + (.5 * HEX_WIDTH * (y % 2))), ((y) * HEX_HEIGHT * 0.75)

def hex_centers_grid():
    for x in range(HEXES_WIDE+2):
        for y in range(HEXES_HIGH+4):
            yield x, y

def color_generator():
    colors_blue = [ '#00FFFF',  '#00FFFF',	 '#E0FFFF',	 '#AFEEEE',	 '#7FFFD4',	 '#40E0D0',	 '#48D1CC',	 '#00CED1',	 '#5F9EA0',	 '#4682B4',	 
                    '#B0C4DE',	'#B0E0E6',	 '#ADD8E6',	 '#87CEEB',	 '#87CEFA',	 '#00BFFF',	 '#1E90FF',	 '#6495ED',	 '#7B68EE',	 '#4169E1',	 
                    '#0000FF',	'#0000CD',	 '#00008B',	 '#000080',	 '#191970',	 
    ]
    colors_green = ['#ADFF2F',  '#7FFF00',  '#7CFC00',  '#00FF00',  '#32CD32',  '#98FB98',  '#90EE90',  '#00FA9A',  '#00FF7F',  '#3CB371',
                    '#2E8B57',  '#228B22',  '#008000',  '#006400',  '#9ACD32',  '#6B8E23',  '#808000',  '#556B2F',  '#66CDAA',  '#8FBC8F',
                    '#20B2AA',  '#008B8B',  '#008080',        
    ]
    colors_purple = ['#E6E6FA', '#D8BFD8',  '#DDA0DD',  '#EE82EE',  '#DA70D6',  '#FF00FF',  '#FF00FF',  '#BA55D3',  '#9370DB',  '#8A2BE2',
                     '#9400D3', '#9932CC',  '#8B008B',  '#800080',  '#4B0082',  '#6A5ACD',  '#483D8B',  '#7B68EE',
    ]
    colors_white = ['#FFFFFF',  '#FFFAFA',  '#F0FFF0',  '#F5FFFA',  '#F0FFFF',  '#F0F8FF',  '#F8F8FF',  '#F5F5F5',  '#FFF5EE',  '#F5F5DC',
                    '#FDF5E6',  '#FFFAF0',  '#FFFFF0',  '#FAEBD7',  '#FAF0E6',  '#FFF0F5',  '#FFE4E1',
    ]
    colors_all = colors_blue + colors_green + colors_purple
    colors = colors_white
    while True:
        random.shuffle(colors)    
        for color in colors:
            yield color

def pil_hex():
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    colors = color_generator()
    coords = hex_centers_grid()
    fnt =ImageFont.load_default().font
    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        #n = 0
        draw.polygon((list(rhombus_points_random(x,y,n)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_random(x,y,n+2)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_random(x,y,n+4)) + [x,y]), fill=next(colors), outline=128)
        # draw.polygon(list(hex_points(x,y)), outline=128)
        cc_x, cc_y = next(coords)
        current_center = str(cc_x) + "." + str(cc_y)
        draw.text((x-10,y), current_center, font = fnt, fill="#000000")
    
    image.save('pil_hexes_pointy.png', 'PNG')

sys.stdout.write("hello from Python %s\n" % (sys.version,))
pil_hex()
