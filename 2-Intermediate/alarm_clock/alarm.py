import os
import sys
import argparse
from dateutil import parser
import datetime

p = argparse.ArgumentParser(description="Alarm Clock")
p.add_argument('time',type=str , help ="Time To Sound the Alarm")
args = p.parse_args()


def alarm():
    beep = lambda : os.system("echo -n '\a';sleep 0.2;" * 3)
    beep()

if __name__ == "__main__":

    try:
        date = parser.parse(args.time)
    except Exception as e:
        print(f"Error {e}\n")
        raise NotImplementedError

    current_date = date - datetime.datetime.now().today()
    if current_date.total_seconds() <= 0:
        raise "Time Has Passed"
    else:
        while current_date:
            current_date = date - datetime.datetime.now().today()
            if int(current_date.total_seconds()) == 0:
                alarm()
                break
