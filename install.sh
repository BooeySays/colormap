#!/bin/bash

## install.sh version 1.0

if [ -n "$DX2GIT" ]; then
	mkdir -p "$DX2GIT/colormap"
	cp * "$DX2GIT/colormap/"
fi

cp ./colormap "$DX2FUNCS/colormap.sh"
