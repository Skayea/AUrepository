#!/bin/bash
df -h | awk '
NR > 1 { 
    fs = $1 
    percent = $5 
    
    gsub(/%/, "", percent)
    print fs, "|", percent "%"
    
    if (percent > 90) {
        print "Диск", fs, "заполнен более чем на 90%!"
    }
}'