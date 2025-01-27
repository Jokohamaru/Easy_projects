import arithmetic_operators as ao

user_input = input("Nhap phep tinh: ").split(" ")
print(user_input)

if "+" in user_input:
    print(ao.plus(int(user_input[0]),int(user_input[2])))
elif "-" in user_input:
    print(ao.minus(int(user_input[0]),int(user_input[2])))
elif "/" in user_input:
    print(ao.devide(int(user_input[0]),int(user_input[2])))
else:
    print(ao.multiple(int(user_input[0]),int(user_input[2])))






