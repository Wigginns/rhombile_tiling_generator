import cairocffi as cairo
import random
from hexagon_builder import rhombus_points_next3, hex_centers_grid, hex_centers, hex_points, IMAGE_HEIGHT, IMAGE_WIDTH
from pprint import pprint
from color_generators import get_colormind_for_cairo

colors = get_colormind_for_cairo()
ims = cairo.SVGSurface("hexes.svg", IMAGE_WIDTH, IMAGE_HEIGHT)
ctx = cairo.Context(ims)

# draw a polygon from a given list of points with a given fill color
def draw_polygon(points, fill):
    r, g, b = fill
    ctx.set_source_rgba(r, g, b)

    for point in points:
        ctx.line_to(point[0], point[1])

    ctx.fill()


def given_facing_color(n):
    return random.randint(0, 100) % 3


def default_color(n):
    return n


def block_color(n):
    return n+1


def draw_hexes(color_func=default_color):
    n=0
    for x, y in hex_centers():
        n = color_func(n)

        for i in range(0,7,2):
            m = n + i
            draw_polygon((list(rhombus_points_next3(x, y, m)) + [(x,y)]), fill=colors[m % 3])


def main():
    # setup image and set background
    bg_color = colors[random.choice([3, 4])]
    ctx.set_source_rgb(bg_color[0], bg_color[1], bg_color[2])
    ctx.rectangle(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT)
    ctx.fill()

    draw_hexes()
    # draw_hexes(given_facing_color)
    # draw_hexes(block_color)

    # cairosvg.svg2png(file_obj=open(r'C:\Users\Benjamin\github\rhombile_tiling_generator\hexes.svg',"rb"),
    #     write_to=r'C:\Users\Benjamin\github\rhombile_tiling_generator\examples\hexes.png')

if __name__ == "__main__":
    main()
