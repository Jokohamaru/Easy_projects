import random
import number_check
import number_input 

correct_number = random.randint(0,100)
print(correct_number)
condition = True
while condition == True:
    user_input = number_input.num_input()
    condition = number_check.check_num(user_input,correct_number)

print("Thank")


        