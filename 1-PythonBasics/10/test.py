#  We don't have the unnecessary code defination here and the code is looking cleaner 

#  Here python will check whether maths file is in current directory or not to import classes 
#  If does not find math here then it will check where python is installed 
# we can import functions as well

from maths import Calculator, add
# from maths import *    # we can also do that here => astric means everything 
from complex_function import ComplexFunction

calc = Calculator()
cf = ComplexFunction()

calc.add(1,2)
calc.subtract(1,2)
calc.multiple(1,2)

cf.check_even_or_odd(12)
cf.check_even_or_odd(1)
cf.check_even_or_odd(100)
cf.check_even_or_odd(3)

add(1,2)

