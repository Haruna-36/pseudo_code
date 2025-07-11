year = int(input("年を入力："))

if year % 4 == 0 and year % 400 != 0:
    print("leap year")
else:
    print("not leap year")
