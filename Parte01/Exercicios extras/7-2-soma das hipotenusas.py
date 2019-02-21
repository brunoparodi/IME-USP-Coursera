import math

def hip(cat1,cat2):
    hip = math.sqrt((cat1 ** 2) + (cat2 ** 2))
    return hip

def soma_hipotenusas(h):
    cat1 = 3
    cat2 = 4
    contador = 0
    hip = 5
    result_hip = 0
    while cat1 < h:
        while cat2 < h:
            while hip <= h:
                if hip == math.sqrt((cat1 ** 2) + (cat2 ** 2)):
                    contador = contador + 1
                    result_hip = hip + resul_thip     
                hip = hip + 1
            hip = 5
            cat2 = cat2 + 1
        cat2 = cat1 + 1
        cat1 = cat1 + 1
    return resulthip
            
