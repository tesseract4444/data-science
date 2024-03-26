def celsius_to_fahrenheit(degrees_celsius: float) -> float:
    return degrees_celsius * 1.8 + 32


def fahrenheit_to_celsius(degrees_fahrenheit: float) -> float:
    return (degrees_fahrenheit - 32) * 5/9


def celsius_to_kelvin(degrees_celsius: float) -> float:
    return degrees_celsius + 273.15


def kelvin_to_celsius(degrees_kelvin: float) -> float:
    return degrees_kelvin - 273.15


def fahrenheit_to_kelvin(degrees_fahrenheit: float) -> float:
    return (degrees_fahrenheit + 459.67) * 5/9


def kelvin_to_fahrenheit(degrees_kelvin: float) -> float:
    return degrees_kelvin * 1.8 - 459.67


print(celsius_to_fahrenheit(37.68))
print(fahrenheit_to_celsius(212))
print(celsius_to_kelvin(212))
print(kelvin_to_celsius(0))
print(fahrenheit_to_kelvin(32))
print(kelvin_to_fahrenheit(309))
