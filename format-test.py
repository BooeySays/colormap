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

testformatting()

#function testformatting(){
#	TESTNUM=0
#	echo -en "\n\n\033[01mＴｅｘｔ  ｆｏｒｍａｔｔｉｎｇ  ｔｅｓｔ：\033[m\n"
#	for TEXT in {"Reguar","Bold","Dim","Italics","Underlkne","Blink","Not Used","Reversed","Hidden","Strike Thru"}; do
#		echo -en "\n "$TEXT":\r\033[18C"
#		for TEST in "$TESTNUM"; do
#			echo -en "\033[m[ \033["$TEST"m TEST \033[m ]"
#			TESTNUM=$((TESTNUM + 1))
#		done
#	done
#	echo -e ""
#}
#
#
#function __cmap1()
#{
#	xxx=0
#	echo -e "[01m\n\nＢａｓｉｃ ｃｏｌｏｒｓ：\n[m"
##	while [ "$xxx" -lt 17 ]; do
##		while [ "$xxx" -lt 8 ]; do
#			echo -en "\033[01mRegr:\033[m"
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
##			echo -e "BOLD / BRIGHT"
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
#
#function __cmap2()
#{
#echo -e "\n\n[01mＥｘｔｒａ ｃｏｌｏｒｓ ：[m\n"
#xxx=16
#while [ $xxx -lt 231 ]; do
#	while [ $xxx -lt 100 ]; do
#		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
#		((xxx +=1))
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
#
#function __cmap3v(){
#xxx=232
#echo -e """\n\n\033[01mＳｈａｄｅｓ  ｏｆ  ｇｒｅｙ (ｖｅｒｔｉｃａｌ):\033[m
#Note: \033[3mThe verticle version of this table is being
#      displayed because the terminal is not wide
#      enough to display the horizontal table prop-
#      erly. To show the Horizontal table, increase
#      the terminal's width to 96 cols or more.\033[m
#"""
#
#while [ $xxx -lt 256 ]; do
#		echo -e "[38;5;15m "$xxx"   [48;5;"$xxx"m     [m  "
#		((xxx +=1))
#done
#}
#
#function __cmap3h(){
#echo -e "\n\n\033[01mＳｈａｄｅｓ  ｏｆ  ｇｒｅｙ (ｈｏｒｉｚｏｎｔａｌ)：\033[m\n"
#if [ $COLUMNS -gt 95 ]; then
#	h3count=232
#	echo 2{32..55}
#	while [ $h3count -lt 256 ]; do
#		echo -en "\e[48;5;"$h3count"m   \e[m"
#		echo -en " "
#		h3count=$((h3count + 1))
#	done
#	echo -e "\n\n"
#fi
#}
#
#function __cmapall(){
#	testformatting
#	__cmap1
#	__cmap2
#    if [ "$COLUMNS" -gt '97' ]; then
#        __cmap3h
#    else
#        __cmap3v
#    fi
#    #echo -e ""
#    figlet -f term -c -w 77 " ------ END OF FILE ------ "
#    echo -e "\n\n"
#
#}
#
#function cmap(){
#    __cmapall | less -r -P 'Space to advance a screen' -e
#}
#
#function shades_grey(){
#	g=232
#	while [ $g -lt 256 ]; do
#		echo -en "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
#		((g +=1))
#		echo -en "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
#		((g +=1))
#		echo -en "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
#		((g +=1))
#		echo -e "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
#		((g +=1))
#	done
#}
#
#cmap
#unset -f testformatting shades_grey __cmapall __cmap1 __cmap2 __cmap3h __cmap3v cmap
