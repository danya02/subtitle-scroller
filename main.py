#!/usr/bin/python3
import time
import json
sub = json.load(open("subtitles.json"))
magic = {  # some automagical codes
    "start_line": "\r",
    "clear_line": "\033[K"}
clear_line = False
for i in sub["sub"]:
    if clear_line:
        print(magic["clear_line"])
    symb_time = (i["time"]-i["final_delay"])/len(i["text"])
    for j in i["text"]:
        print(j, end="")
        time.sleep(symb_time)
    if i["clear"]:
        print(magic["start_line"])
        clear_line = True
