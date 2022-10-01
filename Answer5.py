#Answer5
def twoSum(nums, target):
    sums = []
    for i in range(len(nums)):
        add=nums[i+1:]
        for j in range(len(add)):
            if(nums[i]+add[j]==target):
                
                print(nums[i],"+",add[j],'=',nums[i]+add[j])
                return i,j+i+1
            
               
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9