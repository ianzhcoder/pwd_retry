#while True:
time = 0
while time < 4:
    password = 'a123456'
    user_pw = input("Please enter your password:")
    if user_pw == password:
        print("登入成功!")
        break
    else:
        time = time + 1
        print ("密碼錯誤!")
        if time < 3:
            print ("還有", 3-time, "次機會")
        else:
            print ("猜錯三次,鎖定帳號!")
            break
