print("welcome to my computer game! ")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay lets play! ")
score = 0


answer = input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect! ")

answer = input(" what does gpu stand for ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect! ")

answer = input("what does ram stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect! ")

answer = input("what does psu stan for? ")
if answer.lower() == "power supply":
    print("correct")
    score += 1
else:
    print("incorrect! ")

answer = input("")
if answer.lower() == "":
    print("correct")
    score += 1
else:
    print("incorrect! ")

print("you got " + str(score) + " question correct")


i = 1

while i <= 10:
    print(i)
    i += 1

