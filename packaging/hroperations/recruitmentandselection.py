def applications():
    ''' prints applictions '''
    import random
    import string 
    applis = dict(applicants = random.choices(string.ascii_uppercase, k = 5), qualifications = random.choices(['mba', 'bba', 'mca', 'bca', 'ba', 'bsc'], k = 5))
            
    return(applis)


if __name__ == '__main__':
    for k, v in applications().items():
        print(v)
