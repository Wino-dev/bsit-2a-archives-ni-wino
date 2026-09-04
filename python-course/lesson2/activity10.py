print("Spelling Bee Game")

points = 0

print("Description: A common instrument with 6 strings and is played with hands by strumming/plucking the strings.")

user_answer = input("Your Answer: ")
answer = "guitar"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A small insect that can carry more than its own weight.")

user_answer = input("Your Answer: ")
answer = "ant"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A hardware device that displays a computer's visual output.")

user_answer = input("Your Answer: ")
answer = "monitor"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A book containing a word's meaning and use case.")

user_answer = input("Your Answer: ")
answer = "dictionary"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A portable desktop computer that runs on battery.")

user_answer = input("Your Answer: ")
answer = "laptop"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: An electronic component that resists current in a circuit.")

user_answer = input("Your Answer: ")
answer = "resistor"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A device worn over the head that outputs audio signals.")

user_answer = input("Your Answer: ")
answer = "headset"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A device that tracks its movement and sends signals to a computer's cursor.")

user_answer = input("Your Answer: ")
answer = "mouse"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print("Description: A device worn on the wrist that tracks the time.")

user_answer = input("Your Answer: ")
answer = "watch"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")

print("Description: An accessory with two dark lenses that blocks harmful light from reaching the eyes.")

user_answer = input("Your Answer: ")
answer = "sunglasses"

if user_answer.lower() == answer:
    print("Correct Answer!")
    points += 1
else:
    print("Incorrect Answer!")
    
print(f"Points: {points}")