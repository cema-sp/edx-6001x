def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    res = {}
    for key, value in d.iteritems():
        try:
            res[value].append(key)
        except KeyError:
            res[value] = [key]

    for key in res:
        res[key].sort()

    return res

