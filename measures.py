def feet_to_inches(feet):
    out = feet * 12
    print(out)
    return out

def feet_to_meters(feet):
    calc = feet / 3.281
    out = round(calc, 2)
    print(out)
    return out

feet_to_inches(3)
feet_to_meters(12)