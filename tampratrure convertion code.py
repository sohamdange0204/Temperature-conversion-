# Temperature conversion
unit = input("Is this temp in Celsius or Fahrenheit (C/F): ").strip().upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    converted_temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {converted_temp}°F")
elif unit == "F":
    converted_temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {converted_temp}°C")
else:
    print(f"'{unit}' is an invalid unit. Please enter 'C' or 'F'.")
