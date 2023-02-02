 # import module sys to get the type of exception
import sys
##randomList = ['a', 0 , 2]
##for entry in randomList :
##    try :
##        print (" The entry is", entry )
##        r = 1/int ( entry )
##        break
##    except :
##        print (" Oops !", sys . exc_info ()[0], " occurred .")

##try:
##    f = open('myfile.txt')
##    s = f.readline()
##    i = int(s.strip())
##    print(s)
##except OSError as err:
##    print('OS error: {}'.format(err))
##except ValueError :
##    print('Could not convert data to an integer.')
##except:
##    print ('Unexpected error :', sys.exc_info())
##    raise

##for arg in sys.argv[1:]:
##    try:
##        f = open(arg, 'r')
##    except OSError :
##        print('cannot open', arg)
##    else:
##        print(arg , 'has', len(f.readlines()), 'lines')
##        f.close()
        
##try:
##    raise Exception('spam', 'eggs')
##except Exception as inst:
##    print(type(inst))    # the exception instance
##    print(inst.args)     # arguments stored in .args
##    print(inst)          # __str__ allows args to be printed directly,
##                         # but may be overridden in exception subclasses
##    x, y = inst.args     # unpack args
##    print('x =', x)
##    print('y =', y)

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
