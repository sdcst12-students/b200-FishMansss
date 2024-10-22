

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in either of the lists
    # duplicate values will be ignored
    union = []
   #list1 == list1.sort(),list2 == list2.sort()

    union = set(list1).union(list2)
    union = list(union)
    union.sort()
    print(union)
    return union   


easy1 = [5,10,15,2,4,6,8]
easy2 = [-2,-4,-6,2,4,6,0.1]

getUnion(easy1,easy2)


'''
common = set(list1).intersection(list2)










'''