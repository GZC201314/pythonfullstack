#__author:gzc
#date:2018/11/16

import random


def foo():
    v_code = ""
    for i in range(5):
        randomNum = random.randrange(0,2)
        if randomNum ==0:
            v_code += str(random.randrange(10))
        else:
            v_code += chr(random.randrange(65,91))
    print(v_code)
    return v_code

foo()
foo()
foo()
foo()
foo()
foo()
foo()
foo()
foo()
foo()



