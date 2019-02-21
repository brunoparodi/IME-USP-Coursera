def maximo(x, y , z):
    if x > y > z or x > z > y :
        return x
    if y > x > z or y > z > y:
        return y
    if z > x > y or z > y > x:
        return z
    return x
