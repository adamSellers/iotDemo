from envirophat import light
from envirophat import motion

from time import sleep
import sys
while True:
    print [light.light(), motion.accelerometer().z]
    sys.stdout.flush()
    sleep(3)
