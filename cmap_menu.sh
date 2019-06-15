#!/bin/bash

echo -en """
Which color map would you like displayed ?

  1.	Basic colors 0-15 (Bold and Normal)
  2.	16 - 232 (All the other shades)
  3.	232 - 256 (Grey to white) VERtiCAL
  4.	232 - 256 (Grey to white) VERtiCAL
  5.	Everything at once (with less)

  : """
read -n 1 -r WHICH_CLR_MAP
case $WHICH_CLR_MAP in
1)
	colormap1
	;;
2)
	colormap2
	;;
3)
	colormap3v
	;;
4)
	colormap3h
	;;
5)
	colormap4
	;;
*)
	
