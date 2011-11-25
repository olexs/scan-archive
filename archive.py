#! /usr/bin/python
import sys, os, shutil
from datetime import datetime
from dateutil.relativedelta import relativedelta

archive_from = "/home/vima/Picasa/VIMA"
archive_to = "/home/vima/Picasa/VIMA/VIMA_LAGER"

d_format = "%d.%m.%y"

end = datetime.now() + relativedelta( days = -7 )

log = open('archive-log.txt', 'w')
print >>log, datetime.now(), 'Starting archiving...'

for line in os.listdir(archive_from):
    try:
        date = datetime.strptime(line.split()[0], d_format)
        if date < end:
            shutil.move(archive_from+'/'+line, archive_to+'/'+line)
            print >>log, 'Moving:', line
    except (ValueError, IndexError):
        pass 

print >>log, datetime.now(), 'Archiving finished.'