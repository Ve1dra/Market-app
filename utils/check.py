list_oj = []

def func():
    yield("Hello David!")
list_oj.append(func)
print(list_oj)

name = 1
print(hex(id(name)))
dict_obj = {
    name: func(),
    "name": map(lambda greet: print(greet), func())
}

print(hex(id(dict_obj[name])))


my_name = "Abdulrasheed"
list_name = []


for i in my_name:
    print(i)
    list_name.append(i)
print(list_name)

dict_num = {"num1": 1, "num2": 2}

try:
    number_in = int(input("Enter any number: "))
except ValueError:
    print("This is not a valid number")
    print(dict_num)
else:
    print(dict_num.items(), f"Length of dictionary is {len(dict_num)}")
    dict_num.update({'num3': number_in})
    print(dict_num)