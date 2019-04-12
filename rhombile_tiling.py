#! python
import sys, random, requests, json
from PIL import Image, ImageDraw, ImageFont
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, hex_points, IMAGE_HEIGHT, IMAGE_WIDTH
from color_generators import *
OUTLINE_VALUE = 0

def gen_multicolor(outline=False):
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    colors = color_generator()
    coords = hex_centers_grid()
    fnt =ImageFont.load_default().font
    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=next(colors))
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=next(colors))
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=next(colors))

        if outline:
            draw_outlines(draw,x,y,n)
        # draw.polygon(list(hex_points(x,y)), outline=128)
        # cc_x, cc_y = next(coords)
        # current_center = str(cc_x) + "." + str(cc_y)
        # draw.text((x-10,y), current_center, font = fnt, fill="#000000")

    image.save('megacolor.png', 'PNG')


def gen_tricolor(outline=False):
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))

    coords = hex_centers_grid()
    # fnt =ImageFont.load_default().font
    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        #draw.polygon(list(hex_points(x,y)), fill=next(colors), outline=128)
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=color_generator_n(n))
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=color_generator_n(n+2))
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=color_generator_n(n+4))

        if outline:
            draw_outlines(draw,x,y,n)
        # draw.polygon(list(hex_points(x,y)), outline=255)
        # cc_x, cc_y = next(coords)
        # current_center = str(cc_x) + "." + str(cc_y)
        # draw.text((x-10,y), current_center, font = fnt, fill="#000000")

    image.save('tricolor.png', 'PNG')

def gen_colormind(outline=False):
    img_filename = 'colormind'
    if outline:
        img_filename += '_outline'

    data = '{"model":"default"}'
    response = requests.post('http://colormind.io/api/', data=data)

    json_string = response.json() #convert to dict

    colors = list()  #add colors from dict to list of tuples for use later
    for rgb in json_string['result']:
        colors.append(tuple(rgb))
    random.shuffle(colors)

    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    saved = False

    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        n = random.randint(0,5)

        if not saved:
            with open(img_filename + '.txt', 'w') as fp:
                fp.write('Color Scheme: '+', '.join('({}, {}, {})'.format(c[0],c[1],c[2]) for c in colors))
                fp.write('\nRhombus Colors:')
                fp.write('\n'+'RGB({}, {}, {})'.format(*colors[n%3]))
                fp.write('\n'+'RGB({}, {}, {})'.format(*colors[(n+2)%3]))
                fp.write('\n'+'RGB({}, {}, {})'.format(*colors[(n+4)%3]))
            saved = True
        
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=colors[n%3])
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=colors[(n+2)%3])
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=colors[(n+4)%3])
        
        if outline:
            draw_outlines(draw,x,y,n)
    
    image.save(img_filename+'.png', 'PNG')

def draw_outlines(draw, hex_x, hex_y, n):
    draw.polygon((list(rhombus_points_next3(hex_x,hex_y,n)) + [hex_x,hex_y]), outline=OUTLINE_VALUE)
    draw.polygon((list(rhombus_points_next3(hex_x,hex_y,n+2)) + [hex_x,hex_y]), outline=OUTLINE_VALUE)
    draw.polygon((list(rhombus_points_next3(hex_x,hex_y,n+4)) + [hex_x,hex_y]), outline=OUTLINE_VALUE)

# sys.stdout.write("hello from Python %s\n" % (sys.version,))
print("Generating images...")


gen_multicolor()
gen_tricolor()
gen_colormind()
# gen_colormind()