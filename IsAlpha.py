if __name__ == '__main__':
    s = input()
    Checkalphanum = False
    Checkalpha = False
    CheckDigits = False
    CheckLowercase = False
    CheckUpper = False
    for i in s.split(" "):
        print(i)
        if i.isalnum():
            Checkalphanum = True
            break
    for i in s:
        if i.isalpha() == True:
            Checkalpha = True
        if i.isdigit() == True:
            CheckDigits = True
        if i.islower() == True:
            CheckLowercase = True
        if i.isupper() == True:
            CheckUpper = True
print(Checkalphanum)
print(Checkalpha)
print(CheckDigits)
print(CheckLowercase)
print(CheckUpper)
