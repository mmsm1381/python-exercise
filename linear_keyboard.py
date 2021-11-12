def keyboard_function(keyboard:str,goal:str)->int:
    keyboard_dict = {}
    i = 1
    for words in keyboard:
        keyboard_dict[words]=i
        i+=1
    current_word = keyboard_dict[goal[0]]
    time = 0
    for i in range(1,len(goal)):
        time+=abs(current_word-keyboard_dict[goal[i]])
        current_word = keyboard_dict[goal[i]]
    return time
print(keyboard_function("abcdefghijklmnopqrstuvwxyz","codeforces"))
