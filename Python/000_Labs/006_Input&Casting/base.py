def add(x,y):
    sum = x + y
    return sum 
    
def mult(x,y):
    prod = x * y
    return prod
    
def printlist(lst):
    i = 1 
    for item in lst:
        print(str(i) + "." + item)
        i = i + 1
    
def addlist(lst):
    sum = 0
    for number in lst:
        sum = sum + number
    return sum
#--------------------------------    
    ans = add(8,3)
    print(ans)
    
christmasList = ["air pods", "PC", "bow and arrow", "car", "money"]
printlist(christmasList)
    
listfavnum = [67, 43, 41, 21, 27, 2, 6, 7]
print(addlist(listfavnum))
        
    
    