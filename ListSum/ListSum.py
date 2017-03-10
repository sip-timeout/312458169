def get_list_one_by_one(lst):
    """ get list of numbers, strings are ignored. return: list of numbers """
    print('Type a number, type "stop" to end the list')
    member = input()
    if(member == "stop"):
        return lst
    else:
        if(member.isdigit()):
            lst.append(int(member))
        else:
            print("{} is ignored, not a number".format(member))
        return get_list_one_by_one(lst)


def get_full_list(lst):
    """ get list of numbers, if typed not a number, user must retype. return: list of numbers """
    while True:
        print("Type values seperated by a comma")
        list_as_str = input()
        lst = (list_as_str.split(","))
        # Convert list members to integer
        try:
            lst = list(map(int, lst))
            break
        except ValueError:
            print("Error: all members must be numbers, try again")
    return lst


def get_list_input():
    """ return: input option type 'o' or 'f' """
    print('Choose list input type, "o" - one by one or "f" - full list ')
    input_type = input()
    return input_type


def sum_list_members(lst):
    """ sum int list members """
    return sum(lst)


def list_sum():
    """ Main function """
    lst = []
    input_type = get_list_input()
    if (input_type == "o"):
        lst = get_list_one_by_one(lst)
    elif (input_type == "f"):
        lst = get_full_list(lst)
    lst_sum = sum_list_members(lst)
    print("The sum of the list: {0} members is {1}".format(lst,lst_sum))


list_sum()