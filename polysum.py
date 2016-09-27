from math import pi, tan

def polysum(n, s):
    '''
    n = number of sides, s = length of side
    returns sum of polygon's area and perimeter squared
    '''
    area_polygon = (0.25 * n * s**2) / tan(pi/n)
    per_polygon = n * s
    sq_per = per_polygon**2
    sum = area_polygon + sq_per
    return float("%.4f" % sum)

if __name__ == "__main__":
    polysum(7, 3.5)
