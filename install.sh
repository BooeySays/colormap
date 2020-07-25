#!/bin/bash

WAIT=" \033[00;01;38;5;190m[\033[38;5;15mWAIT\033[38;5;190m]\033[m "
PASS=" \033[00;01;38;5;46m[\033[38;5;15mPASS\033[38;5;46m]\033[m "
DONE=" \033[00;01;38;5;46m[\033[38;5;15mDONE\033[38;5;46m]\033[m "
FAIL=" \033[00;01;38;5;196m[\033[38;5;15mFAIL\033[38;5;196m]\033[m "

#echo -en "$WAIT Preparing ...";
{
	sudo apt-get
} &> /dev/null;
#echo -e "\r$DONE"
#if $(! command -v make &> /dev/null) || $(! command -v wget &> /dev/null); then
#	echo -e "There are some apps missing, that are required..."
#	echo -e "Please provide root privledges..."
#	{
#	sudo apt-get update -y
#	} &> /dev/null;
#fi

if $(! command -v make &> /dev/null) || $(! command -v wget &> /dev/null); then
	echo -en "$WAIT Updating apt-get repo ..."
	sudo apt-get update -y &> /dev/null;
	echo -e "\r$DONE"
fi

echo -en "$WAIT Checking for SetupDX2 ...";
if [ ! -d "$HOME/.DX2" ]; then
	echo -e "\r$FAIL";
	echo -e "Installing SetupDX2 ...";
	echo -en "$WAIT Checking for wget ...";
	if $(! command -v wget &> /dev/null); then
		echo -e "\r$FAIL";
		echo -en "\t$WAIT Installing wget ...";
		sudo apt-get install wget -y &> /dev/null;
		echo -e "\r\t$DONE";
	fi
	echo -en "$WAIT Downloading SetupDX2 set up files ...";
	wget -q https://raw.githubusercontent.com/BooeySays/SetupDx2/Release/Setup.py;
	echo -e "\r$PASS";
	echo -en "$WAIT Setting up SetupDX2 ...";
	python3 ./Setup.py;
	echo -e "\r$PASS";
	echo -en "$WAIT Checking for make ...";
	if $(! command -v make &> /dev/null); then
		echo -e "\r$FAIL";
		echo -en "\t$WAIT Installing make ...";
		sudo apt-get install make -y &> /dev/null;
		echo -e "\r\t$DONE";
	else
		echo -e "\r$PASS";
	fi
	echo -en "$WAIT Installing colormap files ...";
	make -s;
	echo -e "\r$PASS";
else
	echo -e "\r$PASS"
	echo -en "$WAIT Checking for make ...";
	if $(! command -v make &> /dev/null); then
		echo -e "\r$FAIL";
		echo -en "\t$WAIT Installing make ...";
		{
		sudo apt-get install make -y;
		}  &> /dev/null;
		echo -e "\r\t$DONE";
	else
		echo -e "\r$PASS";
	fi
	echo -en "$WAIT Installing colormap files ...";
	make -s;
	echo -e "\r$PASS";
#	if $(! command -v make &> /dev/null); then
#		sudo apt-get update -y && sudo apt-get install make -y;
#	fi
#	make -s;
fi
