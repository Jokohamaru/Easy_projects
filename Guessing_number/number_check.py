def check_num (num , right_num):
    if num == right_num:
        print(f"That right, the secret number is :{right_num}")
        return False
    elif -10 < right_num - num < 10:
        print("Almost there!!! Again.")
    return True
    