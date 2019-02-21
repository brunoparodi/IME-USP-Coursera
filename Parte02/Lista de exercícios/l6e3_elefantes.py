def incomodam(n):
    if int(n) <= 0:
        return ''
    if int(n) > 0:
        return 'incomodam ' + str(incomodam(int(n-1)))


def elefantes(n):
    if n <= 0:
        return ''
    if n == 1:
        return 'Um elefante incomoda muita gente\n'
    else:
        return (elefantes(n-1) +
    str(n) +
    " elefantes " +
    incomodam(n) +
    "muito mais\n"
    + str(n) +
    " elefantes incomodam muita gente\n")

def teste():
    print(elefantes(4))

    print(elefantes(1))

    print(elefantes(2))
