# Write a program that converts Celsius temperature to Fahrenheit temperatures.
# 9/25/2018
# CTI-110 P2HW1 - Celsius Fahrenheit Converter
# Cary Eaglin

#Greet user
print("Greetings User.")
#Ask for temperature to convert
celsius = float(input("What is the temperature in Celsius? "))
#Convert temperature
fahren = celsius *1.8 + 32
#Display results
print("The temperature in Fahrenheit is: ", fahren)
