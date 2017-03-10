def get_list_one_by_one(lst):
    print('Enter a number, type "stop" to end the list')
    member = input()
    if(member == "stop"):
        return lst
    else:
        lst.append(int(member))
        return get_list_one_by_one(lst)

def get_full_list(lst):
    print("Type values seperated by a comma")
    list_as_str = input()
    list_as_str.split(",").join()
    for member in range(0,len(list_as_str)):
        lst.append(member)
    return lst

def list_sum():
    lst = []
    print('Choose list input type, "o" - one by one or "f" - full list ')
    input_type = input()
    if(input_type == "o"):
        get_list_one_by_one(lst)

    elif(input_type == "f"):
        get_full_list(lst)
    print(type(lst))
    print(lst)
list_sum()

