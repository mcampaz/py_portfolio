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


# def slow_print(data):
#     for item in data:
#         yield item
#     
# the_texts = slow_print(texts)
# for i in range(100):
#     print(next(the_texts))
fixed_line_texts, telemarketer_texts, mobile_texts = parsing_numbers(texts)
fixed_line_calls, telemarketer_calls, mobile_calls = parsing_numbers(calls)



# print(parsing_numbers(texts))
print(parsing_numbers(calls))



"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
for incoming in mobile_texts:
    for answering in mobile_texts[incoming]:
            print("First record of texts, {} texts {} at time {}".format(incoming, answering, mobile_texts[incoming][answering][0]))
print()

for incoming in fixed_line_calls:
    for answering in fixed_line_calls[incoming]:
        time, duration = (fixed_line_calls[incoming][answering][-1]).split(" ")
        print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming, answering, time, duration))

for incoming in telemarketer_calls:
    for answering in telemarketer_calls[incoming]:
        time, duration = (telemarketer_calls[incoming][answering][-1]).split(" ")
        print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming, answering, time, duration))

for incoming in mobile_calls:
    for answering in mobile_calls[incoming]:
        time, duration = (mobile_calls[incoming][answering][-1]).split(" ")
        print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming, answering, time, duration))
