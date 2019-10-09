#!/usr/bin/env python3

import sys, os, shutil

COLS, LINES = shutil.get_terminal_size()
__version__='2.1b'


def testformatting():
	formats = ["Reguar", "Bold", "Dim", "Italics", "Underlkne", "Blink", "Not Used", "Reversed", "Hidden", "Strike Thru"]
	x = 0
	print("\n\n\033[01mＴｅｘｔ  ｆｏｒｍａｔｔｉｎｇ  ｔｅｓｔ：\033[m\n")
	for TEXT in formats:
		print(" "+ TEXT + ":\r\033[18C", end='')
		print("\033[m[ \033[0" + str(x) + "m TEST \033[m ]")
		x = (int(x) + int(1))
	print('')


def __cmap1():
	xxx = 0
	print("[01m\n\nＢａｓｉｃ ｃｏｌｏｒｓ：\n[m")
	print("\033[00;01mRegr\033[m")
	while xxx < int('8'):
		print("[m " + "{:02d}".format(xxx) + ":[38;5;" + str(xxx) + "m▆▆▆▆[m ", end='')
		xxx = int(int(xxx) + 1)
	print('')
	while xxx < int('16'):
		print("[m " + "{:02d}".format(xxx) + ":[38;5;" + str(xxx) + "m▆▆▆▆[m ", end='')
		xxx = int(int(xxx) + 1)
	print('')
	print("\033[00;01mBold\033[m\n")
#
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -e "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
##			echo -e print("BOLD / BRIGHT"
##		done
#	echo -en "\033[01mBold:\033[m"
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m "$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m"$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m"$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m"$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m"$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m"$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
#			echo -en "[m"$xxx":[38;5;"$xxx"m▆▆▆▆[m "
#			((xxx +=1))
##echo -e "\n\033[m\033[01m[BOLD]\033[m"
#
#echo
##			figlet -c -w 62 -f term '[REGULAR]'
##			echo -e "NORMAL"
##			echo -e """
##NOTE:
##0 - 7  are the same as 30 - 37 WITHOUT bold
##8 - 15 are the same colors are 30-37, when used with 01 (BOLD)
#
##"""
##	done
#}
#
__cmap1()
