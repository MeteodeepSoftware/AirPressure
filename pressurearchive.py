from time import sleep
from sense_hat import SenseHat

myAPI = ""

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
pressure = round(pressure, 1)
pressure = str(pressure)
	
target1 = open('/var/www/meteodeep/pressurearchiveddata.txt', 'w')
target1.write(pressure)
target1.close()

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

f = urlopen(baseURL + "&field1=%s" % (str(pressure)))
f.close() 

from subprocess import call
Upload = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /var/www/meteodeep/pressurearchiveddata.txt /PressureArchivedData.txt"
call ([Upload], shell=True)

# crontab
# 0 * * * * sudo /usr/bin/python3 /var/www/meteodeep/LivePressureArchive.py
