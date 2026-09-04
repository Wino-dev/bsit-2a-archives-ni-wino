age = int(input())
hour = int(input())

if age < 18 and hour >= 10 or hour <= 4 :
    print("Not allowed to go outside")
else:
    print("Allowed to go outside")