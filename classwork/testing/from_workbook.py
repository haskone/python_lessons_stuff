from copy import copy

def gen_sublist(lst):
    result = [[]]
    for i in lst:
        result.append([i])
    
    for lenght in range(len(lst))[2:]:               
        for i in range(len(lst) - lenght + 1):                
            result.append(lst[i:i+lenght])
    
    if lst:
        result.append(copy(lst))    
    return result
