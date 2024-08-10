#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string or isinstance(roman_string, str): 
        translate = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(roman_string)):
            if i > 0 and translate[roman_string[i]] > translate[roman_string[i - 1]]:
                num += translate[roman_string[i]] - 2 * translate[roman_string[i - 1]]
            else:
                num += translate[roman_string[i]]
        return num
    return 0