
def help_():
    print('this is just a demo package for dummy modules and scripts')
    
from .module1 import mod_one_func_one, mod_one_func_two
from .module2 import mod_two_func_one, mod_two_func_two
from .subpackage.modinsubpack import *
