array =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
found = False
def balance(arr, find):
    treeOrder =[]
    global found
    # found = False
    def findingRoot(array):
        finding0Root = array[(len(array)//2)]
        print(finding0Root)
        treeOrder.append(finding0Root)
        print("line 28",finding0Root)
        print("line 29",find)
        print(finding0Root == find)
        if finding0Root == find:
            for i in array:
                array.remove(i)
            global found
            found = True
            return found
            
        else:     
            array.remove(finding0Root)    
        
    while len(arr) > 0 and found == False:   
        findingRoot(arr)
    
        rootindex = (len(arr)//2)
        print(treeOrder)
        
        
        left = arr[0:rootindex]
        print(arr[0:rootindex])
            
            
        right = arr[rootindex:]
        print(arr[rootindex:])
            
            
            
        if find < treeOrder[len(treeOrder)-1]:
            for i in right:
                array.remove(i)
            while len(left) > 0:
                findingRoot(left)
                print(left)
            
            # for num in len(left):
            #     left.remove(num)

        if find > treeOrder[len(treeOrder)-1]:
            for i in left:
                array.remove(i)
            while len(right) > 0:
                findingRoot(right)
                print(right)
            # for num in len(right):
            #     right.remove(num)
            # treeOrder += right
    if found == False:
        return "Not Found"
    else:
        return "Found"
    return treeOrder

    

print(balance(array, 4))

