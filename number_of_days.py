year = int(input("年を入力"))
month = int(input("月を入力"))

if year % 4 == 0 and year % 400 != 0:
    if month in [1,3,5,7,8,10,12]:
        print(31)
    elif month in [4,6,9,11]:
        print(30)
    elif month in [2]:
        print(29)

else:
    if month in [1,3,5,7,8,10,12]:
        print(31)
    elif month in [4,6,9,11]:
        print(30)
    elif month in [2]:
        print(28)
