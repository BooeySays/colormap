#!/usr/bin/env python3

import sys, os

initcount = 0

def cmap():
	print('[00;01mBasic Colors: [m')
	initcount = 0
	count = 7
#	print(' ' * 18 + '[00;01m[Basic: 0-7][m')
	while count >= 0:
#		print('[m  ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ': [38;5;' + str(initcount) + 'm▆▆▆▆[m ',end='')
		print('[m  ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ':[38;5;' + str(initcount) + 'm▆▆[m ',end='')
		initcount += 1
		count -= 1
	print('')
	count = 7
	while count >= 0:
#		print('[m  ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ': [38;5;' + str(initcount) + 'm▆▆▆▆[m ',end='')
		print('[m  ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ':[38;5;' + str(initcount) + 'm▆▆[m ',end='')
		initcount += 1
		count -= 1
	print('')
#	print(' ' * 18 + '[00;01m[Bold: 8-15][m\n')
	print('')
	print('[00;01mAdvanced colors: [m')
	initcount = 16
	while initcount < 232:
		countb = 6
		while countb > 0:
			count = 6
			while count > 0:
#				print('[m   ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ': [38;5;' + str(initcount) + 'm▆▆▆▆[m ',end='')
				print('[m   ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ':[38;5;' + str(initcount) + 'm▆▆▆[m ',end='')
				initcount += 1
				count -= 1
			countb -= 1
			print('')
		print('')
	print('[00;01mShades of grey: [m')
	while initcount < 256:
		count = 6
		while count > 0:
#			print('[m   ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ': [38;5;' + str(initcount) + 'm▆▆▆▆[m ',end='')
			print('[m   ' + '[' + str(len(str(initcount))) + 'D' + str(initcount) + ':[38;5;' + str(initcount) + 'm▆▆▆[m ',end='')
			initcount += 1
			count -= 1
		print('')


cmap()