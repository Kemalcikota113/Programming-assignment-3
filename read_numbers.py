import os
import math


def read_integers1(path):
    lst = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            string_list = line.split(", ")
            for s in string_list:
                lst.append(int(s))
    return lst

def read_integers2(path2):
    lst2 = []
    with open(path2, "r") as file:
        for line in file:
            line = line.strip()
            string_list = line.split(":")
            for s in string_list:
                lst2.append(int(s))
    return lst2

def mean(lst):
    sum = 0
    for i in lst:
        sum += i
    mean = sum / len(lst)
    return mean

def std(lst):
    mean_value = mean(lst)
    newlst = []

    for i in range(len(lst)):
        newlst.append((lst[i] - mean_value)**2)

    std = math.sqrt(sum(newlst) / len(newlst))

    return std




path = "E:\\1DV501\\10000_integers\\file_10000integers_A.txt"
path_2 = "E:\\1DV501\\10000_integers\\file_10000integers_B.txt"
lst1 = read_integers1(path)
lst2 = read_integers2(path_2)

print("file_10000integers_A.txt: \n", lst1)
print("file_10000integers_B.txt: \n", lst2)
print()
print("The median of file_A is : ", mean(lst1))
print("The standard value of file_A is:", std(lst1))
print("The median of file_B is: ", mean(lst2))
print("The standard value of file_B is:", std(lst2))