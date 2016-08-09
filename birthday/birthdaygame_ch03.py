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
    print('-----------------------------------')
    print('        BIRTHDAY APP')
    print('-----------------------------------')
    print()


def get_birthdate():
    print('Please enter your birthday as follows:\n')
    byear = int(input('Year[YYYY]:'))
    bmonth = int(input('Month[MM]:'))
    bday = int(input('Day[DD]:'))
    birthday = datetime.datetime (byear, bmonth, bday)
    print(birthday)
    return birthday


def compute_date_information(given_date, now):
    date1 = datetime.datetime(now.year, given_date.month, given_date.day)
    date2 = now
    delta = date2 - date1
    days = int(delta.total_seconds() / 60 / 60 / 24)
    return days


def printout_birthday_info(num_days):
    if num_days > 0:
        print('You already had your birthday {} days ago'.format(num_days))
    elif num_days < 0:
        print('Your birthday will be here in {} days'.format(num_days))
    else:
        print('Congratulations! Today is your birthday')



def main():
    print_header()
    bday = get_birthdate()
    now = datetime.datetime.now()
    num_days = compute_date_information(bday, now)
    printout_birthday_info(num_days)


main()