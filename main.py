#!/usr/bin/python3
import time
import json
import sys
sub = json.load(open("subtitles.json"))
magic = {  # some automagical codes
    "start_line": "\r",
    "clear_line": "\033[K"}
clear_line = False
for i in sub["sub"]:
    import os
    rows, columns = os.popen('stty size', 'r').read().split()
    rows = int(rows)
    columns = int(columns)
    if i["text"] == "...........":
        i["text"] = "FILL-IN"+"."*(columns-7)
    if i["text"] == "END":
        i["text"] = "END".center(columns, "-")
    if clear_line:
        clear_line = False
        sys.stdout.write(magic["clear_line"])
    symb_time = (i["time"]-i["final_delay"])/len(i["text"])
    for j in i["text"]:
        sys.stdout.write(j)
        sys.stdout.flush()
        time.sleep(symb_time)
    time.sleep(i["final_delay"])
    if i["clear"]:
        sys.stdout.write(magic["start_line"])
        clear_line = True
input()
