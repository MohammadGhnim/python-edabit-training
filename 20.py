
'''

Temperature Conversion

Write a program that takes a temperature input in celsius and converts it to Fahrenheit and Kelvin.
Return the converted temperature values in a list.

The formula to calculate the temperature in Fahrenheit from Celsius is:

F = C*9/5 +32

The formula to calculate the temperature in Kelvin from Celsius is:

K = C + 273.15


Notes
Return calculated temperatures up to two decimal places.
Return "Invalid" if K is less than 0.


'''

def temp_conversion(celsius):
    f = round(celsius * 9 / 5 + 32, 2)
    k = round(celsius * 273.15 , 2)
    if k < 0:
        return "invalid"
    else:
        return[f, k]
