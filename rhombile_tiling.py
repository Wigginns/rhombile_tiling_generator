#! python
import sys, random
from PIL import Image, ImageDraw, ImageFont
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, hex_points, IMAGE_HEIGHT, IMAGE_WIDTH
from color_generators import *
OUTLINE_VALUE = 0

def gen_multicolor(outline=False):
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    colors = color_generator()

    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=next(colors))
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=next(colors))
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=next(colors))

        if outline:
            draw_outlines(draw,x,y,n)

    image.save('megacolor.png', 'PNG')


def gen_tricolor(outline=False):
    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))

    draw = ImageDraw.Draw(image)
    for x,y in hex_centers():
        n = random.randint(0,5)
        draw.polygon((list(rhombus_points_next3(x,y,n)) + [x,y]), fill=color_generator_n(n))
        draw.polygon((list(rhombus_points_next3(x,y,n+2)) + [x,y]), fill=color_generator_n(n+2))
        draw.polygon((list(rhombus_points_next3(x,y,n+4)) + [x,y]), fill=color_generator_n(n+4))

        if outline:
            draw_outlines(draw,x,y,n)

    image.save('tricolor.png', 'PNG')

def gen_colormind(outline=False):
    img_filename = 'colormind'
    if outline:
        img_filename += '_outline'

    colors = get_colormind_colors()

    image = Image.new("RGBA", (IMAGE_WIDTH,IMAGE_HEIGHT), (0,0,0,0))
    saved = False

    #start draw
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
    
    #end draw
    image.save(img_filename+'.png', 'PNG')

    crop_area = (1,1,1921,1081)
    cropped = image.crop(crop_area) #left, upper, right, lower pixel
    cropped.save(img_filename+'crop'+'.png', 'PNG')

def draw_rhombile_hexes(draw, hex_x, hex_y, n):
    return

def draw_outlines(draw, hex_x, hex_y, n):
    draw.polygon((list(rhombus_points_next3(hex_x,hex_y,n)) + [hex_x,hex_y]), outline=OUTLINE_VALUE)
    draw.polygon((list(rhombus_points_next3(hex_x,hex_y,n+2)) + [hex_x,hex_y]), outline=OUTLINE_VALUE)
    draw.polygon((list(rhombus_points_next3(hex_x,hex_y,n+4)) + [hex_x,hex_y]), outline=OUTLINE_VALUE)

# sys.stdout.write("hello from Python %s\n" % (sys.version,))
print("Generating images...")


# gen_multicolor()
# gen_tricolor()
gen_colormind()
# gen_colormind()