
def g(x,y):
    if x <= y:
        return 1
    else:
        return g(x-y+1,1)
    
print(g(3,2))