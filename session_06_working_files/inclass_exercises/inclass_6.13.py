# 6.13:  Create a static method.

# To the below class add the static method ftoc(temp) which
# converts a temperature in Fahrenheit to Celsius.
# 
# The formula is (temp - 32) * 5 / 9
# 
# To be a static method, the method must not take self as an
# argument, and must be decorated with @staticmethod.

class Forecast:

    def __init__(self, forecast, high=0, low=0):
        self.text = forecast
        self.hightemp = high
        self.lowtemp = low

    # your ftoc(temp) static methood here



t = Forecast('Light rain', high=62, low=48)


print(t.ftoc(32))       # 0.0
print(t.ftoc(212))      # 100.0

# Expected Output:

# 0.0
# 100.0

