#!/usr/bin/python3

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    _base = 1
    if exp > 0:
        for i in range(exp):
            _base = _base * base
    return _base

if __name__ == "__main__":
    print(iterPower(-2.29, 10))
                                                          
