#!/bin/bash

XXX=15

while [ "$XXX" -lt '232' ]; do
    LINE=1
    while [ "$LINE" -gt '0' ]; do
        for i in {"$((XXX + 1))","$((XXX + 2))","$((XXX + 3))","$((XXX + 4))","$((XXX + 5))","$((XXX + 6))"}; do
            printf '%03d' " $i"
            echo -en "[m:\033[38;5;"$i"m▆▆▆\033[m [01m"
        done
        echo
        LINE="$((LINE-1))"
    done
    XXX="$((XXX + 6))"
done

