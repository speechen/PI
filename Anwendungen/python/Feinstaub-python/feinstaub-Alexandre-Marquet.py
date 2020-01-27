from machine import UART
import time
import sds011

uart = UART(1, baudrate=9600, pins=('P21','P22'))
dust_sensor = sds011.SDS011(uart)
dust_sensor.sleep()

while True:
    #Datasheet says to wait for at least 30 seconds...
    print('Start fan for 5 seconds.')
    dust_sensor.wake()
    time.sleep(5)

    #Returns NOK if no measurement found in reasonable time
    status = dust_sensor.read()
    #Returns NOK if checksum failed
    pkt_status = dust_sensor.packet_status

    #Stop fan
    dust_sensor.sleep()

    if(status == False):
        print('Measurement failed.')
    elif(pkt_status == False):
        print('Received corrupted data.')
    else:
        print('PM25: ', dust_sensor.pm25)
        print('PM10: ', dust_sensor.pm10)

    time.sleep(10)