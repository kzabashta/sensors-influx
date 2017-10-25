import RPi.GPIO as GPIO
from utils import dht11

from influxdb import InfluxDBClient

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor = dht11.DHT11(pin=4)

def getTemperature():
    while 1:
        result = instance.read()
        if result.temperature > 0:
            return result.temperature
        else:
            print result

def getHumidity():
    while 1:
        result = instance.read()
        if result.humidity > 0:
            return result.humidity

client = InfluxDBClient(database='dbname')

while 1:
    result = sensor.read()
    while 1:
        
    json_body = [
        {
            "measurement": "temperature",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

print getHumidity()