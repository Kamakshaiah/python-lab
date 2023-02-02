def catDat(x):

    ''' Creates categorical data.
        Input: 'x' should be a random vector of numbers.
        Output: A list of categories along with frequencies.  '''
    
    a = b = c = d = 0
    a; b; c; d

    for i in x:
        if i == 1:
            a = a + 1
        elif i == 2:
            b = b + 1
        elif i == 3:
            c = c + 1
        elif i == 4:
            d = d + 1

    data = [('one', a),
            ('two', b),
            ('three', c),
            ('four', d)]
    y = []
    z = []

    for i in data:
        y.append(i[0])
        z.append(i[1])
    return y, z
