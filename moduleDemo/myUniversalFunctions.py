def checkIfNotNumeric(*args):
    for i in args:
        if not isinstance(i, (int, float)):
            return False
    return True

def addAllNumerics(*args):
    s = 0
    for x in args:
        s += x
    return s

def myName():
    print("Python Course")