def triangle_area(a,b,c):
    s = (a+b+c)/2
    sa = s-a
    sb = s-b
    sc = s-c
    sofeverything = s*sa*sb*sc
    area = sofeverything **.5
    print(area)
    return area

def circle_area(radius):
    properarea = 3.1415 * (radius ** 2)
    area = round(properarea, 2)
    print(area)
    return area

def trapezoid_area(base_1, base_2, height):
    base=base_1+base_2
    area = .5*base*height
    print(area)
    return area


def rectangle_area(base, height):
    area = base * height
    print(area)
    return area
