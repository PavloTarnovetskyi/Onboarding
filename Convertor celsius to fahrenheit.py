celsius = int(input("Enter an integer value of temperature in celsius:"))


def fahrenheit(c):
    return 1.8 * c + 32


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(float(fahrenheit(celsius))))

