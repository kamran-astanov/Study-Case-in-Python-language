#!/usr/bin/env python3

import sys
import os
step = ""

'''OPS435 Assignment 1 - Winter 2020
Program: a1_kastanov.py
Author: "Kamran Astanov"
The python code in this file (a1_kastanov.py) is original work written by
"Kamran Astanov". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.'''

def usage():
    """
    usage() -> str
        The usage() function will take no argument and return a
        tring describing the usage of the script.
        e.g. usage() -> "Usage: a1_kastanov.py [--step] YYYY-MM-DD +/-n"

     """

    print("Usage: a1_kastanov.py [--step] YYYY-MM-DD +/-n")
    exit()


def is_digit(number):
    """
    is_digit(number) -> str
        The is_digit(number) function will take argument and check
        if it is digit or includes also alphabet. Then will return
        True or False.
        e.g. is_digit("2020-10-01") -> "True"
             is_digit("20bc-10-01") -> "False"

    """
    a = '0123456789'
    for i in number:
        if i in a:
            return True
        else:
            return False


def leap_year(l_year):
    """
    leap_year (l_year) -> str
        The leap_year() function will take a year in "YYYY" format, and return True
        if the given year is a leap year, otherwise return False.
        e.g. leap_year("2020-10-11") -> "True"
             leap_year("2019-10-11") -> "False"

    """
    if is_digit(l_year):
         str_year, str_month, str_day = l_year.split('-')
         year = int(str_year)
         month = int(str_month)
         day = int(str_day)
         lyear = year % 4
         if lyear == 0:
            lyearstatus = "True"
         else:
            lyearstatus = "False"
         lyear = year % 100
         if lyear == 0:
             lyearstatus = "False"
         lyear = year % 400
         if lyear == 0:
             lyearstatus = "True"
         return (lyearstatus)


def days_in_mon(day_mon):
    """
    days_in_mon(day_mon) -> str
        The days_in_mon() function will take a year in "YYYY" format, and return
        a dictionary object which contains the total number of days in each month
        for the given year. The days_in_mon() function should make use of the leap_year() function.
        e.g. days_in_mon("2020-10-11") -> "{1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}"
             days_in_mon("2019-10-11") -> "{1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}"

    """
    if leap_year(day_mon) == "True":
        feb_max = 29
    else:
        feb_max = 28

    mon_days = {1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mon_days



def valid_date(date):
    """
    valid_date(date) -> str
        The valid_date(date) function will take a date in "YYYY-MM-DD" format, and return True
        if the given date is a valid date, otherwise return False plus an appropriate status message.
        The valid_date(date) function should make use of the days_in_mon() function.
        e.g. valid_date("2020-10-10") -> "True"
             valid_date("20201410") ->   "False" plus "Error: wrong date entered"
             valid_date("2020-14-10") -> "False" plus "Error: wrong month entered"
             valid_date("2020-12-32") -> "False" plus "Error: wrong day entered"

    """
    if len(date) != 10:
        print("Error: wrong date entered")
        sys.exit()

    if is_digit(date):
         str_year, str_month, str_day = date.split('-')
         year = int(str_year)
         month = int(str_month)
         real_days_mon = days_in_mon(date)
         day = int(str_day)
         if  month == 00 or month > 12:
             print("Error: wrong month entered")
             sys.exit()
         elif day == 00 or day > real_days_mon[month]:
              print("Error: wrong day entered")
              sys.exit()
         else:
             return True




def after(today):
    """
    after(today) -> str
        The after() function will take a date in "YYYY-MM-DD" format and return
        the date of the next day in the same format.
        e.g. after("2020-10-11") ->  "2020-10-12"
             after("2020-10-31") -> "2020-11-01"

    """

    if valid_date(today):
        str_year, str_month, str_day = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        mon_max = days_in_mon(today)
        tmp_day = day + 1  # next day
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month]  # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(year) + "-" + str(to_month).zfill(2) + "-" + str(to_day).zfill(2)

        return next_date



def before(today):
    """
    before(today) -> str
        The before() function will take a date in "YYYY-MM-DD" format and return
        the date of the previous day in the same format.
        e.g. after("2020-10-11") ->  "2020-10-10"
             after("2020-10-31") -> "2020-10-30"

    """

    if valid_date(today):
        str_year, str_month, str_day = today.split('-')
        year = int(str_year)
        month = int(str_month)
        previous_month = month - 1  # previous month
        if previous_month == 0:
           previous_month = 12
        day = int(str_day)
        mon_max = days_in_mon(today)
        tmp_day = day - 1  # previous day
        if tmp_day == 0:
            to_day = mon_max[previous_month]
            tmp_month = month - 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month == 0:
            to_month = 12
            year = year - 1  # previous year
        else:
            to_month = tmp_month + 0

        previous_date = str(year) + "-" + str(to_month).zfill(2) + "-" + str(to_day).zfill(2)

        return previous_date



def dbda(date, days):
   """
    dbda(date, days) -> str
        The dbda() function will take a date in "YYYY-MM-DD" format, a positive or
        negative integer, and return a date either before or after the given date
        according to the value of the given integer in the same format.
        e.g. dbda("2019-01-01 3") 2019-01-04
             dbda("2019-01-01 -1") 2018-12-31 """


   days = int(days)


   if days > 0:
    if step == "True":
        while days != 0:
          date = after(date)
          days = days - 1
          print(str(date))
    else:
            while days != 0:
                date = after(date)
                days = days - 1
            print(str(date))


   elif days < 0:
       if step == "True":
          while days != 0:
            date = before(date)
            days = days + 1
            print(str(date))
       else:
           while days != 0:
               date = before(date)
               days = days + 1
           print(str(date))

if __name__ == "__main__":
  if ((len(sys.argv) >= 5 or len(sys.argv) <= 2)):
   usage()
  if sys.argv[1] == "--step":
    step = "True"
    date = sys.argv[2]
    days = sys.argv[3]
    dbda(date,days)
  else:
    step = "False"
    date = sys.argv[1]
    days = sys.argv[2]
    dbda(date, days)











