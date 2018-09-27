old_password = input("voer uw oude wachtwoord in")
new_password = input("voer uw nieuwe wachtwoord in")

if old_password != new_password:
    if len(new_password) >= 6:
        print(True)
    else:
        print(False)

else:
    print(False)
