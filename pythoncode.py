import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import spidev
GPIO.setmode(GPIO.BCM)
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=50000

sensor = Adafruit_DHT.DHT11
pin = 17
humidity, temperature = Adafruit_DHT,read_retry(sensor,pin)

def read_spi_adc(adcChannel):
  adcValue=0
  buff=spi.xfer2([1,(8+adcChannel)<<4,0])
  adcValue = ((buff[1]&3)<<8)+buff[2]
  return adcValue
try:
  while True:
   adcValue=read_spi_adc(0)
   print("Soil Water Sensor : %d" %(adcValue))
   time.sleep(0.5)
adcValue=read_spi_adc(1)
   print("Soil Water Sensor : %d" %(adcValue))
   time.sleep(0.5)
   if humidity is not None and temperature is not None:
    print("Temp : ", temperature)
    print("Humi : ", humidity)

finally:
  GPIO.cleanup()
  spi.close()