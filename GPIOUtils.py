import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def setAsOutputPin(pin):
	"""
	Sets the given pin as an output pin
	:param pin: pin which is to be set as output pin
	"""

	GPIO.setup(pin, GPIO.OUT)


def setAsInputPin(pin):
	"""
	Sets the given pin as an input pin
	:param pin: pin which is to be set as input pin
	"""

	GPIO.setup(pin, GPIO.IN)


def setOutputHighOnPin(pin):
	"""
	Sets output high on the given pin number
	:param pin: the pin which is to be turned on
	"""

	GPIO.output(pin, True)


def setOutputLowOnPin(pin):
	"""
	Sets output low on the given pin number
	:param pin: the pin which is to be turned off
	"""

	GPIO.output(pin, False)
