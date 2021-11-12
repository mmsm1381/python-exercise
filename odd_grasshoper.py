def grass_hoper_function(x:int,n:int)->int:
    current_jump = 1
    while current_jump<=n:
        if not x%2 or x==0:
            x-=current_jump
            current_jump+=1
        else:
            x+=current_jump
            current_jump+=1
    return x
print(grass_hoper_function(10,10))
