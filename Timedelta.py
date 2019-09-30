

#HACKERRANK QUESTION

#You are given 2 timestamps in the format given below:
#Day dd Mon yyyy hh:mm:ss +xxxx
#Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between
#them.
#Input Format
#The first line contains , the number of testcases.
#Each testcase contains lines, representing time and time .
#Constraints
#Input contains only valid timestamps
#.
#Output Format
#Print the absolute difference in seconds.
#Sample Input 0
#2
#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000
#Sat 02 May 2015 19:54:36 +0530
#Fri 01 May 2015 13:54:36 -0000
#Sample Output 0
#25200
#88200


#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1=datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z' )
    t2=datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z' )
    #t1.replace(tzinfo=timezone.utc)
    #t1.replace(tzinfo=timezone.utc)

    t_delta=abs(t1-t2)
    return str(int(t_delta.total_seconds()))
    #print(t_delta.total_seconds())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
