#Answer 1:

def calculate(min,max,step):
    sums=0
    i=min
    while i<=max:
        sums+=i
        i+=step
    print(sums)#
                     
calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)
calculate(1,6,1)
