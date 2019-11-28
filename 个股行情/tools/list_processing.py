# 此方法用处是使列表化为以任意个元素组成的列表组
def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) * children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list


def list_bond(init_list):
    main_list = []
    for i in init_list:
        for n in i:
            main_list.append(n)
    return main_list
