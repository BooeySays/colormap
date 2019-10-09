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

def __cmap2():
	print("\n\n[01mＥｘｔｒａ ｃｏｌｏｒｓ ：[m\n")
	xxx=16
	while xxx < 231:
		while xxx < 100:
			print("[01m " + str(xxx) + "[m:[00;38;5;" + str(xxx) + "m▆▆▆▆▆▆[m  ", end='')
			xxx = int(int(xxx) + 1)
			print("[01m " + str(xxx) + "[m:[00;38;5;" + str(xxx) + "m▆▆▆▆▆▆[m  ", end='')
			xxx = int(int(xxx) + 1)
			print("[01m " + str(xxx) + "[m:[00;38;5;" + str(xxx) + "m▆▆▆▆▆▆[m  ", end='')
			xxx = int(int(xxx) + 1)
			print("[01m " + str(xxx) + "[m:[00;38;5;" + str(xxx) + "m▆▆▆▆▆▆[m  ", end='')
			xxx = int(int(xxx) + 1)
			print("[01m " + str(xxx) + "[m:[00;38;5;" + str(xxx) + "m▆▆▆▆▆▆[m  ", end='')
			xxx = int(int(xxx) + 1)
			print("[01m " + str(xxx) + "[m:[00;38;5;" + str(xxx) + "m▆▆▆▆▆▆[m  ")
			xxx = int(int(xxx) + 1)
#		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#		((xxx +=1))
#		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#		((xxx +=1))
#		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#		((xxx +=1))
#		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#		((xxx +=1))
#		echo -e "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#		((xxx +=1))
#	done
#	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#	((xxx +=1))
#	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#	((xxx +=1))
#	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#	((xxx +=1))
#	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#	((xxx +=1))
#	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#	((xxx +=1))
#	echo -e "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#	((xxx +=1))
#done
#}

__cmap2()
