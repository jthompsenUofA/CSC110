def celsius_to_fahrenheit(celsius):
    calc = (celsius * 1.8) + 32
    out = round(calc, 2)
    print(out)
    return out

def fahrenheit_to_celsius(fahrenheit):
    calc = (fahrenheit - 32) * (5/9)
    out = round(calc, 2)
    print(out)
    return out

celsius_to_fahrenheit(20)
fahrenheit_to_celsius(72)
