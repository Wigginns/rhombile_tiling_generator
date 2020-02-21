import cairocffi as cairo, sys, argparse, copy, math, random, cairosvg
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, hex_points, IMAGE_HEIGHT, IMAGE_WIDTH
from pprint import pprint
from color_generators import get_colormind_for_cairo

float_gen = lambda a, b: random.uniform(a, b)

# colors = []
# for i in range(15):
#     colors.append((float_gen(.4, .75), float_gen(.4, .75), float_gen(.4, .75)))

colors = get_colormind_for_cairo()

# ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, IMAGE_WIDTH, IMAGE_HEIGHT)
ims = cairo.SVGSurface("hexes.svg", IMAGE_WIDTH, IMAGE_HEIGHT)
ctx = cairo.Context(ims)
print(IMAGE_WIDTH, IMAGE_HEIGHT)

def hex_polygon(points, fill):
    # ctx.set_source_rgba(random.choice(colors)[0], random.choice(colors)[1], random.choice(colors)[2], 5)
    
    # r,g,b = random.choice(colors[0:3])
    r,g,b = fill
    ctx.set_source_rgba(r,g,b, 5)

    for i in range(len(points)):
        ctx.line_to(points[i][0], points[i][1])
        # ctx.stroke()

    ctx.fill()


def main():

    # setup image and set background 
    ctx.set_source_rgb(0.9, 0.9, 0.9)
    ctx.rectangle(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT)
    ctx.fill()

    ctx.set_line_width(10)

    # for n in range(0,6,2):
    #         print("n: ")
    #         print(n)

    for x,y in hex_centers():
        n = random.randint(0,100)
        
        hex_polygon((list(rhombus_points_next3(x,y,n)) + [(x,y)]), fill=colors[n%3])
        hex_polygon((list(rhombus_points_next3(x,y,n+2)) + [(x,y)]), fill=colors[(n+2)%3])
        hex_polygon((list(rhombus_points_next3(x,y,n+4)) + [(x,y)]), fill=colors[(n+4)%3])
        
 
    # cairosvg.svg2png(file_obj=open(r'C:\Users\Benjamin\github\rhombile_tiling_generator\hexes.svg',"rb"), 
    #     write_to=r'C:\Users\Benjamin\github\rhombile_tiling_generator\examples\hexes.png')
    
   
if __name__ == "__main__":
    main()