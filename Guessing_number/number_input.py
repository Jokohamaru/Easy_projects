def num_input():
    try:
        user_input = int(input("Nhap gia tri tu 0 - 100:"))
        if user_input < 0 or user_input > 100:
            print("Khong dung khoang gioi han!!! (0 - 100)")
            num_input()
        return user_input
        
    except ValueError as e:
        print(f"Loi {e}, nhap khong dung gia tri (0 - 100) ")
        num_input()
    except Exception as e:
        print(f"Loi khong xac dinh {e}")
        num_input()

