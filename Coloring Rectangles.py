def coloring(m:int,n:int)->int:

    count = 0

    if not m%3:
        count+=n

    if not n%3:
        count+=m
    
    if n==2 and m==2:
        count+=2    
    elif n%3 and m%3:
        if n>m:
            count+= coloring(m,n%3)
            count+= coloring(m,3*(n//3))
        else : 
            count += coloring(m%3,n)
            count += coloring(3*(m//3),n)

    
    return count

number = int(input())

for i in range (number):
    input_1 = input().split(" ")
    print(coloring(int(input_1[0]),int(input_1[1])))