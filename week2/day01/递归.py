#__author:gzc
#date:2018/11/6

def fet(n):
    if(n==1):
        return 1
    return fet(n-1)*n




print(fet(30))