def is_in_revised(x, col):
    dic = x[col]
    for val in dic.values():
        if val >= 2:
            return True
    return False