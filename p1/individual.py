c = float(input("Enter temperature (Celsius) : "))
f = c * 1.8 + 32
k = c + 273.15
print("Temperature (Fahrenheit) = {0:5.2f} \n"
      "Temperature (Kelvin) = {1:5.2f}".format(f, k))