target = 5
nums = [0,2,3,1]
dic = {}

for index, n in enumerate(nums): 
    #print(index, n)
    
    if n in dic:
        print(n , index)
        print([dic[n], index])

    dic[target-n] = index

print(dic)