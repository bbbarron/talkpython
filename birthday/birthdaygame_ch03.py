# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:06:40 2016

@author: bbarron

The Birthday date game from
Talk Python to Me class
birthday_ch03.py
"""

import datetime


def print_header():
    print('------------------------------------------')
    print('              Birthday App')
    print('------------------------------------------')
    print()


def get_birthdate():
    print('Please enter your birthday as follows:\n')
    byear = int(input('Year[YYYY]:'))
    bmonth = int(input('Month[MM]:'))
    bday = int(input('Day[DD]:'))
    birthday = datetime.datetime (byear, bmonth, bday)
    return(birthday)


def compute_date_information():
    pass


def printout_birthday_info():
    pass

def main():
    print_header()
    get_birthdate()
    now = datetime.datetime.now()
#    compute_date_information(birthday, now)
    
    

main()