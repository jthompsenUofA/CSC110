def celsius_to_fahrenheit(celsius):
    out = (celsius * 1.8) + 32
    print(out)
    return out

def fahrenheit_to_celsius(fahrenheit):
    out = (fahrenheit - 32) * (5/9)
    print(out)
    return out

celsius_to_fahrenheit(20)
fahrenheit_to_celsius(72)