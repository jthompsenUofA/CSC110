def triangle_area(a,b,c):
    s = (a+b+c)/2
    sa = s-a
    sb = s-b
    sc = s-c
    sofeverything = s*sa*b*sc
    area = sofeverything **.5
    print(area)
    return area

def circle_area(radius):
    squared = radius ** 2
    area = 3.145 * squared
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
