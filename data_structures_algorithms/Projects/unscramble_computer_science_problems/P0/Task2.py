"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from datetime import datetime, timedelta
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def parsing_numbers(connections_data):
    fixed_lines = {}
    mobiles = {}
    telemarketers = {}
    for connection in connections_data:
        if connection[0][0] == '(':
            if connection[0] not in fixed_lines:
                fixed_lines[connection[0]] = {}
            if connection[1] not in fixed_lines[connection[0]]:
                fixed_lines[connection[0]][connection[1]] = [connection[2]]
            else:
                fixed_lines[connection[0]][connection[1]].append(connection[2])
        elif connection[0].startswith('140'):
            if connection[0] not in telemarketers:
                telemarketers[connection[0]] = {}
            if connection[1] not in telemarketers[connection[0]]:
                telemarketers[connection[0]][connection[1]] = [connection[2]]
            else:
                telemarketers[connection[0]][connection[1]].append(connection[2])
        else:
            if connection[0] not in mobiles:
                mobiles[connection[0]] = {}
            if connection[1] not in mobiles[connection[0]]:
                mobiles[connection[0]][connection[1]] = [connection[2]]
            else:
                mobiles[connection[0]][connection[1]].append(connection[2])
    return fixed_lines, telemarketers, mobiles

fixed_line_calls, telemarketer_calls, mobile_calls = parsing_numbers(calls)

different_numbers = []
for incoming, answering in fixed_line_calls.items():
    if incoming not in different_numbers:
        different_numbers.append(incoming)
    answering_number = list(answering.keys())[0]
    if answering_number not in different_numbers:
        different_numbers.append(answering_number)

for incoming, answering in telemarketer_calls.items():
    if incoming not in different_numbers:
        different_numbers.append(incoming)
    answering_number = list(answering.keys())[0]
    if answering_number not in different_numbers:
        different_numbers.append(answering_number)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_connected = {}
for incoming in fixed_line_calls:
    for answering in fixed_line_calls[incoming]:
        current_timer = timedelta()
        for timing in fixed_line_calls[incoming][answering]:
            time, duration = timing.split(" ")
            call_hours, call_minutes, call_seconds = duration.split(":")
            call_timer = timedelta(hours=int(call_hours), minutes=int(call_minutes), seconds=int(call_seconds))
            current_timer += call_timer
        if incoming not in time_connected.keys():
            time_connected[incoming] = current_timer
        else:
            time_connected[incoming] += current_timer
        if answering not in time_connected.keys():
            time_connected[answering] = current_timer
        else:
            time_connected[answering] += current_timer
            
for incoming in telemarketer_calls:
    for answering in telemarketer_calls[incoming]:
        current_timer = timedelta()
        for timing in telemarketer_calls[incoming][answering]:
            time, duration = timing.split(" ")
            call_hours, call_minutes, call_seconds = duration.split(":")
            call_timer = timedelta(hours=int(call_hours), minutes=int(call_minutes), seconds=int(call_seconds))
            current_timer += call_timer
        if incoming not in time_connected.keys():
            time_connected[incoming] = current_timer
        else:
            time_connected[incoming] += current_timer
        if answering not in time_connected.keys():
            time_connected[answering] = current_timer
        else:
            time_connected[answering] += current_timer       
        
for incoming in mobile_calls:
    for answering in mobile_calls[incoming]:
        current_timer = timedelta()
        for timing in mobile_calls[incoming][answering]:
            time, duration = timing.split(" ")
            call_hours, call_minutes, call_seconds = duration.split(":")
            call_timer = timedelta(hours=int(call_hours), minutes=int(call_minutes), seconds=int(call_seconds))
            current_timer += call_timer
        if incoming not in time_connected.keys():
            time_connected[incoming] = current_timer
        else:
            time_connected[incoming] += current_timer
        if answering not in time_connected.keys():
            time_connected[answering] = current_timer
        else:
            time_connected[answering] += current_timer

itemMaxValue = max(time_connected.items(), key=lambda x : x[1])
 
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(itemMaxValue[0], itemMaxValue[1].total_seconds()))
      