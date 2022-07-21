#!/usr/local/bin/python3
import sys
import re


def contains_marker(line):
    return re.search('fillseq|overwrite|readseq|readrandom|readrand100K', line)
    
if __name__ == "__main__":
    file1 = open(sys.argv[1], 'r')
    lines = file1.readlines()

    markers = []
    line = 0
    for i in lines:
        m = contains_marker(i)
        if m != None:
            markers.append(line)
        line += 1

    for m in markers:
        print(lines[m])
        
