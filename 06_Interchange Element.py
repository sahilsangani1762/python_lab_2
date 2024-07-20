def interchange_elements(lst):
    if len(lst) > 1:
        new_lst = lst.copy()
        new_lst[0], new_lst[-1] = new_lst[-1], new_lst[0]
        return new_lst
    return lst
lst = [12, 35, 9, 56, 24]
result = interchange_elements(lst)
print("Input: ", lst)
print("Output:", result)