from random import shuffle
red = []
blue = []
white = []
k = 10
for x in range(k):
    red.append('R')
    blue.append('B')
    white.append('W')

print('\nred : {}'.format(red))
print('blue : {}'.format(blue))
print('white : {}\n'.format(white))

all_colors = []
all_colors = red + blue + white
shuffle(all_colors)

print('all colors : {}\n'.format(all_colors))

chosen_red = []
chosen_blue = []
chosen_white = []
for x in range(k*3):
    chosen_color = all_colors[x]

    if chosen_color == 'R':
        chosen_red.append('R')
    elif chosen_color == 'B':
        chosen_blue.append('B')
    elif chosen_color == 'W':
        chosen_white.append('W')

    if len(chosen_red) >= 4 or len(chosen_blue) >= 4 or len(chosen_white) >= 4:
        print('chosen ball count : {}'.format(x+1))
        print('chosen red : {} {} :'.format(chosen_red, len(chosen_red)))
        print('chosen blue : {} {} :'.format(chosen_blue, len(chosen_blue)))
        print('chosen white : {} {} :\n'.format(chosen_white, len(chosen_white)))
        break