#!/usr/bin/python3
import json
outp={"sub":[]}
inp=open(input("Path to .srt file: ")).read().split("\n\n")
magic = {  # some automagical codes
    "start_line": "\r",
    "clear_line": "\033[K"}
n=0
e=0

max_delay=2
last_time=0.0
def min(*n):
    return sorted(n)[0]
def max(*n):
    return sorted(n, reverse=True)[0]
for i in inp:
    outp_block=[]
    print(magic["start_line"]+str(n)+"/"+str(len(inp))+" done ("+str(e)+" errors)"+magic["clear_line"], end="")
    #try:
    n=+1
    if len(i.split("\n"))==3:
        l1=i.split("\n")[0]
        l2=i.split("\n")[1]
        l3=i.split("\n")[2]
        time_in=l2.split(" --> ")[0]
        time_out=l2.split(" --> ")[1]
        time_out=int(time_out.split(":")[0])*3600+int(time_out.split(":")[1])*60+int(time_out.split(":")[2].split(",")[0])+int(time_out.split(":")[2].split(",")[1])*0.001
        time_in=int(time_in.split(":")[0])*3600+int(time_in.split(":")[1])*60+int(time_in.split(":")[2].split(",")[0])+int(time_in.split(":")[2].split(",")[1])*0.001
        time=time_out-time_in
        text=l3
        outp_block=[{"time":time_in-last_time, "text":"...........","clear":True,"final_delay":0},{"time": time, "text": text, "clear": True, "final_delay": min(time,max_delay)}]
        last_time=time_out
    elif len(i.split("\n"))==4:
        l1=i.split("\n")[0]
        l2=i.split("\n")[1]
        l3=i.split("\n")[2]
        l4=i.split("\n")[3]
        time_in=l2.split(" --> ")[0]
        time_out=l2.split(" --> ")[1]
        time_out=int(time_out.split(":")[0])*3600+int(time_out.split(":")[1])*60+int(time_out.split(":")[2].split(",")[0])+int(time_out.split(":")[2].split(",")[1])*0.001
        time_in=int(time_in.split(":")[0])*3600+int(time_in.split(":")[1])*60+int(time_in.split(":")[2].split(",")[0])+int(time_in.split(":")[2].split(",")[1])*0.001
        time=time_out-time_in
        time1=time*(len(l3)/len(l3+l4))
        time2=time*(len(l4)/len(l3+l4))
        outp_block=[{"time":time_in-last_time, "text":"...........","clear":True,"final_delay":0},{"time": time1, "text": l3+" ", "clear": False, "final_delay": min(max_delay,time1)},{"time": time2, "text": l4, "clear": True, "final_delay": min(time2, max_delay)}]
        last_time=time_out
    #else:
    #    raise ValueError
    #except:
    #    e+=1
    outp["sub"]=outp["sub"]+outp_block
print()
json.dump(outp, open(input("Output path: "), "w"))
