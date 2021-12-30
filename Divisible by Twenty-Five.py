
def divisible(plain_text:str)->int:

    count = 0
    if plain_text[0]=="0" and len(plain_text)>1:
        return count

    elif "_" in plain_text:
        for i in range(0,10):
            index = plain_text.find("_")
            new = plain_text[:index] + str(i)+plain_text[index+1:]
            count +=divisible(new)

    elif "X" in plain_text:
        for n in range(0,10):
            new = plain_text.replace("X",str(n))
            count += divisible(new)

    else :
        if  not int(plain_text)%25:
            count+=1  
 

    return count

input_1 = input()
print(divisible(input_1))

