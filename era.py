def era(input_list:str,tol:int)->int:
    my_list = [int(d) for d in input_list.split(' ')]
    count_down = 0
    for i in range(max(my_list)):
        if i+1<my_list[i]:
            my_list.insert(i,i+1)
            count_down+=1
    return count_down
print(era("1 2 5 7 4",5))