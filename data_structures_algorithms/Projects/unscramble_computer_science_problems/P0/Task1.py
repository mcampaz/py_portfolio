"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
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
                fixed_lines[connection[0]] = {connection[1]:[connection[2]]}
            if connection[1] not in fixed_lines[connection[0]]:
                fixed_lines[connection[0]][connection[1]] = [connection[2]]
            else:
                fixed_lines[connection[0]][connection[1]].append(connection[2])
        elif connection[0].startswith('140'):
            if connection[0] not in telemarketers:
                telemarketers[connection[0]] = {connection[1]:[connection[2]]}
            if connection[1] not in telemarketers[connection[0]]:
                telemarketers[connection[0]][connection[1]] = [connection[2]]
            else:
                telemarketers[connection[0]][connection[1]].append(connection[2])
        else:
            if connection[0] not in mobiles:
                mobiles[connection[0]] = {connection[1]:[connection[2]]}
            if connection[1] not in mobiles[connection[0]]:
                mobiles[connection[0]][connection[1]] = [connection[2]]
            else:
                mobiles[connection[0]][connection[1]].append(connection[2])
    return fixed_lines, telemarketers, mobiles

fixed_line_texts, telemarketer_texts, mobile_texts = parsing_numbers(texts)
fixed_line_calls, telemarketer_calls, mobile_calls = parsing_numbers(calls)

different_numbers = []
for incoming, answering in mobile_texts.items():
    if incoming not in different_numbers:
        different_numbers.append(incoming)
    answering_number = list(answering.keys())[0]
    if answering_number not in different_numbers:
        different_numbers.append(answering_number)

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

for incoming, answering in mobile_calls.items():
    if incoming not in different_numbers:
        different_numbers.append(incoming)
    answering_number = list(answering.keys())[0]
    if answering_number not in different_numbers:
        different_numbers.append(answering_number)

print(different_numbers)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
print("There are {} different telephone numbers in the records.".format(len(different_numbers)))