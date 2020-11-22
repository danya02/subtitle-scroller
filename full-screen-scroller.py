#!/usr/bin/python3
import time
import os
import random
name = input('')
text = open(name+'.txt').read().split('~')
labels = list(map(lambda x: float(x.split()[0]), open(name+'-labels.txt').read().strip().split('\n')))

parts = []

def sleep(how_long):
#    how_long /= 10
    target = time.time() + how_long
    while time.time() < target: pass

def output_part(textpart):
#    print('printing', repr(textpart), 'delay', time_per_symbol)
    for char, time in textpart:
        if char == '`': os.system('clear')
        else: print(char, flush=True, end='')
        sleep(time)
#        print(time)

current_time = 0
for textpart, timestamp in zip(text, labels):
    time_to_print_part = timestamp - current_time
#    print(time_to_print_part, repr(textpart))
    if len(textpart) == 0:
        parts.append(time_to_print_part)
        continue
    time_per_symbol = time_to_print_part / len(textpart)
    durations = [time_per_symbol] * len(textpart)
    for i in range(len(durations)//2):
        offset = random.random() / 5 # up to 20 percent difference
        offset = offset * time_per_symbol
        durations[i] += offset
        durations[-1-i] -= offset
    random.shuffle(durations)
    text = zip(textpart, durations)
    parts.append(text)
    current_time = timestamp

os.system('clear')
#input()

for what in parts:
    if isinstance(what, float): time.sleep(what)
    else: output_part(what)
