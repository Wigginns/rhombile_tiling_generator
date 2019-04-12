import random

#return 1 of 3 colors for specific rhombus orientations to create an illusion of shadows
def color_generator_n(n):
    colors_white = [ '#A9A9A9','#D3D3D3','#FAFAFA', ]
    return colors_white[n%3]

#return color from whichever semi random colorsheme you choose
def color_generator():
    colors_blue = [ '#00FFFF', '#E0FFFF', '#AFEEEE', '#7FFFD4', '#40E0D0', '#48D1CC',	 '#00CED1',	 '#5F9EA0',	 '#4682B4',
                    '#B0C4DE',	'#B0E0E6', '#ADD8E6', '#87CEEB', '#87CEFA', '#00BFFF', '#1E90FF',	 '#6495ED',	 '#7B68EE',	 '#4169E1',
                    '#0000FF',	'#0000CD', '#00008B', '#000080', '#191970',
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
    colors_all = colors_blue + colors_green + colors_purple +colors_white
    colors = colors_all
    while True:
        random.shuffle(colors)
        for color in colors:
            yield color
