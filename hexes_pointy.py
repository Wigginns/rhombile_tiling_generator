#! python
import sys, random, requests, json
from PIL import Image, ImageDraw, ImageFont
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, IMAGE_HEIGHT, IMAGE_WIDTH
from color_generators import *

def pil_hex():
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    colors = color_generator()
    coords = hex_centers_grid()
    fnt =ImageFont.load_default().font
    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=next(colors), outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=next(colors), outline=128)
        # draw.polygon(list(hex_points(x,y)), outline=128)
        cc_x, cc_y = next(coords)
        current_center = str(cc_x) + "." + str(cc_y)
        #draw.text((x-10,y), current_center, font = fnt, fill="#000000")

    image.save('pil_hexes_pointy.png', 'PNG')


def pil_hex_tricolor():
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    colors = color_generator()
    coords = hex_centers_grid()
    fnt =ImageFont.load_default().font
    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=color_generator_n(n), outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=color_generator_n(n+2), outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=color_generator_n(n+4), outline=128)
        # draw.polygon(list(hex_points(x,y)), outline=255)
        cc_x, cc_y = next(coords)
        current_center = str(cc_x) + "." + str(cc_y)
        #draw.text((x-10,y), current_center, font = fnt, fill="#000000")

    image.save('pil_hexes_tricolor_pointy.png', 'PNG')

sys.stdout.write("hello from Python %s\n" % (sys.version,))

pil_hex()
pil_hex_tricolor()
