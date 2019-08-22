#!/bin/bash

__version__='2.3'

function cmap0(){
	TESTNUM=0
	FORMATCOLOR="\033[38;5;$(($RANDOM%231))m"
	echo -en "\n\n\033[01mＴｅｘｔ  ｆｏｒｍａｔｔｉｎｇ  ｔｅｓｔ：\033[m\n\n"
	echo -en "Random color used for this test: [\033[07m"$FORMATCOLOR"     \033[m]\n\n"
	for TEST in "$TESTNUM"; do
		for TEXT in {"Reguar","Bold","Dim","Italics","Underlkne","Blink","\033[01;07m N/A - NOT USED \033[m","Reversed","Hidden","Strike Thru"}; do
#			echo "$TEST"
#			echo -en "\033[m[ \033["$TEST"m"$FORMATCOLOR" TEST \033[m ]"
			echo -en " \033[m[\033["$TEST"m"$FORMATCOLOR" TEST \033[m]"
			echo -e " "$TEXT""
			TEST=$((TEST + 1))
		done
	done
	unset FORMATCOLOR TESTNUM TEST TEXT
}


function cmap1()
{

	xxx=0
	echo -e "[01m\n\nＢａｓｉｃ ｃｏｌｏｒｓ：\n[m"
#	while [ "$xxx" -lt 17 ]; do
#		while [ "$xxx" -lt 8 ]; do
## CMAP1 BAR SET 1
			printf '\033[00;07m'
			python3 -c "print(' ' * 63 + '\n' + ' ' * 63 + '\r Regular ( on white BG )')"
#			python3 -c "print(' ' * 63)"
#			echo -en "\033[01mRegr (on white):\033[00;07m\n"
#			printf '\n'
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			((xxx +=1))
			printf '\n'
## CMAP1 BAR SET 2
#			echo -e "BOLD / BRIGHT"
#		done
#	echo -en "\033[01mBold:\033[m"
			echo -en "[00;07m "$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			echo -en "[00;07m"$xxx":[00;07;48;5;"$xxx"m▆▆▆▆[00;07m "
			xxx=$((xxx + 1))
			printf '\n\033[00;07m'
			python -c "print(' ' * 63 + '\n\033[00;38;5;196m' + '-' * 63)"
			printf '\033[00;40m'
			xxx=0
## CMAP1 BAR SET 3
			python3 -c "print(' ' * 63 + '\n' + ' ' * 63 + '\r Regular ( on black BG )')"
#			python3 -c "print(' ' * 63)"
#			echo -en "\033[01mRegr (on white):\033[00;07m\n"
#			printf '\n'
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -e "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
## CMAP1 BAR SET 4
			echo -en "[00;40m "$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			echo -en "[00;40m"$xxx":[00;40;38;5;"$xxx"m▆▆▆▆[00;40m "
			((xxx +=1))
			printf '\n\033[00;40m'


			printf '\n'
			echo -en "\033[00;07m\n\n"
#echo -e "\n\033[m\033[01m[BOLD]\033[m"

echo
#			figlet -c -w 62 -f term '[REGULAR]'
#			echo -e "NORMAL"
#			echo -e """
#NOTE:
#0 - 7  are the same as 30 - 37 WITHOUT bold
#8 - 15 are the same colors are 30-37, when used with 01 (BOLD)

#"""
#	done
}


function cmap2()
{
echo -e "\n\n[01mＥｘｔｒａ ｃｏｌｏｒｓ ：[m\n"
xxx=16
while [ $xxx -lt 231 ]; do
	while [ $xxx -lt 100 ]; do
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -e "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
	done
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -e "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
done
}

function cmap3(){
if [ "$COLUMNS" -gt '97' ]; then
	echo -e "\n\n\033[01mＳｈａｄｅｓ  ｏｆ  ｇｒｅｙ (ｈｏｒｉｚｏｎｔａｌ)：\033[m\n"
	if [ $COLUMNS -gt 95 ]; then
		h3count=232
		echo 2{32..55}
		while [ $h3count -lt 256 ]; do
			echo -en "\e[48;5;"$h3count"m   \e[m"
			echo -en " "
			h3count=$((h3count + 1))
		done
		echo -e "\n\n"
	fi
else
	xxx=232
	echo -e """\n\n\033[01mＳｈａｄｅｓ  ｏｆ  ｇｒｅｙ (ｖｅｒｔｉｃａｌ):\033[m
Note: \033[3mThe verticle version of this table is being
      displayed because the terminal is not wide
      enough to display the horizontal table prop-
      erly. To show the Horizontal table, increase
      the terminal's width to 96 cols or more.\033[m
"""

	while [ $xxx -lt 256 ]; do
		echo -e "[38;5;15m "$xxx"   [48;5;"$xxx"m     [m  "
		((xxx +=1))
	done
fi
}

function __cmapall(){
#	FORMATCOLOR="\033[38;5;$(($RANDOM%231))m"
	cmap0;
#	unset FORMATCOLOR
	cmap1;
	cmap2;
    cmap3;
    #echo -e ""
    figlet -f term -c -w 77 " ------ END OF FILE ------ "
    echo -e "\n\n"

}

function cmap(){
    __cmapall | less -r -P 'Space to advance a screen' -e
}

function shades_grey(){
	g=232
	while [ $g -lt 256 ]; do
		echo -en "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
		((g +=1))
		echo -en "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
		((g +=1))
		echo -en "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
		((g +=1))
		echo -e "\033[38;5;15m\033[48;5;"$g"m "$g" \033[m\t"
		((g +=1))
	done
}

#CHANGELOG
# v2.3 - 190822
#  - Changed cmap1 to include the color bars on white and black bg
#
# v2.2 - 190821
#
# testformatting() / cmap0:
#  -	Edited textformatting to show the TEST bar first, followed by
#	the format desc
#		 -	Added colors for the test bar
# -	renamed to cmap0()
#
# __cmap1():
# -	renamed to cmap1()
#
# __cmap2():
# -	renamed to cmap2()
#
# __cmap3h() / __cmap3v():
# -	combined both into one function called cmap3
#
# v2.1
#
# -	added testformatting() to display a text using all the different
#	formatting options, to see which ones work and which doesn't