class TempConversion:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


# Example usage:
# Convert 20 degrees Celsius to Fahrenheit
temperature_in_celsius = 20
print(f"{temperature_in_celsius}ºC is {TempConversion.celsius_to_fahrenheit(temperature_in_celsius)}ºF")

# Convert 68 degrees Fahrenheit to Celsius
temperature_in_fahrenheit = 68
print(f"{temperature_in_fahrenheit}ºF is {TempConversion.fahrenheit_to_celsius(temperature_in_fahrenheit)}ºC")
