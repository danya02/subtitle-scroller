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
