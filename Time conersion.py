import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time=re.search(r"(?P<hh>..):(?P<mm>..):(?P<ss>..)(?P<ampm>..)",s)
    hour=time.group('hh')
    if time.group('ampm')=='PM':
        if hour == '12':
            hr=12
        else:
            hr=str(int(hour)+12)
    else:
        if hour=='12':
            hr='00'
        else:
            hr=hour
    
    return(hr+":"+time.group('mm')+":"+time.group('ss'))
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
