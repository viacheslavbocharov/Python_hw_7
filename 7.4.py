def common_elements():

    def lst_multiple_of_number_in_range(number, range):

        lst = []
        for i in range:
            if i % number == 0:
                lst.append(i)
        return lst

    # used range(100) because in final result have to be {0, 75, 45, 15, 90, 60, 30} as in HW example
    lst1 = lst_multiple_of_number_in_range(3, range(100))
    lst2 = lst_multiple_of_number_in_range(5, range(100))
    return set(lst1).intersection(set(lst2))


print(common_elements())
