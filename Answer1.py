#Answer 1:
def calculate(min,max,step):
    sums=0 
    for i in range(min,max+1,step):
        sums += i 
        if(sums != 6 and sums != 18 and sums != 0  ):
           continue  
        print("result = ",sums)
        
    
calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)
