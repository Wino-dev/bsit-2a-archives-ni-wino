name = input()
age = input()
currentHour = int(input())

if currentHour >= 4 and currentHour < 12:
    print(f"Good morning, {name}! You are currently {age} years old.")
elif currentHour >= 12 and currentHour < 6:
    print(f"Good afternoon, {name}! You are currently {age} years old.")
else:
    print(f"Good evening, {name}! You are currently {age} years old.")