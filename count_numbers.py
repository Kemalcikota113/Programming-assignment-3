import os


def makelist(path):
    lst = []
    with open(path, "r") as file:
        as_str = file.read()

        if ", " in as_str:
            as_str = as_str.replace("\n", ", ")

            string_list = as_str.split(", ")

            for s in string_list:
                if s != "":
                    lst.append(int(s))

        if ":" in as_str:
            string_list = as_str.split(":")

            for s in string_list:
                lst.append(int(s))

    return lst

def count_different(lst):
    return len(set(lst))


def count_occourences(lst):
    set = {i: lst.count(i) for i in lst}

    sorted_lst = sorted(set.items(), key=lambda tup: tup[1], reverse=1)

    return sorted_lst[0: 5]



path = "E:\\1DV501\\10000_integers\\file_10000integers_A.txt"
lst = makelist(path)
print("difference of file A: ", count_different(lst))
print("set of file A: ", count_occourences(lst))

path = "E:\\1DV501\\10000_integers\\file_10000integers_B.txt"
lst = (makelist(path))
print("difference of file B: ", count_different(lst))
print("set of file A: ", count_occourences(lst))
