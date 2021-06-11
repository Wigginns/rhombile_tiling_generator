import cairocffi as cairo
import sys, argparse, copy, math, random
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, hex_points, IMAGE_HEIGHT, IMAGE_WIDTH
from pprint import pprint
from color_generators import get_colormind_for_cairo

# float_gen = lambda a, b: random.uniform(a, b)

# colors = []
# for i in range(15):
#     colors.append((float_gen(.4, .75), float_gen(.4, .75), float_gen(.4, .75)))

colors = get_colormind_for_cairo()

# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMAGE_WIDTH, IMAGE_HEIGHT)
ims = cairo.SVGSurface("hexes.svg", IMAGE_WIDTH, IMAGE_HEIGHT)
ctx = cairo.Context(ims)

#draw a polygon from a given list of points with a given fill color
def draw_polygon(points, fill):

    r,g,b = fill
    ctx.set_source_rgba(r,g,b)

    for i in range(len(points)):
        ctx.line_to(points[i][0], points[i][1])

    ctx.fill()

def given_facing_color(n):
    return random.randint(0,100)%3

def default_color(n):
    return n

def block_color(n):
    return n+1
    

def draw_hexes(color_func=default_color):
    n = 0
    for x,y in hex_centers():
        n = color_func(n)

        draw_polygon((list(rhombus_points_next3(x,y,n)) + [(x,y)]), fill=colors[n%3])
        draw_polygon((list(rhombus_points_next3(x,y,n+2)) + [(x,y)]), fill=colors[(n+2)%3])
        draw_polygon((list(rhombus_points_next3(x,y,n+4)) + [(x,y)]), fill=colors[(n+4)%3])

def main():

    # setup image and set background 
    
    bg_selection = random.choice([3,4])
    # ctx.set_source_rgb(0.9, 0.9, 0.9)
    ctx.set_source_rgb(colors[bg_selection][0],colors[bg_selection][1],colors[bg_selection][2])
    ctx.rectangle(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT)
    ctx.fill()

    # draw_hexes()
    # draw_hexes(given_facing_color)
    draw_hexes(block_color)
 
    # cairosvg.svg2png(file_obj=open(r'C:\Users\Benjamin\github\rhombile_tiling_generator\hexes.svg',"rb"), 
    #     write_to=r'C:\Users\Benjamin\github\rhombile_tiling_generator\examples\hexes.png')
    
   
if __name__ == "__main__":
    main()