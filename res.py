def a(string_a):
    list_a = string_a.split(",")
    len_list_a = len(list_a)
    for i in range(len_list_a):
        list_a[i] = int(list_a[i]) ** 2
    return list_a 
string_a = input()
number_list = a(string_a)
print(number_list)