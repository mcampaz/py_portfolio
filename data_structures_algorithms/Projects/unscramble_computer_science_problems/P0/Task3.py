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

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140."""

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

banglore_codes = []
for call_number in mobile_calls.keys():
    if call_number.startswith("7") or call_number.startswith("8") or call_number.startswith("9"):
        if call_number[:5] not in banglore_codes:
            banglore_codes.append(call_number[:5])
            print("mobile: ", call_number[:5])
print("mnum of mobile codes: ", len(banglore_codes))

for call_number in fixed_line_calls.keys():
    if call_number.startswith("(080)"):
        
        if call_number[:8] not in banglore_codes:
            banglore_codes.append(call_number[:8])
            print("fixed line: ", call_number[:8])
print("total num of mobile codes: ", len(banglore_codes))            
sorted_banglore_codes = sorted(banglore_codes)
print("The numbers called by people in Bangalore have codes:")
for code in sorted_banglore_codes:
    print(code)

"""
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
