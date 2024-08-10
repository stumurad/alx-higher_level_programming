#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and trans[roman_string[i]] > trans[roman_string[i - 1]]:
            num += trans[roman_string[i]]
            - 2 * trans[roman_string[i - 1]]
        else:
            num += trans[roman_string[i]]
    return num
