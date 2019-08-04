#!/bin/bash

TESTNUM=0
echo -en "\033[01mＴｅｘｔ  ｆｏｒｍａｔｔｉｎｇ  ｔｅｓｔ：\033[m\n"
for TEXT in {"Reguar","Bold","Dim","Italics","Underlkne","Blink","Not Used","Reversed","Hidden","Strike Thru"}; do
	echo -en "\n "$TEXT":\r\033[18C"
	for TEST in "$TESTNUM"; do
		echo -en "\033[m[ \033["$TEST"m TEST \033[m ]"
		TESTNUM=$((TESTNUM + 1))
	done
done
echo -e "\n\n"

