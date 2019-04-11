#! python
import sys, random, requests, json
from PIL import Image, ImageDraw, ImageFont
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, IMAGE_HEIGHT, IMAGE_WIDTH
from color_generators import *

def gen_multicolor():
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
        # cc_x, cc_y = next(coords)
        # current_center = str(cc_x) + "." + str(cc_y)
        # draw.text((x-10,y), current_center, font = fnt, fill="#000000")

    image.save('megacolor.png', 'PNG')


def gen_tricolor():
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))

    coords = hex_centers_grid()
    # fnt =ImageFont.load_default().font
    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=color_generator_n(n), outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=color_generator_n(n+2), outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=color_generator_n(n+4), outline=128)
        # draw.polygon(list(hex_points(x,y)), outline=255)
        # cc_x, cc_y = next(coords)
        # current_center = str(cc_x) + "." + str(cc_y)
        # draw.text((x-10,y), current_center, font = fnt, fill="#000000")

    image.save('tricolor.png', 'PNG')

def gen_colormind():
    data = '{"model":"default"}'
    response = requests.post('http://colormind.io/api/', data=data)

    json_string = response.json() #convert to dict

    colors = list()
    for rgb in json_string['result']:
        colors.append(tuple(rgb))

    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    saved = False

    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        n = random.randint(0,5)

        if not saved:
            with open('colormind.txt', 'w') as fp:
                fp.write('\n'.join('({}, {}, {})'.format(c[0],c[1],c[2]) for c in colors))
            saved = True
        
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=colors[n%3], outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=colors[(n+2)%3], outline=128)
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=colors[(n+4)%3], outline=128)
    
    image.save('colormind.png', 'PNG')



sys.stdout.write("hello from Python %s\n" % (sys.version,))


gen_multicolor()
gen_tricolor()
gen_colormind()
