import RPi.GPIO as GPIO
from utils import dht11

from influxdb import InfluxDBClient

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor = dht11.DHT11(pin=4)

client = InfluxDBClient(database='sensors')

while 1:
    result = sensor.read()
    if result.error_code == 0:
        temperature = result.temperature
        humidity = result.humidity + 40
        json_body = [
            {
                "measurement": "temperature",
                "fields": {
                    "Float_value": temperature
                }
            },
            {
                "measurement": "humidity",
                "fields": {
                    "Float_value": humidity
                }
            }
        ]
        client.write_points(json_body)