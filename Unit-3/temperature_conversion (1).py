# Create a Temperature class. Create 2 methods named convertFarenheit() and convertCelsius().

class Temperature:
    def convertFahrenheit(self, c):
        f = (c * 9/5) + 32
        return f

    def convertCelsius(self, f):
        c = (f - 32) * 5/9
        return c


t = Temperature()
print("Celsius to Fahrenheit:", t.convertFahrenheit(30))
print("Fahrenheit to Celsius:", t.convertCelsius(86))
