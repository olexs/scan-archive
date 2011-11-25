#! /usr/bin/python
import sys, os
from datetime import datetime
from dateutil.relativedelta import relativedelta

archive_from = "/home/vima/Picasa/VIMA"
archive_to = "/home/vima/Picasa/VIMA/VIMA_LAGER"

d_format = "%d.%m.%y"

start = datetime.strptime('01.01.11', d_format)
end = datetime.now() + relativedelta( days = -7 )

for line in os.listdir(archive_from):
    try:
        date = datetime.strptime(line.split()[0], d_format)
        if start <= date < end:
            sys.stdout.write(line)
    except (ValueError, IndexError):
        pass 