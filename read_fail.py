#!/bin/env python3
import RPi.GPIO as GPIO
import time

# Set the GPIO pin number where the DHT sensor's data pin is connected.
LINEFAIL_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LINEFAIL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def linefail_callback(channel):
    print("⚠️ Line fail detected! (pin shorted to ground)")


print(f"Reading pullup on GPIO {LINEFAIL_PIN}...")
print("Press Ctrl+C to exit.")

GPIO.add_event_detect(
    LINEFAIL_PIN, GPIO.FALLING, callback=[linefail_callback], bouncetime=200
)

print("Monitoring UPS line fail on pin 37 (GPIO26). Press Ctrl+C to exit.")

try:
    while True:
        time.sleep(1)  # keep the script alive
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    GPIO.cleanup()
