#!/bin/bash

DONE="\033[00;01m[ \033[00;01;32mDONE \033[00;01m]\033[m"
WAIT="\033[00;01m[ \033[00;01;38;5;190mWAIT \033[00;01m]\033[m"
FAIL="\033[00;01m[ \033[00;01;38;5;196mFAIL \033[00;01m]\033[m"

echo -e ""
echo -e -n "$WAIT Searching for \033[00;01;36m$HOME/.DX2/bin\033[00;01m ... \r"
if [ -d "$HOME/.DX2/bin" ]; then
	echo -e "$DONE"
	echo -e -n "$WAIT\tCopying script into $HOME/.DX2/bin ... \r";
	cp ./colormap "$HOME/.DX2/bin/colormap";
	echo -e "$DONE";
	chmod u+x "$HOME/.DX2/bin/colormap";
else
	echo -e "$FAIL"
	echo -e "\n\033[00;01;38;5;196mERROR \033[00;01m- DX2Setup was not found"
	echo -e ""
	echo -en """DX2Setup up sets up your system so that you can easily install
and/or remove scripts with out making any changes to the system's
current set up.

The script (colormap) needs to be copied into a bin directory that
is part of your system's \$PATH. If you choose to run DX2Setup now,
DX2Setup will create a seperate	bin directory, add the path to \$PATH,
and then copy the script into the new bin directory.

Otherwise, this setup will stop and you can manually copy the script
into the bin (or any other directory that is in \$PATH) directory of
your choosing.

Set up DX2Setup now? [\033[00;01;38;5;46mY\033[00;01m|\033[00;01;38;5;196mn\033[00;01m]: """
	read
	case $REPLY in
		'Y'|'y'|'')
			echo -e ""
			echo -e -n "$WAIT Downloading DX2Setup install script ...\r"
			wget -q https://raw.githubusercontent.com/BooeySays/SetupDx2/Release/Setup.py
			echo -e "$DONE"
			python3 ./Setup.py
			;;
		'n'|'N')
			echo -e "\nExiting setup ...\n"
			return
			;;
		*)
			echo -e "\ninvalid key selection\n\nExiting setup ...\n"
			return
			;;
	esac
fi