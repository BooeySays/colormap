#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
	colorindex = sys.argv[1]
else:
	colorindex=0
initx=7


def drawcolor(colorindex):
	if len(str(colorindex)) == 1:
		startx=7
		color=int(colorindex)
		while startx > 0:
			print('\033[00;48;5;' + str(color) + 'm   ' + str(color) + ' \033[m ',end='')
#			print(str(color) + ': ' + '\033[00;48;5;' + str(color) + 'm  \033[m ',end='')
#			print(str(color) + ': ' + '\033[00;48;5;' + str(color) + 'm  \033[m ',end='')
			startx -= 1
			color += 1
	elif len(str(colorindex)) >= 2:
		startx=6
		color=int(colorindex)
		while startx > 0:
			if len(str(color)) == 2:
				print('\033[00;48;5;' + str(color) + 'm  ' + str(color) + ' \033[m ',end='')
				startx -= 1
				color += 1
			elif len(str(color)) == 3:
				print('\033[00;48;5;' + str(color) + 'm ' + str(color) + ' \033[m ',end='')
				startx -= 1
				color += 1
#		startx=6
#		color=int(colorindex)
#		while startx > 0:
#			print(str(color) + ': ' + '\033[00;48;5;' + str(color) + 'm  \033[m ',end='')
#			startx -= 1
#			color += 1


drawcolor(colorindex)