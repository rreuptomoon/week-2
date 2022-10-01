def maxProduct(nums):
    indexA = nums[0]
    indexB = nums[1]
    
    res=[]
    for i in range(len(nums)):
        if nums[i]!= indexA:
            res.append(indexA*nums[i])
        #print(res3
    if len(nums)>=3:
        indexC = nums[2]
        for i in range(len(nums)):
            if nums[i]!= indexB and nums[i]!= indexA:
                res.append(indexB*nums[i])
        #print(res)
        for i in range(len(nums)):
            if nums[i]!= indexB and nums[i]!= indexA and nums[i]!= indexC:
                res.append(indexC * nums[i])
        #print(res)

    max = res[0]
    for b in range(len(res)):
        if res[b] > max :
            max = res[b]
    print(max)


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10
